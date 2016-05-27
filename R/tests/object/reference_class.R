library(methods)
Account <- setRefClass("Account")
a <- Account$new()
str(a)

Account <- setRefClass("Account",
  fields = list(balance = "numeric"))

a <- Account$new(balance = 100)
a$balance
#> [1] 100
a$balance <- 200
a$balance
#> [1] 200

## mutable
b <- a
b$balance
#> [1] 200
a$balance <- 0
b$balance

## copy
c <- a$copy()
c$balance
#> [1] 0
a$balance <- 100
c$balance
#> [1] 0

## unmutable
al <- list(1,2,3)
al
bl <- al
bl[[2]] <- 1
bl

Account <- setRefClass("Account",
  fields = list(balance = "numeric"),
  methods = list(
    withdraw = function(x) {
      balance <<- balance - x
    },
    deposit = function(x) {
      balance <<- balance + x
    }
  )
)
a$deposit(100)
# a$methods


NoOverdraft <- setRefClass("NoOverdraft",
  contains = "Account",
  methods = list(
    withdraw = function(x) {
      if (balance < x) stop("Not enough money")
      balance <<- balance - x
    }
  )
)
accountJohn <- NoOverdraft$new(balance = 100)
accountJohn$deposit(50)
accountJohn$balance
#> [1] 150
# accountJohn$withdraw(200)
#> Error in accountJohn$withdraw(200): Not enough money


isS4(accountJohn) && is(accountJohn, "refClass")
library(pryr)
otype(accountJohn)