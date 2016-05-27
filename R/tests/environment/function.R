library(pryr)

## enclosing environment
environment(sd)
#> <environment: namespace:stats>

## binding environment
where("sd")
#> <environment: package:stats>

# 
execution_environment <- NA
plus <- function(x) {
    execution_environment <<- environment()
    print(identical(parent.env(execution_environment), parent.frame()))
    function(y) x + y
}
plus_one <- plus(1)
identical(parent.env(environment(plus_one)), environment(plus))
identical(environment(plus_one), execution_environment)

h <- function() {
  x <- 10
  function() {
    x
  }
}
i <- h()
x <- 20 # if use this one, call dynamic scoping.
i()