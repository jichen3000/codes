puts.some <- function(){
    print("puts some")
}

# puts.some()
print("for source")

initial.options <- commandArgs(trailingOnly = FALSE)
file.arg.name <- "--file="
script.name <- sub(file.arg.name, "", initial.options[grep(file.arg.name, initial.options)])
script.basename <- dirname(script.name)
print(script.name)


# ifmain just equal is.null(sys.frames()) 
print(is.null(sys.frames()))
if (is.null(sys.frames())){
    print("ifmain")
}