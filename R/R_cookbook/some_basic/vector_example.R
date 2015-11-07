x <- seq(from=0, to=5, by=2)
x
is.vector(x)

x <- seq(from=0, to=10, length.out=5)
x

rep(pi, times=5)



v <- c( 3, pi, 4) 
w <- c(pi, pi, pi) 
v == w
any(v==w)

v[3]
v[-3] # exclude element
v[-(1:2)]
length(v)

fib <- c(0,1,1,2,3,5,8,13,21,34)
fib[3:5]

fib %% 2 == 0
fib[fib %% 2 == 0]

years <- c(1960, 1964, 1976, 1994)
names(years) <- c("Kennedy", "Johnson", "Carter", "Clinton") 
years

years["Carter"]

years[c("Carter","Clinton")]