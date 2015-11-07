## apply for array, including matrix
## MARGIN: a vector giving the subscripts which the function will be
# applied over.  E.g., for a matrix ‘1’ indicates rows, ‘2’
# indicates columns, ‘c(1, 2)’
y <- matrix (rnorm (100), 10, 5)
y
apply(y, 1, mean)
apply(y, 2, mean)


## simple apply
c1 <- sapply(1:5, toString)
c1

## list apply
lapply(as.list(1:5), toString)


## tapply, for vector, acording indexs
n <- 17; fac <- factor(rep(1:3, length = n), levels = 1:5)
table(fac)
tapply(1:n, fac, sum)
tapply(1:n, fac, sum, simplify = FALSE)
tapply(1:n, fac, range)
tapply(1:n, fac, quantile)