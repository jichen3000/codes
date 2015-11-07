data(iris)
# print(iris)

filename <- 'myData.RData'
# binary file
save(iris, file=filename)

# will load to current session, iris_read is only string
iris_read <- load(filename)
print(iris_read)

test.data <- read.table(header = TRUE, 
        text="a b\n1 2\n3 4\n")
print(test.data)


test.data <- read.table(text = " 
1 2
3 4",
col.names=c("a","b"),
row.names = c("first","second"))
print(test.data)

write.csv(test.data, file = "test.csv")
csv.data = read.csv("test.csv", header = TRUE, row.names=1)
head(csv.data)
colnames(csv.data)

# install.packages("WriteXLS")
# library("WriteXLS")
# WriteXLS("iris", ExcelFileName="iris.xls")

flower.type = data.frame(Species = "setosa", Flower = "iris")
merge(flower.type, iris[1:3,], by ="Species")

t.test(iris$Petal.Width[iris$Species=="setosa"],
       iris$Petal.Width[iris$Species=="versicolor"])

iris.data = read.csv(url("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"), header = FALSE,  col.names =
   c("Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width",
   "Species"))

data_link <- "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
data_col_names <- c("mpg","cylinders","displacement","horsepower","weight","acceleration","model","origin","car")
cars.data = read.csv(url(data_link), sep="", header = FALSE,  col.names = data_col_names)





