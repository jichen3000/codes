## atomic
# is.vector not use for check vector, use is.list || is.atomic
y <- 1:10
is.vector(y) # true
attr(y, "my_attribute") <- "This is a vector"
is.vector(y) # false
is.atomic(y) # true
is.list(y) # false

# flat
c(1, c(2, c(3, 4)))
#> [1] 1 2 3 4
# the same as
c(1, 2, 3, 4)

## list
x <- list(1:3, "a", c(TRUE, FALSE, TRUE), c(2.3, 5.9))
str(x)


is.recursive(x)

x <- list(list(list(list())))
str(x)

x <- list(list(1, 2), c(3, 4))
y <- c(list(1, 2), c(3, 4))
str(x)
#> List of 2
#>  $ :List of 2
#>   ..$ : num 1
#>   ..$ : num 2
#>  $ : num [1:2] 3 4
str(y)
#> List of 4
#>  $ : num 1
#>  $ : num 2
#>  $ : num 3
#>  $ : num 4