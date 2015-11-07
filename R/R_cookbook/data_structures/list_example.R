lst <- list(mid=0.5, right=0.841, far.right=0.977)
lst

names(lst)
for (nm in names(lst)) cat("The", nm, "limit is", lst[[nm]], "\n")


values <- pnorm(-2:2)
names <- c("far.left", "left", "mid", "right", "far.right")
lst2 <- list()
lst2[names] <- values
lst2

# remove
lst2$far.left <- NULL

cat("lst2 : ")
lapply(lst2, abs)>0
lst2[lapply(lst2, abs)>0]

# to vector
mean(unlist(lst2))

lst2

# removing null
lst3 <- list(mid=NULL, right=0.841, far.right=0.977)
lst3
lst3[sapply(lst3, is.null)] <- NULL
cat("lst3 : ")

# removing by condition
lst[lapply(lst,abs) < 1] <- NULL
lst3

"list"
g <- "My First List"
h <- c(25, 26, 18, 39)
j <- matrix(1:10, nrow=5)
k <- c("one", "two", "three")
mylist <- list(title=g, ages=h, j, k)
mylist
mylist[[2]]
mylist[["ages"]]

y <- 1