x <- c(40,2,83,28,58)
f <- factor(c("A","C","C","B","C"))

"   catalog"
groups <- split(x, f)
groups
unstack(data.frame(x, f))

