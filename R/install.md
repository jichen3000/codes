## setting for mirror
emacs ~/.Rprofile
\#chooseCRANmirror(ind=89)
options(repos=structure(c(CRAN="http://cran.cnr.Berkeley.edu/")))


require(tseries)
\#bypass the warn message
suppressMessages(require(tseries))

## setting default packages
pkgs <- getOption("defaultPackages") 
pkgs <- c(pkgs, "zoo") 
options(defaultPackages = pkgs) 
rm(pkgs)

## vector or list to matrix or arrays
B <- list(1,2,3,4,5,6) 
dim(B)
dim(B) <- c(2,3) 
print(B)
mode(B) == "list"
class(B) == "matrix"
