library("foreach")
options(error=function()traceback(2))

do_some <- function(index){
    # print(paste0("index:",index))
    c(1:6) + index*10
}

foreach_with_parallel <- function(){
    suppressPackageStartupMessages(require("parallel"))
    suppressPackageStartupMessages(require("doParallel"))

    cluster <- makeCluster(detectCores() - 1)
    registerDoParallel(cluster, cores = detectCores() - 1)

    count = 3
    data = foreach(i = 1:count, .export = c("do_some"), .combine=c) %dopar% {
        # try({
            # print(ls(environment()))
            do_some(i)
            c(1:6) + i*10
        # })
    }
    stopCluster(cluster)
    data
}

foreach_simple <- function(){
    x <- foreach(i=1:3, b=rep(10, 3)) %do% (i+b)
    invisible(x)
}

if (is.null(sys.frames())){
    suppressPackageStartupMessages(require(minitest))
    only_test("use function")

    test("simple", {
        x <- foreach(i=1:3, b=rep(10, 3)) %do% (i+b)
        x %equal% list(11, 12, 13)
    })

    test("list length is less one", {
        x <- foreach(a=1:1000, b=rep(10, 2)) %do% (a+b)
        x %equal% list(11, 12)
    })

    test(".combine", {
        x <- foreach(i=1:3, .combine='c') %do% exp(i)
        x %equal% exp(1:3)

        set.seed(2)
        x <- foreach(i=1:4, .combine='cbind') %do% rnorm(4)
        set.seed(2)
        y <- sapply(rep(4,4), rnorm)
        colnames(y) <- paste("result",1:4,sep=".")
        x %equal% y
        x %output% 
                c("       result.1    result.2   result.3   result.4",
                "[1,] -0.8969145 -0.08025176  1.9844739 -0.3926954",
                "[2,]  0.1848492  0.13242028 -0.1387870 -1.0396690",
                "[3,]  1.5878453  0.70795473  0.4176508  1.7822290",
                "[4,] -1.1303757 -0.23969802  0.9817528 -2.3110691")

        set.seed(2)
        x <- foreach(i=1:4, .combine='+') %do% rnorm(4)
        print(x) %output% 
                "[1]  0.6146123 -0.8611865  4.4956798 -2.6993900"
    })

    test("parallel", {
        suppressPackageStartupMessages(require(randomForest))
        set.seed(2)
        x <- matrix(runif(500), 100)
        y <- gl(2, 50)
        rf <- foreach(ntree=rep(250, 4), .combine=combine) %do%
            randomForest(x, y, ntree=ntree)
        print(rf) %output% c(
                "",
                "Call:",
                " randomForest(x = x, y = y, ntree = ntree) ",
                "               Type of random forest: classification",
                "                     Number of trees: 1000",
                "No. of variables tried at each split: 2",
                ""
        )

        suppressPackageStartupMessages(require("parallel"))
        suppressPackageStartupMessages(require("doParallel"))

        cluster <- makeCluster(detectCores() - 1)
        registerDoParallel(cluster, cores = detectCores() - 1)
        rf <- foreach(ntree=rep(250, 4), .combine=combine, 
                .packages='randomForest') %dopar%
            randomForest(x, y, ntree=ntree)
    
        stopCluster(cluster)
        print(rf) %output% c(
                "",
                "Call:",
                " randomForest(x = x, y = y, ntree = ntree) ",
                "               Type of random forest: classification",
                "                     Number of trees: 1000",
                "No. of variables tried at each split: 2",
                ""
        )
    })

    test("list comprehensions", {
        x <- foreach(a=irnorm(1, count=10), .combine='c') %:% when(a >= 0) %do% sqrt(a)
        print(x) %output% "[1] 0.8950148 1.4612782 1.0349242 0.9821052"
    })

    test("use function", {
        data <- foreach_with_parallel()
        print(data) %output% 
                " [1] 11 12 13 14 15 16 21 22 23 24 25 26 31 32 33 34 35 36"
    })

}