x <- c(40,2,83,28,58)
y <- sapply(x, function(i){i+10})

my_list <- list(x,y)
my_list

"return vector"
sapply(my_list, mean)

"return matrix"
sapply(my_list, range)

"return list"
lapply(my_list, mean)

"return list"
lapply(my_list, range)


my_matrix <- cbind(x,y)
"my matrix"
my_matrix
mode(my_matrix)
class(my_matrix)
class(x)

"apply to every element"
sapply(my_matrix, mean)

"apply to every row"
apply(my_matrix, 1, mean)

rownames(my_matrix)<- paste("row", 1:5, sep="_")

"margin for a matrix '1' indicates rows, '2' indicates columns, 'c(1, 2)'"
apply(my_matrix, 1, mean)

f <- factor(c("A","C","C","B","C"))

"   groups"
groups <- split(x, f)
groups

"apply for group"
tapply(x, f, mean)

"by by"
by(CO2, CO2$Type, summary)

"apply to many vectors"
mapply(min, x, y)

