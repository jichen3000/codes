x <- c(1,2,3)
y <- c(4,5,6)
# plot(x,y)

generate.data.frame <- function(init_vector, size, col_names=NULL, col_prefix=""){
    col_list <- as.list(0:(size-1))
    col_list <- lapply(col_list, function(x) sapply(init_vector, function(y) y*10**x))
    result_df <- as.data.frame(col_list)
    if(is.null(col_names)){
        col_names <- sapply(1:size, function(x) paste(col_prefix,"col",x,sep=""))
    }
    names(result_df) <- col_names
    result_df
}

x_df = generate.data.frame(1:4, 3,col_prefix="x")
y_df = generate.data.frame(3:6, 3,col_prefix="y")
x_df
y_df
plot(x_df, y_df, xcol1 ~ ycol1)