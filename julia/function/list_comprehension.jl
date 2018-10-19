arr = Float64[x^2 for x in 1:4 if x!=2]
println(arr)

mat1 = [x + y for x in 1:2, y in 1:3]
println(mat1)

table10 = [x * y for x=1:10, y=1:10]
println(table10)