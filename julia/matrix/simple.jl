matrix = [1 2 3; 3 4 5]
# 2×2 Array{Int64,2}:
#  1  2
#  3  4
println(matrix)

println(ndims(matrix))
println(size(matrix))
println(length(matrix))

nrows, ncols = size(matrix)

aa = eye(3)
println(aa)
aa += 1
println(aa)

v = [1.,2.,3.] 
w = [2.,4.,6.]
println(hcat(v,w))
println(vcat(v,w))
# println(append!(v,w))

println([v w])
println([v,w])
println([v;w])
