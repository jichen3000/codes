modify <- function(x) {
  x$a <- 2
  invisible()
}

x_l <- list()
x_l$a <- 1
modify(x_l)
x_l$a

x_e <- new.env()
x_e$a <- 1
modify(x_e)
x_e$a
#> [1] 2

x <- 1
e1 <- new.env()
get("x", envir = e1)
#> [1] 1

e2 <- new.env(parent = emptyenv())
get("x", envir = e2)
#> Error in get("x", envir = e2): object 'x' not found