println("in:")
a = for i in 1:5
    println(i + 1)
end
println(a)

println("=:")
a = for i = 1:5
    println(i + 1)
end
println(a)

println("index:")
for (index, value) = enumerate(3:6)
    println(index, ":",value)
end

println("break:")
for (index, value) = enumerate(3:6)
    if index == 2
        break
    end
    println(index, ":",value)
end

println("continue:")
for (index, value) = enumerate(3:6)
    if index == 2
        continue
    end
    println(index, ":",value)
end
