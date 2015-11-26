
main <- function(formula_str, train_csv_path, best_choices_csv_path, from_store_id, to_store_id){
    source("evaluate_helper.R")
    train_raw <- read.csv(train_csv_path, header=TRUE)
    # train_raw <- read.csv('data/train.csv', header=TRUE)
    # train_raw <- read.csv('data/train_20.csv', header=TRUE)
    train_clean <- train_raw[train_raw$Open==1,]

    # 54 rows, cause log_regression wrong
    # train_clean <- train_clean[train_clean$Sales!=0,]

    train_clean <- train_clean[train_clean$Store>=from_store_id,]
    train_clean <- train_clean[train_clean$Store<=to_store_id,]

    train_clean$Date <- as.Date(train_clean$Date)
    train_clean$Month <- as.integer(format(train_clean$Date, "%m"))
    train_clean$Week <- as.integer(format(train_clean$Date, "%U"))
    train_clean$DateInt <- as.integer(train_clean$Date)
    train_clean$Year <- as.integer(format(train_clean$Date, "%Y"))

    all_set = split_by_column(train_clean, 'Date', 50)
    train_set = all_set$train
    test_set = all_set$test


    # formula <- Sales~DayOfWeek
    # formula <- Sales~DayOfWeek+Promo
    # formula <- Sales ~ DayOfWeek + SchoolHoliday
    # formula_str <- "Sales ~ DayOfWeek + Promo"
    # formula_str <- "Sales ~ DayOfWeek + Promo + SchoolHoliday"
    formula <- as.formula(formula_str)

    # svm_tune
    method_names <- c("simple_regression","rubost_regression",
            "log_regression","glm_regression","gam_regression",
            "bagging","boosting","boosting_cv","randomforest","svm")
    best_choices <-gen_best_choices_to_file(train_set,test_set,method_names,formula)


    # write.table(best_choices, file="best_choices.csv", sep=",")
    # best_choices_csv_path <- "best_choices.csv"
    write.table(best_choices, file=best_choices_csv_path, sep=",")

}

gen_result_csv_name <- function(){
    now <- Sys.time()
    paste0("result_",format(now,"%Y-%m-%d_%H-%M-%S"),".csv")
}



get_args <- function(){
    suppressPackageStartupMessages(require(optparse)) # don't say "Loading required package: optparse"
    # manual: http://cran.r-project.org/web/packages/optparse/optparse.pdf
    # vignette: http://www.icesi.edu.co/CRAN/web/packages/optparse/vignettes/optparse.pdf

    option_list = list(
      make_option(c("-f", "--formula"), action="store",
            type='character',
            help="formula"),
      make_option(c("-t", "--train_csv_path"), action="store",
            default="data/train.csv", type='character',
            help="train set csv file path, data/train.csv or data/train_20.csv"),
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
    cat("formula: ")
    cat(args$formula)
    cat("\n")
    cat("train_csv_path: ")
    cat(args$train_csv_path)
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
# formula_str <- "Sales ~ DayOfWeek + Promo"
# formula_str <- "Sales ~ DayOfWeek + Promo + SchoolHoliday"
# Rscript choose_methods.R -t data/train_20.csv --from 80 --to 150 -f "Sales ~ DayOfWeek + Promo"
# nohup Rscript choose_methods.R -b best_choices7.csv -f "Sales ~ DayOfWeek + Promo" >log7.log 2>&1 &
# nohup Rscript choose_methods.R -b best_choices8.csv -f "Sales ~ DayOfWeek + Promo + SchoolHoliday" >log8.log 2>&1 &
# nohup Rscript choose_methods.R -b best_choices9.csv -f "Sales ~ DayOfWeek" >log9.log 2>&1 &
# nohup Rscript choose_methods.R -b best_choices10.csv -f "Sales ~ DayOfWeek + SchoolHoliday" >log10.log 2>&1 &
# nohup Rscript choose_methods.R -b best_choices12.csv -f "Sales ~ DayOfWeek" >log12.log 2>&1 &
# nohup Rscript choose_methods.R -b best_choices13.csv -f "Sales ~ DayOfWeek + SchoolHoliday" >log13.log 2>&1 &
main(args$formula, args$train_csv_path, args$best_choices_csv_path,
        args$from, args$to)
