"create data.frame"
patientID <- c(1, 2, 3, 4)
age <- c(25, 34, 28, 52)
diabetes <- c("Type1", "Type2", "Type1", "Type1")
status <- c("Poor", "Improved", "Excellent", "Poor")
patientdata <- data.frame(patientID, age, diabetes, status)
patientdata

"get some columns"
patientdata[1:2]
patientdata[c("diabetes", "status")]
"returns one column, not a data frame"
patientdata$age
patientdata[["age"]]

"to table"
table(patientdata$diabetes, patientdata$status)

"use with or attach"
attach(patientdata)
diabetes
detach(patientdata)

with(patientdata, {
   stats <- summary(age)
   stats
   keepstats <<- summary(age)
  })
# cannot see stats outside of with
# keepstats

"point a row name"
patientdata <- data.frame(patientID, age, diabetes, status,
          row.names=age)
patientdata  

"str data.frame"
str(patientdata)

"subset"
subset(patientdata, select=age)
subset(patientdata, select=c(patientID, age))
subset(patientdata, subset=(age > 30))
subset(patientdata, select=c(patientID, age), subset=(age > 30))



"edit: will popup a window"
# tmp <- edit(patientdata)
"edit: will popup a window, cannot undo"
# fix(patientdata) 

"combine by columns"
cbind(patientdata,patientdata)
"combine by rows"
rbind(patientdata,patientdata)

"change col names"
colnames(patientdata) <- c("1", "2","3")
patientdata

""
data.frame(matrix(NA, nrow = 2, ncol = 3))
e1 <- data.frame(matrix(NA, nrow = 0, ncol = 3))