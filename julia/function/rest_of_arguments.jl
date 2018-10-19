function fname(arglist)
    # return 1
    1,2
end

println(fname(2))

function varargs(n, m, args...)
    "arguments : $n $m $args"
end

println(varargs(1,2,3,4,5))


function varargs2(args...)
    "arguments2: $args"
end

a = [1,2,3,4,5]
println(varargs2(a...))
