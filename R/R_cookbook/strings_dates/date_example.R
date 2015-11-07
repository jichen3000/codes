now <- Sys.Date()
mode(now)
class(now)

"as.Date"
as.Date("2010-12-31")
as.Date("12/31/2010", format="%m/%d/%Y")

"to str"
format(Sys.Date())
as.character(Sys.Date())
format(Sys.Date(), format="%m/%d/%Y")

"help strftime"
# help(strftime)
# %b Abbreviated month name (“Jan”)
# %B Full month name (“January”)
# %d Day as a two-digit number
# %m Month as a two-digit number
# %y Year without century (00–99
# %Y Year with century

"construct date"
ISOdate(2012,2,29)
as.Date(ISOdate(2012,2,29))

"int"
d <- as.Date("2010-03-15")
as.integer(d)
julian(d)
as.integer(as.Date("1970-01-01"))
as.integer(as.Date("1969-12-21"))

"get year, day"
d <- as.Date("2010-03-15") 
p <- as.POSIXlt(d)
p$mday
p$mon
p$year + 1900

s <- as.Date("2012-01-01") 
e <- as.Date("2012-02-01") 
date_vector <- seq(from=s, to=e, by=1)
date_vector
mode(date_vector)
class(date_vector)
is.vector(date_vector)
seq(from=s, by=1, length.out=7)
