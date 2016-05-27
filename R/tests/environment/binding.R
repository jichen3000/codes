`a + b` <- 3
`:)` <- "smile"
`    ` <- "spaces"
ls()
#  [1] "    "   ":)"     "a + b"
`:)`
#  [1] "smile"

library(pryr)
system.time(b %<d-% {Sys.sleep(1); 1})
#>    user  system elapsed 
#>       0       0       0
system.time(b)
#>    user  system elapsed 
#>   0.000   0.000   1.001

x %<a-% runif(1)
x
#> [1] 0.1100141
x
#> [1] 0.1063044
rm(x)