e1 <- expression(a+1)
typeof(e1)
mode(e1)
storage.mode(e1)
a <- 10
eval(e1)

c1 <- quote(x + y)
typeof(c1)
mode(c1)
storage.mode(c1)

s1 <- as.list(c1)
typeof(s1[[1]])
mode(s1[[1]])
storage.mode(s1[[1]])

typeof(NULL)
mode(NULL)
storage.mode(NULL)
is.null(NULL)

typeof(NA)
mode(NA)
storage.mode(NA)
typeof(TRUE)
mode(TRUE)
storage.mode(TRUE)

typeof(NaN)
mode(NaN)
storage.mode(NaN)

x <- c(1:3)
x
y <- as.vector(x, "any")
mode(y)