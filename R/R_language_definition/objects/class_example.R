xpos <- function(x, ...)
    UseMethod("xpos")
xpos.xypoint <- function(x) x$x
xpos.rthetapoint <- function(x) x$r * cos(x$theta)    

x <- 1
attr(x, "class") <- "foo"
x

# Or in one line
x <- structure(1, class = "foo")
x

# more clear
class(x) <- "foo"
class(x)

class(x) <- c("A", "B")
class(x)

letters
x <- structure(1, class = letters)
bar <- function(x) UseMethod("bar", x)
bar.z <- function(x) "z"
bar.default <- function(x) "default"
bar(x)
bar(structure(1, class = "mm"))

## find all methods
methods(bar)
# methods(print)

baz <- function(x) UseMethod("baz", x)
baz.A <- function(x) "A"
baz.B <- function(x) "B"

ab <- structure(1, class = c("A", "B"))
ba <- structure(1, class = c("B", "A"))
baz(ab)
baz(ba)

baz.C <- function(x) c("C", NextMethod())
ca <- structure(1, class = c("C", "A"))
cb <- structure(1, class = c("C", "B"))
baz(ca)
baz(cb)

# Turn object into class A - doesn't work!
baz.D <- function(x) {
  class(x) <- "A"
  c('D',NextMethod())
}
da <- structure(1, class = c("D", "A"))
db <- structure(1, class = c("D", "B"))
baz(da)
baz(db)