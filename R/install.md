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

## R_X11.so
In addition: Warning message:
In doTryCatch(return(expr), name, parentenv, handler) :
  unable to load shared object '/Library/Frameworks/R.framework/Resources/modules//R_X11.so':
  dlopen(/Library/Frameworks/R.framework/Resources/modules//R_X11.so, 6): Library not loaded: /opt/X11/lib/libSM.6.dylib
  Referenced from: /Library/Frameworks/R.framework/Resources/modules//R_X11.so
  Reason: image not found

install X11 for mac, XQuartz
then 
locate libSM.6.dylib
sudo ln -s /opt/X11 /usr/X11  
