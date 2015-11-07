# run in cli
foo <- function(x) { print(1); bar(2) }
bar <- function(x) { x + a.variable.which.does.not.exist }
## Not run: 
foo(2) # gives a strange error
traceback()
.Traceback