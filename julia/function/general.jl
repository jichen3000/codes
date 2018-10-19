f(n, m) = "base case"
f(n::Number, m::Number) = "n and m are both numbers"
f(n::Number, m) = "n is a number"
f(n, m::Number) = "m is a number"
f(n::Integer, m::Integer) = "n and m are both integers"

println(typeof(f))

println(f(1,2))
println(f(1,2.5))
println(f(1,""))
println(f(true,""))
println(f("",""))
