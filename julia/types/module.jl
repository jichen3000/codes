module Colin
    # export p
    p = println
end

Colin.p("123")
println(names(Colin))
println(whos(Colin))
println(names(Main))

module Colin
    mm = println
end

Colin.mm("mm")
# require("module.jl")
# Using Colin
#请记住：当你离开这个世界时，你不能带走任何你已经获得的东西，唯一能带走的只有一颗充满诚实、爱、牺牲和勇气的心。

# include