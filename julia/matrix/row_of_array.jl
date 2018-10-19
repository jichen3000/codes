# a (column) vector
[1,2,3]
[1; 2; 3]
# 3-element Array{Int64,1}:
#  1
#  2
#  3

# a row vector 
row=[1 2 3]
# 1×3 Array{Int64,2}:
#  1  2  3

for i in row
    println(i)
end

Array{Int64, 1} == Vector{Int64} #> true
Array{Int64, 2} == Matrix{Int64} #> true