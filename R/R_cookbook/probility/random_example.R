"same random value"
set.seed(666)

"uniform distribution"
runif(1)
runif(10)
runif(1, min=-3, max=3)

"rnorm for the Normal distribution's random number generator"
rnorm(1)
rnorm(1, mean=100, sd=15)
"with means of -10, 0, and +10, respectively"
rnorm(3, mean=c(-10,0,+10), sd=1)

"sample, not select the same element"
sample(1:100, 5)
"could be same"
sample(1:100, 5, replace=TRUE)

"different probability"
sample(c(FALSE,TRUE), 20, replace=TRUE, prob=c(0.2,0.8))
"binary-valued"
rbinom(10, 1, 0.8)
