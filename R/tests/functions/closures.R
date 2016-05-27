power <- function(exponent) {
  function(x) {
    x ^ exponent
  }
}

square <- power(2)
square(2)
#> [1] 4
square(4)
#> [1] 16

cube <- power(3)
cube(2)
#> [1] 8
cube(4)
#> [1] 64

# When you print a closure, you don’t see anything terribly useful:
square
#> function(x) {
#>     x ^ exponent
#>   }
#> <environment: 0x3a50680>
cube
#> function(x) {
#>     x ^ exponent
#>   }
#> <environment: 0x37f10f8>

as.list(environment(square))
#> $exponent
#> [1] 2
as.list(environment(cube))
#> $exponent
#> [1] 3

library(pryr)
unenclose(square)
#> function (x) 
#> {
#>     x^2
#> }
unenclose(cube)
#> function (x) 
#> {
#>     x^3
#> }

power <- function(exponent) {
  print(environment())
  function(x) x ^ exponent
}
zero <- power(0)
#> <environment: 0x4197fa8>
environment(zero)
#> <environment: 0x4197fa8>

# mutate status
new_counter <- function() {
  i <- 0
  function() {
    i <<- i + 1
    i
  }
}

a <- new_counter()
a()
a()

b <- new_counter()
b()
b()

new_counter1 <- function() {
  i <- 0
  function() {
    i <- i + 1
    i
  }
}

a <- new_counter1()
a()
a()

b <- new_counter1()
b()
b()
