k(x; a1 = 1, a2 = 2) = x * (a1 + a2)

println(k(1,a2=3))

function varargs2(;args...)
    println(args[1])
    args
end

println(varargs2(k1="name1", k2="name2", k3=7))