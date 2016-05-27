library(pryr)

df <- data.frame(x = 1:10, y = letters[1:10])
otype(df)    # A data frame is an S3 class
#> [1] "S3"
otype(df$x)  # A numeric vector isn't
#> [1] "base"
otype(df$y)  # A factor is
#> [1] "S3
is.object(df) & !isS4(df)

mean
#> function (x, ...) 
#> UseMethod("mean")
#> <bytecode: 0x21b6ea8>
#> <environment: namespace:base>
ftype(mean)
#> [1] "s3"      "generic"

sum
# ftype(sum)
# report error


ftype(t.data.frame) # data frame method for t()
#> [1] "s3"     "method"
ftype(t.test)       # generic function for t tests
#> [1] "s3"      "generic"

methods("mean")
#> [1] mean.Date     mean.default  mean.difftime mean.POSIXct  mean.POSIXlt 
#> see '?methods' for accessing help and source code
methods("t.test")
#> [1] t.test.default* t.test.formula*
#> see '?methods' for accessing help and source code

# 
# getS3method("mean")

# You can also list all generics that have a method for a given class
methods(class = "ts")
#>  [1] aggregate     as.data.frame cbind         coerce        cycle        
#>  [6] diffinv       diff          initialize    kernapply     lines        
#> [11] Math2         Math          monthplot     na.omit       Ops          
#> [16] plot          print         show          slotsFromS3   time         
#> [21] [<-           [             t             window<-      window       
#> see '?methods' for accessing help and source code


# Create and assign class in one step
foo <- structure(list(), class = "foo")

# Create, then set class
foo <- list()
is.object(foo) # false
class(foo) <- "foo"
is.object(foo) # true

class(foo)
#> [1] "foo"
inherits(foo, "foo")
#> [1] TRUE


f <- function(x) UseMethod("f")
f.a <- function(x) "Class a"
f.default <- function(x) "Unknown class"

f(structure(list(), class = "a"))
#> [1] "Class a"
# No method for b class, so uses method for a class
f(structure(list(), class = c("b", "a")))
#> [1] "Class a"
# No method for c class, so falls back to default
f(structure(list(), class = "c"))
#> [1] "Unknown class"

t
t.test
test1 <- structure(list(), class = "test")
# t(test1)


y <- 1
g <- function(x) {
  y <- 2
  UseMethod("g")
}
g.numeric <- function(x) y
g(10)

h <- function(x, index) {
  x <- 10
  UseMethod("h")
}
h.character <- function(x, index) paste("char", x)
h.numeric <- function(x, index) paste("num", x)

h("a", 1)

# UseMethod determine the type at the point pass the argument
# UseMethod use the environment in the generic method.

## internal generic
f <- function() 1
g <- function() 2
class(g) <- "function"

class(f) # function, but it is internal
class(g)

length.function <- function(x) "function"
length(f) # invoke internal
length(g)