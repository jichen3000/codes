a = []
result=try
    pop!(a)
catch ex
    if isa(ex, DomainError)
    else
        println(typeof(ex))
        showerror(STDOUT, ex)
        println()
        "mm"
    end
end
println(result)

# println("rethrow")
# try
#     pop!(a)
# catch ex
#     println(typeof(ex))
#     showerror(STDOUT, ex)
#     println()
#     rethrow(ex)
# finally
#     println("finally")
# end