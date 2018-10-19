# http://stackoverflow.com/questions/936748/declaring-a-const-variable-in-r

a <- 1
lockBinding("a", globalenv())
a <- 2
# Error: cannot change value of locked binding for 'a'

# notice,
rm(a)
a <- 2
