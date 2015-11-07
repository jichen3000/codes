sqr = seq(1, 100, by=2)

sqr.squared = NULL
for (n in 1 : length(sqr)){
    sqr.squared[n] = sqr[n]^2
}
