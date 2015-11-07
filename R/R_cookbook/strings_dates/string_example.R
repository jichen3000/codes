"length"
nchar("Everybody")

"add strings"
paste("Everybody", "loves", "stats.", sep="")

stooges <- c("Moe", "Larry", "Curly")
paste(stooges, "loves", "stats.")

"sub string"
substr("Everybody", 6, 12)
# substr("Everybody", 6)


cities <- c("New York, NY", "Los Angeles, CA", "Peoria, IL") 
substr(cities, nchar(cities)-1, nchar(cities))

"split string fixed=TRUE to unset regexp"
path <- "/home/mike/data/trials.csv"
strsplit(path, '/')

paths <-  c("/home/mike/data/trials.csv", 
            "/home/mike/data/errors.csv", 
            "/home/mike/corr/reject.doc")
strsplit(paths, '/')

"replace fixed=TRUE to unset regexp"
s <- "Curly is the smart one. Curly is funny, too." 
sub("Curly", "Moe", s)
gsub("Curly", "Moe", s)

"cat vs print"
s <- "first\rsecond\n"
nchar(s)
print(s)
cat(s)

"combination"
locations <- c("NY", "LA", "CHI", "HOU") 
treatments <- c("T1", "T2", "T3")
outer(locations, treatments, paste, sep="-")

