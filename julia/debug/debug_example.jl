# not support for julia 0.5 yet, 2016-10-19
# Pkg.add("Debug")
# using Debug

@debug function test1()
    a = 100
    # @bp
    b = 100
    a*b
end
# function test2()
#     a2 = 100
#     @bp
#     b2 = 100
#     a2*b2
# end

println("start")
a = 100
test1()
# test2()
