p = println

p("for array creating:")
[1,2,3]
# 3-element Array{Int64,1}:
#  1
#  2
#  3

[1;2;3]
# 3-element Array{Int64,1}:
#  1
#  2
#  3

[1 2 3]
# 1×3 Array{Int64,2}:
#  1  2  3

v = [1,2,3] 
w = [7,8,9]
[v, w]

[v, w]
# 2-element Array{Array{Int64,1},1}:
#  [1,2,3]
#  [7,8,9]

[v;w]
# 6-element Array{Int64,1}:
#  1
#  2
#  3
#  7
#  8
#  9

[v w]
# 3×2 Array{Int64,2}:
#  1  7
#  2  8
#  3  9

# allow
[1 2;3 4]

# not allow
[1;2 3;4]

a = [1 2; 3 4]
b = [5 6; 7 8]

[a b]
[a;b]
[a,b]

