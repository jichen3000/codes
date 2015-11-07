e1 <- quote(2 + 3)
mode(e1)
class(e1)
typeof(e1)

quote("+"(2, 3))
e1[[1]]
e1[[2]]
e1[[3]]

mode(e1[[1]])
class(e1[[1]])
typeof(e1[[1]])

e1[[1]] <- as.name("*")
e1

es <- substitute(e1)
mode(es)
es <- substitute(x+x)
mode(es)

x <- 10.5
e4 <- call("round", x)
mode(e4)
e4