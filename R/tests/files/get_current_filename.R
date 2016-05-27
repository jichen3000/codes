get_current_filename <- function(){
    initial_options <- commandArgs(trailingOnly = FALSE)
    file_arg_name <- "--file="
    sub(file_arg_name, "", 
        initial_options[grep(file_arg_name, initial_options)])
}
