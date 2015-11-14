main <- function(train_csv_path, export_csv_path, best_choices_csv_path,from_store_id, to_store_id){
    source("evaluate_helper.R")
    # best_choices_csv_path <- "best_choices.csv"
    best_choices <- read.csv(best_choices_csv_path, header=TRUE)
    best_choices$Store <- as.integer(rownames(best_choices))
    # train_csv_path <- 'data/train_20.csv'
    train_raw <- read.csv(train_csv_path, header=TRUE)

    train_clean <- train_raw[train_raw$Open==1,]

    # 54 rows, cause log_regression wrong
    train_clean <- train_clean[train_clean$Sales!=0,]

    # from_store_id <- 80
    # to_store_id <- 150
    train_clean <- train_clean[train_clean$Store>=from_store_id,]
    train_clean <- train_clean[train_clean$Store<=to_store_id,]

    # train_clean$Date <- as.Date(train_clean$Date)
    #
    # all_set = split_by_column(train_clean, 'Date', 50)
    # train_set = all_set$train
    # test_set = all_set$test

    test_csv_path <- 'data/test.csv'
    test_raw <- read.csv(test_csv_path, header=TRUE)
    test_raw$Sales<-NA

    test_clean <- test_raw[test_raw$Open==1,]
    test_clean <- test_clean[test_clean$Store>=from_store_id,]
    test_clean <- test_clean[test_clean$Store<=to_store_id,]
    test_clean <- test_clean[!is.na(test_clean$Store),]

    # file_dir <- "."
    # file_path <- file.path(file_dir, export_csv_path)
    # clear_file(file_path)
    # append_file<-get_append_file_function(file_path)
    # append_file("store_id","method","mean")



    # formula = Sales~DayOfWeek+Promo
    train_set <- train_clean
    test_set <- test_clean
    test_result <- perdict_all(train_set, test_set, best_choices)
    test_result <- test_result[!is.na(test_result$Sales),]
    write.table(test_result, file=export_csv_path, sep=",")

}

get_args <- function(){
    suppressPackageStartupMessages(require(optparse)) # don't say "Loading required package: optparse"
    # manual: http://cran.r-project.org/web/packages/optparse/optparse.pdf
    # vignette: http://www.icesi.edu.co/CRAN/web/packages/optparse/vignettes/optparse.pdf

    option_list = list(
      make_option(c("-c", "--train_csv_path"), action="store",
            default="data/train.csv", type='character',
            help="train set csv file path, data/train.csv or data/train_20.csv"),
      make_option(c("-e", "--export_csv_path"), action="store",
            default="test_result.csv", type='character',
            help="test result csv file path"),
      make_option(c("-b", "--best_choices_csv_path"), action="store",
            default="best_choices.csv", type='character',
            help="best choices csv file path"),
      make_option(c("-f", "--from_store_id"), action="store",
            default=1, type='integer',
            help="from which store id"),
      make_option(c("-t", "--to_store_id"), action="store",
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
    cat("from_store_id: ")
    cat(args$from_store_id)
    cat("\n")
    cat("to_store_id: ")
    cat(args$to_store_id)
    cat("\n")
    args
}

args <- get_args()
# RScript choose_methods.R -c data/train_20.csv -e result_1.csv -f 80 -t 100
main(args$train_csv_path, args$export_csv_path, args$best_choices_csv_path,
        args$from_store_id, args$to_store_id)

        # train_csv_path<- "data/train_20.csv"
        # export_csv_path<- "result_1.csv"
        # from_store_id<- 80
        # to_store_id<- 100
