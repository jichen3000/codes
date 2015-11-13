main <- function(file_path){
    clear_file(file_path)
    append_file<-get_append_file_function(file_path)
    append_file("store_id","method","mean")
    # the_file <- file(file_path)
    # cat(c("store_id","method","mean"), file=file_path,sep=",")
    append_file(1,"svm","111")
    # close(the_file)
    # print(getwd())
}

clear_file <- function(file_path){
    # clear file
    cat(c(""), file=file_path)
}

get_append_file_function <- function(file_path){
    function(...) {
        write.table(t(matrix(c(...))), file=file_path,
                row.names=FALSE, append=TRUE, col.names=FALSE, sep=",")
    }
}

get_main_script_path <- function(){
    the_args <- commandArgs()
    path_str <- the_args[grep("--file=",the_args)]
    file_path <- substr(path_str, nchar('--file=')+1, 1000)
    dirname(file_path)
}

if (is.null(sys.frames())){
    cur_dir <- get_main_script_path()
    file_path <- file.path(cur_dir, "result.csv")

    main(file_path)
    train_raw <- read.csv(file_path, header=TRUE)
    print(class(train_raw))
    print(str(train_raw))
    # print(commandArgs())
    # print(Sys.getenv())
    # print(ls(.GlobalEnv))
    print("done")
}
