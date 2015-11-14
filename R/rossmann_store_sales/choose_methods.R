main <- function(train_csv_path, export_csv_path, from_store_id, to_store_id){
    source("evaluate_helper.R")
    train_raw <- read.csv(train_csv_path, header=TRUE)
    # train_raw <- read.csv('data/train.csv', header=TRUE)
    # train_raw <- read.csv('data/train_20.csv', header=TRUE)
    train_clean <- train_raw[train_raw$Open==1,]

    # 54 rows, cause log_regression wrong
    train_clean <- train_clean[train_clean$Sales!=0,]

    train_clean <- train_clean[train_clean$Store>=from_store_id,]
    train_clean <- train_clean[train_clean$Store<=to_store_id,]

    train_clean$Date <- as.Date(train_clean$Date)

    all_set = split_by_column(train_clean, 'Date', 50)
    train_set = all_set$train
    test_set = all_set$test

    file_dir <- "."
    file_path <- file.path(file_dir, export_csv_path)
    clear_file(file_path)
    append_file<-get_append_file_function(file_path)
    append_file("store_id","method","mean")

    formula = Sales~DayOfWeek+Promo

    method_names <- c("simple_regression","rubost_regression",
            "log_regression","glm_regression","gam_regression",
            "bagging","boosting","boosting_cv","randomforest","svm")
    # perdict_matrix <-evaluate_all_by_store(train_set,test_set,method_names)
    perdict_matrix <-evaluate_to_file(train_set,test_set,method_names,append_file)
    best_choices <- organize_best_chcoices_by_store(perdict_matrix,test_set,method_names)
    range_differences = get_range_difference(train_set)
    best_choices$range <- range_differences
    best_choices$mean2range <- round(best_choices[2] / range_differences, 3)[,1]
    best_choices <- subset(best_choices,select=c(1:2, 13:14, 3:12))

    write.table(best_choices, file="best_choices.csv", sep=",")

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
      make_option(c("-c", "--train_csv_path"), action="store",
            default="data/train.csv", type='character',
            help="train set csv file path, data/train.csv or data/train_20.csv"),
      make_option(c("-e", "--export_csv_path"), action="store",
            default=gen_result_csv_name(), type='character',
            help="method mean csv file path"),
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
main(args$train_csv_path, args$export_csv_path,
        args$from_store_id, args$to_store_id)

        train_csv_path<- "data/train_20.csv"
        export_csv_path<- "result_1.csv"
        from_store_id<- 80
        to_store_id<- 100
