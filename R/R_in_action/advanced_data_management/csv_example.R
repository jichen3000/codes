Student <- c("John Davis", "Angela Williams", 
    "Bullwinkle Moose", "David Jones", 
    "Janice Markhammer", "Cheryl Cushing",
    "Reuven Ytzrhak", "Greg Knox", "Joel England",
    "Mary Rayburn")
Math <- c(502, 600, 412, 358, 495, 512, 410, 625, 573, 522)
Science <- c(95, 99, 80, 82, 75, 85, 80, 95, 89, 86)
English <- c(25, 22, 18, 15, 20, 28, 15, 30, 27, 18)
roster <- data.frame(Student, Math, Science, English,
    stringsAsFactors=FALSE)

roster

# write.table(roster, file="student.csv")
# write.csv(roster, file="student.csv")
# without id
write.csv(roster, file="student.csv", row.names=FALSE)

tbl <- read.csv(file="student.csv")
tbl