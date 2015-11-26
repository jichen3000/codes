main <- function(train_csv_path, best_choices_csv_path){
    source("evaluate_helper.R")
    # best_choices_csv_path <- "best_choices.csv"
    best_choices <- read.csv(best_choices_csv_path, header=TRUE)

    train_raw <- read.csv(train_csv_path, header=TRUE)
    # train_raw <- read.csv('data/train.csv', header=TRUE)
    # train_raw <- read.csv('data/train_20.csv', header=TRUE)
    # train_raw <- read.csv('data/high_score_train.csv', header=TRUE)
    train_clean <- train_raw[train_raw$Open==1,]

    # 54 rows, cause log_regression wrong
    # train_clean <- train_clean[train_clean$Sales!=0,]

    # train_clean <- train_clean[train_clean$Store>=from_store_id,]
    # train_clean <- train_clean[train_clean$Store<=to_store_id,]
    # train_clean <- train_clean[train_clean$Store==32,]

    # train_clean$Date <- as.Date(train_clean$Date)
    # train_clean$Month <- as.integer(format(train_clean$Date, "%m"))
    # train_clean$Week <- as.integer(format(train_clean$Date, "%U"))
    # train_clean$DateInt <- as.integer(train_clean$Date)
    # train_clean$Year <- as.integer(format(train_clean$Date, "%Y"))

    train_clean <- add_columns(train_clean)

    all_set = split_by_column(train_clean, 'Date', 50)
    train_set = all_set$train
    test_set = all_set$test
    test_set$actual = test_set$Sales

    test_result <- predict_all(train_set, test_set, best_choices)
    # test_result <- test_result[!is.na(test_result$Sales),]
    # write.table(test_result, file=export_csv_path, sep=",")
    cat("score: ")
    cat(cal_score(test_result$actual, test_result$Sales))
    cat("\n")
}

get_args <- function(){
    suppressPackageStartupMessages(require(optparse)) # don't say "Loading required package: optparse"
    # manual: http://cran.r-project.org/web/packages/optparse/optparse.pdf
    # vignette: http://www.icesi.edu.co/CRAN/web/packages/optparse/vignettes/optparse.pdf

    option_list = list(
      make_option(c("-t", "--train_csv_path"), action="store",
            default="data/train.csv", type='character',
            help="train set csv file path, data/train.csv or data/train_20.csv"),
      make_option(c("-b", "--best_choices_csv_path"), action="store",
            default="best_choices.csv", type='character',
            help="best choices csv file path")
    )
    args = parse_args(OptionParser(option_list=option_list))
    cat("train_csv_path: ")
    cat(args$train_csv_path)
    cat("\n")
    cat("best_choices_csv_path: ")
    cat(args$best_choices_csv_path)
    cat("\n")
    args
}

args <- get_args()
# Rscript mimic_score.R -b result_5_14/best_choices14.csv
# nohup Rscript mimic_score.R -b result_5_14/best_choices14.csv >logs/score14.log 2>&1 &
main(args$train_csv_path, args$best_choices_csv_path)
