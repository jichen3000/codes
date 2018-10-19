function fib_producer(n)
    a, b = (0, 1)
    for i = 1:n
        produce(b)
        a, b = (b, a + b)
    end
end

# The Task constructor argument must be a function with 0 arguments
fib_task = Task( () -> fib_producer(10) )
println(consume(fib_task))
for i in fib_task
    println(i)
end

println("@task:")
fib_task = @task fib_producer(10)
for i in fib_task
    println(i)
end

a = @async 1 + 2 # Task (done) @0x000000002d70faf0
consume(a) # 3
