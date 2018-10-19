
# x |> f, it applies the function f to the argument x
a = 1:10 |> (x -> sqrt(x)) |> sum
println(a)