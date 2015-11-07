## Transforming data into transactions
### list to transactions
install.packages("arules")
library(arules)
tr_list = list(c("Apple", "Bread", "Cake"),
               c("Apple", "Bread", "Milk"),
               c("Bread", "Cake", "Milk"))
names(tr_list) = paste("Tr",c(1:3), sep = "")
trans = as(tr_list, "transactions")
trans

### matrix to transactions
tr_matrix = matrix(
        c(  1,1,1,0,
            1,1,0,1,
            0,1,1,1), ncol = 4)
dimnames(tr_matrix) =  list(
        paste("Tr",c(1:3), sep = ""),
        c("Apple","Bread","Cake", "Milk") +)
trans2 =  as(tr_matrix, "transactions")
trans2

### data.frame to transactions
Tr_df = data.frame( 
    TrID = as.factor(c(1,2,1,1,2,3,2,3,2,3)),
    Item = as.factor(c("Apple", "Milk", "Cake", "Bread", 
                        "Cake", "Milk", "Apple", "Cake", 
                        "Bread", "Bread"))
    )
trans3 = as(split(Tr_df[,"Item"], Tr_df[,"TrID"]), "transactions") 
trans3

help(transactions)
help(itemMatrix)

### Displaying transactions and associations
LIST(trans)
summary(trans)
inspect(trans)

filter_trains = trans[size(trans) >=3]
inspect(filter_trains)
# image(trans)
# itemFrequencyPlot (trans)

## Mining associations with the Apriori rule
data(Groceries)
summary(Groceries)
itemFrequencyPlot(Groceries, support = 0.1, cex.names=0.8, topN=5)
rules = apriori(Groceries, parameter = list(supp = 0.001, conf = 0.5,
    target= "rules"))
summary(rules)
inspect(head(rules))
rules=sort(rules, by="confidence", decreasing=TRUE)
inspect(head(rules))

### Pruning redundant rules
rules.sorted = sort(rules, by="lift")
subset.matrix = is.subset(rules.sorted, rules.sorted)
subset.matrix[lower.tri(subset.matrix, diag=T)] = NA
redundant = colSums(subset.matrix, na.rm=T) >= 1
rules.pruned = rules.sorted[!redundant]
inspect(head(rules.pruned))

### Visualizing association rules
install.packages("arulesViz")
library(arulesViz)
plot(rules.pruned)
plot(rules.pruned, shading="order", control=list(jitter=6))

soda_rule=apriori(data=Groceries, parameter=list(supp=0.001,conf =
    0.1, minlen=2), appearance = list(default="rhs",lhs="soda"))
plot(sort(soda_rule, by="lift"), method="graph",
    control=list(type="items"))
plot(soda_rule, method="grouped")

## Eclat
frequentsets=eclat(Groceries,parameter=list(support=0.05,maxlen=10))
summary(frequentsets)
inspect(sort(frequentsets,by="support")[1:10])

## Creating transactions with temporal information
install.packages("arulesSequences")
library(arulesSequences)
tmp_data = list(c("A"),
                c("A","B","C"),
                c("A","C"),
                c("D"),
                c("C","F"),
                c("A","D"),
                c("C"),
                c("B","C"),
                c("A","E"),
                c("E","F"),
                c("A","B"),
                c("D","F"),
                c("C"),
                c("B"),
                c("E"),
                c("G"),
                c("A","F"),
                c("C"),
                c("B"),
                c("C"))
names(tmp_data) = paste("Tr",c(1:20), sep = "")
trans =  as(tmp_data,"transactions")
transactionInfo(trans)$sequenceID=c(1,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,
    4,4,4)
transactionInfo(trans)$eventID=c(10,20,30,40,50,10,20,30,40,
    10,20,30,40,50,10,20,30,40,50,60)
trans
inspect(head(trans))
summary(trans)
zaki=read_baskets(con = system.file("misc", "zaki.txt", package =
   "arulesSequences"), info = c("sequenceID","eventID","SIZE"))
as(zaki, "data.frame")

### spade
s_result=cspade(trans,parameter = list(support = 0.75),control =
    list(verbose = TRUE))
summary(s_result)
as(s_result, "data.frame")



