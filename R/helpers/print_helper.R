p <- function(variable){
    cat(substitute(variable))
    cat(" : ")
    cat(variable)
    cat("\n")
}

pp <- function(variable){
    # cat(" ")
    cat(substitute(variable))
    cat(": \n")
    print(variable)
}

if (is.null(sys.frames())){
    x <- 1:100
    p(x)
    pp(x)
    y <- 1:5
    pp(y)
    pp(1:5)
}
