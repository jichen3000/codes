## hierarchical clustering
customer.raw= read.csv('customer.csv', header=TRUE)
head(customer.raw)
str(customer.raw)
#### normalizethecustomer
customer = scale(customer.raw[,-1])
hc = hclust(dist(customer, method="euclidean"), method="ward.D2")
hc
hc2 = hclust(dist(customer), method="single")
plot(hc2, hang = -0.01, cex = 0.7)

### cut tree
fit = cutree(hc, k = 4)
fit

table(fit)
# plot(hc)
# rect.hclust(hc, k = 4 , border="red")

## kmeans
set.seed(22)
fit = kmeans(customer, 4)
fit
barplot(t(fit$centers), beside = TRUE,xlab="cluster", ylab="value")

### Drawing a bivariate cluster plot
# install.packages("cluster")
# library(cluster)
# clusplot(customer, fit$cluster, color=TRUE, shade=TRUE)

# par(mfrow= c(1,2))
# clusplot(customer, fit$cluster, color=TRUE, shade=TRUE)
# rect(-0.7,-1.7, 2.2,-1.2, border = "orange", lwd=2)
# clusplot(customer, fit$cluster, color = TRUE, xlim = c(-0.7,2.2),
#     ylim = c(-1.7,-1.2))

## Comparing clustering methods
install.packages("fpc")
library(fpc)
single_c =  hclust(dist(customer), method="single")
hc_single = cutree(single_c, k = 4)
complete_c =  hclust(dist(customer), method="complete")
hc_complete =  cutree(complete_c, k = 4)
set.seed(22)
km = kmeans(customer, 4)
cs = cluster.stats(dist(customer), km$cluster)
cs[c("within.cluster.ss","avg.silwidth")]

# Kmeans is better in this case
sapply(list(kmeans = km$cluster, hc_single = hc_single, hc_complete =
    hc_complete), function(c) cluster.stats(dist(customer), c)
    [c("within.cluster.ss","avg.silwidth")])

### compute the silhouette information
set.seed(22)
km = kmeans(customer, 4)
library(cluster)
kms = silhouette(km$cluster,dist(customer))
summary(kms)
# plot(kms)

### find k
nk = 2:10
set.seed(22)
WSS = sapply(nk, function(k) {
        kmeans(customer, centers=k)$tot.withinss
    })
WSS
plot(nk, WSS, type="l", xlab= "number of k", ylab="within sum of
    squares")
SW = sapply(nk, function(k) {
        cluster.stats(dist(customer), kmeans(customer,
        centers=k)$cluster)$avg.silwidth
    })
SW
# plot(nk, SW, type="l", xlab="number of clusers", ylab="average
#    silhouette width")
nk[which.max(SW)]

## Density-based
install.packages("mlbench")
library(mlbench)
install.packages("fpc")
library(fpc)
set.seed(2)
p = mlbench.cassini(500)
plot(p$x)
ds = dbscan(dist(p$x),0.2, 2, countmode=NULL, method="dist")
ds
plot(ds, p$x)

y = matrix(0,nrow=3,ncol=2)
y[1,] = c(0,0)
y[2,] = c(0,-1.5)
y[3,] = c(1,1)
y
predict(ds, p$x, y)

## Model-based
install.packages("mclust")
library(mclust)
# Error in svd(shape.o, nu = 0) : infinite or missing values in 'x'
mb = Mclust(customer)
plot(mb)
summary(mb)

## dissimilarity matrix
install.packages("seriation")
library(seriation)
dissplot(dist(customer), labels=km$cluster, options=list(main="Kmeans
    Clustering With k=4"))
complete_c =  hclust(dist(customer), method="complete")
hc_complete =  cutree(complete_c, k = 4)
dissplot(dist(customer), labels=hc_complete,
    options=list(main="Hierarchical Clustering"))

## Validating clusters externally
### split the number from picture
install.packages("png")
library(png)
img2 = readPNG("handwriting.png", TRUE)
img3 = img2[,nrow(img2):1]
b = cbind(as.integer(which(img3 < -1) %% 28), which(img3 < -1) / 28)
plot(b, xlim=c(1, 28), ylim=c(1,28))

set.seed(18)
fit = kmeans(b, 2)
plot(b, col=fit$cluster)
plot(b, col=fit$cluster,  xlim=c(1,28), ylim=c(1,28))

ds = dbscan(b, 2)
ds
plot(ds, b,  xlim=c(1,28), ylim=c(1,28))

