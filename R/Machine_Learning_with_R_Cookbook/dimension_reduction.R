## feature selecting
# need java 6
install.packages("FSelector")
library(FSelector)

weights = random.forest.importance(churn~., trainset, importance.type
    = 1)
print(weights)
subset = cutoff.k(weights, 5)
f = as.simple.formula(subset, "Class")
print(f)
evaluator = function(subset) { 
    k=5
    set.seed(2)
    ind = sample(5, nrow(trainset), replace = TRUE)
    results = sapply(1:k, function(i){
        train = trainset[ind == i, ]
        test = trainset[ind != i, ]
        tree = rpart(as.simple.formula(subset, "churn"), trainset)
        error.rate = sum(test$churn != predict(tree, test, type="class"))/ nrow(test)
        return(1 - error.rate)
    })
    return(mean(results))
}
attr.subset = hill.climbing.search(names(trainset)[!names(trainset)
    %in% "churn"], evaluator)
f = as.simple.formula(attr.subset, "churn")
print(f)

## dimension reduction with PCA
data(swiss)
swiss = swiss[,-1]
swiss.pca = prcomp(swiss,
    center = TRUE,
    scale  = TRUE)
swiss.pca
summary(swiss.pca)
predict(swiss.pca, newdata=head(swiss, 1))

## Determining the number of principal components using the scree test
screeplot(swiss.pca, type="barplot")
screeplot(swiss.pca, type="line")

## Determining the number of principal components using the Kaiser method

swiss.pca$sdev
swiss.pca$sdev ^ 2
# From the computed variance, we find both component 1 and 2 have a variance above 1.
which(swiss.pca$sdev ^ 21)
screeplot(swiss.pca, type="line")
abline(h=1, col="red", lty= 3)

plot(swiss.pca$x[,1], swiss.pca$x[,2], xlim=c(-4,4))
text(swiss.pca$x[,1], swiss.pca$x[,2], rownames(swiss.pca$x),
    cex=0.7, pos=4, col="red")
biplot(swiss.pca)

## Performing dimension reduction with MDS
swiss.dist =dist(swiss)
swiss.mds = cmdscale(swiss.dist, k=2)
plot(swiss.mds[,1], swiss.mds[,2], type = "n", main = "cmdscale
    (stats)")
text(swiss.mds[,1], swiss.mds[,2], rownames(swiss), cex = 0.9, xpd =
    TRUE)    
library(MASS)
swiss.nmmds = isoMDS(swiss.dist, k=2)
plot(swiss.nmmds$points, type = "n", main = "isoMDS (MASS)")
text(swiss.nmmds$points, rownames(swiss), cex = 0.9, xpd = TRUE)
swiss.sh = Shepard(swiss.dist, swiss.mds)
plot(swiss.sh, pch = ".")
lines(swiss.sh$x, swiss.sh$yf, type = "S") 

## Reducing dimensions with SVD
swiss.svd = svd(swiss)   
plot(swiss.svd$d^2/sum(swiss.svd$d^2), type="l", xlab=" Singular
    vector", ylab = "Variance explained")
plot(cumsum(swiss.svd$d^2/sum(swiss.svd$d^2)), type="l",
    xlab="Singular vector", ylab = "Cumulative percent of variance
    explained")
swiss.recon = swiss.svd$u[,1] %*% diag(swiss.svd$d[1], length(1),
   length(1)) %*% t(swiss.svd$v[,1])
par(mfrow=c(1,2))
image(as.matrix(swiss), main="swiss data Image")
image(swiss.recon,  main="Reconstructed Image")

### PCA can be regarded as a specific case of SVD
svd.m = svd(scale(swiss))
svd.m$v

pca.m = prcomp(swiss,scale=TRUE)
pca.m$rotation

## Compressing images with SVD
install.packages("bmp")
library(bmp)
lenna = read.bmp("lena512.bmp")
lenna = t(lenna)[,nrow(lenna):1]
image(lenna)

lenna.svd = svd(scale(lenna))
plot(lenna.svd$d^2/sum(lenna.svd$d^2), type="l", xlab=" Singular
    vector", ylab = "Variance explained")
length(lenna.svd$d)
min(which(cumsum(lenna.svd$d^2/sum(lenna.svd$d^2))>0.9))
lenna_compression = function(dim){
    u=as.matrix(lenna.svd$u[, 1:dim])
    v=as.matrix(lenna.svd$v[, 1:dim])
    d=as.matrix(diag(lenna.svd$d)[1:dim, 1:dim]) 
    image(u%*%d%*%t(v))
}
lenna_compression(18)
min(which(cumsum(lenna.svd$d^2/sum(lenna.svd$d^2))>0.99)
lenna_compression(92)

## Performing nonlinear dimension reduction with ISOMAP
install.packages("RnavGraphImageData")
install.packages("vegan")
library(RnavGraphImageData)
library(vegan)
data(digits)
sample.digit = matrix(digits[,3000],ncol = 16, byrow=FALSE)
image(t(sample.digit)[,nrow(sample.digit):1])

set.seed(2)
digit.idx = sample(1:ncol(digits),size = 600)
digit.select = digits[,digit.idx]
digits.Transpose = t(digit.select)
digit.dist = vegdist(digits.Transpose, method="euclidean")
digit.isomap = isomap(digit.dist,k = 8, ndim=6, fragmentedOK = TRUE)
plot(digit.isomap)

digit.st = spantree(digit.dist)
digit.plot = plot(digit.isomap, main="isomap k=8")
lines(digit.st, digit.plot, col="red")

## Performing nonlinear dimension reduction with Local Linear Embedding
install.packages("lle")
library(lle)
data( lle_scurve_data )
X = lle_scurve_data
results = lle( X=X , m=2, k=12,  id=TRUE)
str(results)
plot( results$Y, main="embedded data", xlab=expression(y[1]),
    ylab=expression(y[2]) )
plot_lle( results$Y, X, FALSE, col="red", inter=TRUE )



