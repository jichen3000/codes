most_common = function(the_vector){
    count_table = table(the_vector)
    names(count_table)[count_table == max(count_table)]
}

x = c(1,2,3,3,3,4,4,5,5,5,6)
most_common(x)