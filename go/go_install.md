## set GOROOT
mkdir gopkg

export GOROOT=/usr/local/go
GOPATH=/Users/colin/gopkg
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin

## repl
go get -u github.com/motemen/gore