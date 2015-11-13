mydates <- as.Date(c("2007-06-22", "2004-02-13"))
mydates
myformat <- "%m/%d/%Y"
strDates <- c("01/05/1965", "08/16/1975")
as.Date(strDates, myformat)

today <- Sys.Date()
date()
format(today, format="%B %d %Y")

colin   <- as.Date("1978-06-02")
difftime(today, colin, units="days")

as.character(colin)
as.integer(colin)

days <- as.numeric(strftime(today, format = "%j"))

now <- Sys.time()
format(now,"%Y-%m-%d %H:%M:%S")
