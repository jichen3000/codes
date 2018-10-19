using Base.Test
@test 1 == 1
# @test 1 == 3

arr = [1, 2] 
println(@which sort(arr))

@show 2 + 3

@time [x^2 for x in 1:1000]
# println(@timed [x^2 for x in 1:1000])

println(@elapsed [x^2 for x in 1:1000])

# memory
println(@allocated [x^2 for x in 1:1000])

# time
tic()
[x^2 for x in 1:1000]
toc()