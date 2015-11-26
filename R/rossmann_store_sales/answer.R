main <- function(train_csv_path, export_csv_path, best_choices_csv_path,from_store_id, to_store_id){
    source("evaluate_helper.R")
    # best_choices_csv_path <- "best_choices.csv"
    best_choices <- read.csv(best_choices_csv_path, header=TRUE)
    # best_choices$Store <- as.integer(rownames(best_choices))
    # train_csv_path <- 'data/train_20.csv'
    train_raw <- read.csv(train_csv_path, header=TRUE)

    train_clean <- train_raw[train_raw$Open==1,]

    # 54 rows, cause log_regression wrong
    # train_clean <- train_clean[train_clean$Sales!=0,]

    # from_store_id <- 183
    # to_store_id <- 192
    train_clean <- train_clean[train_clean$Store>=from_store_id,]
    train_clean <- train_clean[train_clean$Store<=to_store_id,]

    train_clean$Date <- as.Date(train_clean$Date)
    train_clean$Month <- as.integer(format(train_clean$Date, "%m"))
    train_clean$Week <- as.integer(format(train_clean$Date, "%U"))
    train_clean$DateInt <- as.integer(train_clean$Date)
    train_clean$Year <- as.integer(format(train_clean$Date, "%Y"))

    test_csv_path <- 'data/test.csv'
    test_raw <- read.csv(test_csv_path, header=TRUE)
    test_raw$Sales<-NA

    test_clean <- test_raw[test_raw$Open==1,]
    test_clean <- test_clean[test_clean$Store>=from_store_id,]
    test_clean <- test_clean[test_clean$Store<=to_store_id,]
    test_clean <- test_clean[!is.na(test_clean$Store),]

    test_clean$Date <- as.Date(test_clean$Date)
    test_clean$Month <- as.integer(format(test_clean$Date, "%m"))
    test_clean$Week <- as.integer(format(test_clean$Date, "%U"))
    test_clean$DateInt <- as.integer(test_clean$Date)
    test_clean$Year <- as.integer(format(test_clean$Date, "%Y"))

    train_set <- train_clean
    test_set <- test_clean
    test_result <- predict_all(train_set, test_set, best_choices)
    test_result <- test_result[!is.na(test_result$Sales),]
    # write.table(test_result, file=export_csv_path, sep=",")


    test_raw$Sales<-0

    source <- test_result
    target <- test_raw
    key_column <- 'Id'
    value_column <- 'Sales'
    submit_result <- match_data(source, target, key_column, value_column)
    write.table(submit_result[,c('Id','Sales')], file=export_csv_path, row.names=FALSE,sep=',')

}



check_result <- function(){
    train_csv_path <- 'data/train.csv'
    train_raw <- read.csv(train_csv_path, header=TRUE)
    train_clean <- train_raw[train_raw$Sales!=0,]
    answer_raw <- read.csv("answer_result.csv", header=TRUE)
    all_stores <- unique(answer_raw$Store)
    # all_stores <- c(1,3,7)
    for(store_id in all_stores){
        train_by_store <- train_clean[train_clean$Store==store_id,]
        answer_by_store <- answer_raw[answer_raw$Store==store_id,]
        cat("store id: ")
        print(store_id)
        train_mean = summary(train_by_store$Sales)[4]
        answer_mean = summary(answer_by_store$Sales)[4]
        diff = round(abs(answer_mean - train_mean)/train_mean * 100,2)
        cat("train mean: ")
        cat(train_mean)
        cat("\tanswer mean: \t")
        cat(answer_mean)
        cat("\tdiff: ")
        cat(diff)
        if(diff>=5){
            cat("\t NOTICE")
        }
        cat("\n")
    }
}

match_main <- function(){
    test_csv_path <- 'data/test.csv'
    test_raw <- read.csv(test_csv_path, header=TRUE)
    test_raw$Sales<-0

    answer_raw <- read.csv("answer_result.csv", header=TRUE)

    # test_1 <- test_raw[test_raw$Store==1,]
    # test_1 <- test_raw[test_raw$Store==1,c('Id', "Store", "Date", "Open","Sales")]
    #
    # answer_1 <- answer_raw[answer_raw$Store==1,c('Id', "Store", "Date", "Open","Sales")]
    # source <- answer_1
    # target <- test_1
    source <- answer_raw
    target <- test_raw
    key_column <- 'Id'
    value_column <- 'Sales'
    submit_result <- match_data(source, target, key_column, value_column)
    write.table(submit_result[,c('Id','Sales')], file='submit_result.csv', row.names=FALSE,sep=',')
}

match_data <- function(source, target, key_column, value_column){
    for(cur_key in unique(source[,key_column])){
        target[target[,key_column]==cur_key,value_column] <- source[
                source[,key_column]==cur_key,value_column]
    }
    target
}

get_args <- function(){
    suppressPackageStartupMessages(require(optparse)) # don't say "Loading required package: optparse"
    # manual: http://cran.r-project.org/web/packages/optparse/optparse.pdf
    # vignette: http://www.icesi.edu.co/CRAN/web/packages/optparse/vignettes/optparse.pdf

    option_list = list(
      make_option(c("-t", "--train_csv_path"), action="store",
            default="data/train.csv", type='character',
            help="train set csv file path, data/train.csv or data/train_20.csv"),
      make_option(c("-e", "--export_csv_path"), action="store",
            default='submit_result.csv', type='character',
            help="test result csv file path"),
      make_option(c("-b", "--best_choices_csv_path"), action="store",
            default="best_choices.csv", type='character',
            help="best choices csv file path"),
      make_option(c("--from"), action="store",
            default=1, type='integer',
            help="from which store id"),
      make_option(c("--to"), action="store",
            default=9999, type='integer',
            help="to which store id")
    )
    args = parse_args(OptionParser(option_list=option_list))
    cat("train_csv_path: ")
    cat(args$train_csv_path)
    cat("\n")
    cat("export_csv_path: ")
    cat(args$export_csv_path)
    cat("\n")
    cat("best_choices_csv_path: ")
    cat(args$best_choices_csv_path)
    cat("\n")
    cat("from: ")
    cat(args$from)
    cat("\n")
    cat("to: ")
    cat(args$to)
    cat("\n")
    args
}

args <- get_args()
# Rscript answer.R -t data/train_20.csv -e submit_result.csv --from 80 --to 100
# Rscript answer.R -b best_choices11.csv -e submit_result11.csv
# nohup Rscript answer.R -b result_3/best_choices.csv >log_answer.log 2>&1 &
# nohup Rscript answer.R -b result_all/best_choices164.csv -e submit_result164.csv >logs/a164.log 2>&1 &
main(args$train_csv_path, args$export_csv_path, args$best_choices_csv_path,
        args$from, args$to)

        # train_csv_path<- "data/train_20.csv"
        # export_csv_path<- "result_1.csv"
        # from_store_id<- 80
        # to_store_id<- 100
