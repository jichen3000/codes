# see the code in Chapter 7\macros.jl)
macro wrap(ex)
    quote
        println("start")
        $ex
        println("after")
    end 
end

@wrap println("some")


macro assert(ex)
    :($ex ? nothing : println("Assertion failed: ", $(string(ex))))
end

@assert 1 == 1.0
@assert 1 == 1.1

println(macroexpand(:(@assert 1 == 1.0)))


