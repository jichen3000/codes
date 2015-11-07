"vector"
a <- c(1, 2, 5, 3, 6, -2, 4)
a[3]
a[c(3,4)]
a[2:6]
a
a[1]

"matrix example"
y <- matrix(1:20, nrow=5, ncol=4)
y
y[3,4]
y[3,]
y[1:2]
y[3,c(3,4)]
y[3]
y[8]

cells <- c(1,26,24,68)
rnames <- c("R1", "R2")
cnames <- c("C1", "C2")
my_matrix <- matrix(cells, nrow=2,
        ncol=2, byrow=TRUE,
        dimnames=list(rnames, cnames))
my_matrix

"array example"
dim1 <- c("A1", "A2")
dim2 <- c("B1", "B2", "B3")
dim3 <- c("C1", "C2", "C3", "C4")
z <- array(1:24, c(2, 3, 4), dimnames=list(dim1, dim2, dim3))
z


"factor"
status <- c("Poor", "Improved", "Excellent", "Poor")
status
factor_status <- factor(status, ordered=TRUE)
factor_status
leveled_status <- factor(status, order=TRUE,
                 levels=c("Poor", "Improved", "Excellent"))
leveled_status


