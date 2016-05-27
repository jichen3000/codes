f2 <- function(x,y){
    s <- paste0(x,":",y)
    cat(s)
    cat("\n")
    s
}

ss <- 5:8
mapply(f2, ss, 1:length(ss))

# sapply(ss, f2)

mylist <- list(a = TRUE, foo = LETTERS[1:3], baz = 1:5)
n <- names(mylist)
mynewlist <- lapply(setNames(n, n), function(nameindex) {mylist[[nameindex]]})
