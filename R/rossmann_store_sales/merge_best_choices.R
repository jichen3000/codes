main <- function(best_choices_paths, merge_csv_path, from_store_id, to_store_id){
    # best_choices_paths <- "result_all/best_choices5.csv,"+
    #         "result_all/best_choices6.csv,result_all/best_choices9.csv"
    file_paths <- unlist(strsplit(best_choices_paths,split=','))
    best_choices_list <- lapply(file_paths, function(file_path){
        df <- read.csv(file_path, header=TRUE)
        df$formula <- as.character(df$formula)
        df$method1 <- as.character(df$method1)
        df
    })
    store_list <- lapply(best_choices_list, function(best_choices){
        best_choices$Store
    })
    common_stores <- Reduce(intersect, store_list)
    first_best <- best_choices_list[[1]]
    new_best <-  first_best[first_best$Store %in% common_stores,
        c('Store','formula','method1','mean1')]
    for(store_id in common_stores){
        print(store_id)
        means <- sapply(best_choices_list, function(best_choices){
            best_choices[best_choices$Store==store_id, "mean1"]
        })
        min_index <- which(means==min(means))[1]
        min_best <- best_choices_list[[min_index]]
        new_best[new_best$Store==store_id,'formula'] <- min_best[
                min_best$Store==store_id,'formula']
        new_best[new_best$Store==store_id,'method1'] <- min_best[
                min_best$Store==store_id,'method1']
        new_best[new_best$Store==store_id,'mean1'] <- min_best[
                min_best$Store==store_id,'mean1']
    }
    # merge_csv_path <- "best_choices11.csv"
    write.table(new_best, file=merge_csv_path, sep=",")

}

get_args <- function(){
    suppressPackageStartupMessages(require(optparse)) # don't say "Loading required package: optparse"
    # manual: http://cran.r-project.org/web/packages/optparse/optparse.pdf
    # vignette: http://www.icesi.edu.co/CRAN/web/packages/optparse/vignettes/optparse.pdf

    option_list = list(
      make_option(c("-b", "--best_choices_paths"), action="store",
            default="data/train.csv", type='character',
            help="train set csv file path, data/train.csv or data/train_20.csv"),
      make_option(c("-m", "--merge_csv_path"), action="store",
            default="test_result.csv", type='character',
            help="test result csv file path"),
      make_option(c("--from"), action="store",
            default=1, type='integer',
            help="from which store id"),
      make_option(c("--to"), action="store",
            default=9999, type='integer',
            help="to which store id")
    )
    args = parse_args(OptionParser(option_list=option_list))
    cat("best_choices_paths: ")
    cat(args$best_choices_paths)
    cat("\n")
    cat("merge_csv_path: ")
    cat(args$merge_csv_path)
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
# Rscript merge_best_choices.R -m best_choices11.csv -b "result_all/best_choices7.csv,result_all/best_choices8.csv,result_all/best_choices9.csv,result_all/best_choices10.csv"
# Rscript merge_best_choices.R -m best_choices14.csv -b "result_all/best_choices5.csv,result_all/best_choices6.csv,result_all/best_choices12.csv,result_all/best_choices13.csv"
main(args$best_choices_paths, args$merge_csv_path,
        args$from, args$to)
