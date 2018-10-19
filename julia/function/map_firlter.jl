println( map(x -> x * 10, [1, 2, 3]) )

# cubes = map(x-> x^3, [1:5])
cubes = map(x-> x^3, 1:5)
println( cubes )


a = filter( n -> iseven(n), 1:5)
println(a)