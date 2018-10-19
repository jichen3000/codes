macro timeit(ex)
    quote
        local t0 = time()
        # local val = $(esc(ex))
        local val = $(ex)
        local t1 = time()
        print("elapsed time in seconds: ")
        @printf "%.3f" t1 - t0
        println("")
        val
    end 
end

a = 999999.99999
println(@timeit a^100)
# println(a^100)
