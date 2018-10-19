# Pkg.add("Gallium")
using Gallium

function test1()
    a = 100
    # @bp
    b = 100
    a * b
end

@enter test1()