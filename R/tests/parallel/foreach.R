library("foreach")

row.count <- 2
col.count <- 3
all.count <- row.count*col.count

e.data <- matrix(seq(1, all.count), nrow = row.count, ncol=col.count)
e.data

new.data <- foreach(i=1:row.count, .combine=rbind) %do% {
    e.data[i,] + 1
}
new.data
