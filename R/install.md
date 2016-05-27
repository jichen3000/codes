## setting for mirror
emacs ~/.Rprofile
\#chooseCRANmirror(ind=89)
options(repos=structure(c(CRAN="http://cran.cnr.Berkeley.edu/")))
wideScreen <- function(howWide=Sys.getenv("COLUMNS")) {
  options(width=as.integer(howWide))
}
wideScreen(180)

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

## install on linux
yum install readline-devel
yum install libXt-devel

./configure
make
make install

## 
http://www.rdocumentation.org

## centos
install.packages("rJava")
which java
ls -l /usr/bin/java
ls -l /etc/alternatives/java
export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75-2.5.4.2.el7_0.x86_64
export PATH=$PATH:$JAVA_HOME/bin
R CMD javareconf
yum install java-1.7.0-openjdk-devel