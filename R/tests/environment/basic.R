e <- new.env()
e$a <- FALSE
e$b <- "a"
e$c <- 2.3
e$d <- 1:3
e$.a <- 1
print(e)
str(e)
e$a < e$d
e$d

ls(e)
parent.env(e)
environmentName(e)

search()
as.environment("package:base")

ls(e, all.names = TRUE)
ls.str(e)

rm("a", envir = e)
ls(e)

x <- 10
exists("x", envir = e)
#> [1] TRUE
exists("x", envir = e, inherits = FALSE)
#> [1] FALSE

identical(globalenv(), environment())
#> [1] TRUE
# globalenv() == environment()

library(pryr)
where("x")
where("mean")

e2 <- new.env(parent = emptyenv())