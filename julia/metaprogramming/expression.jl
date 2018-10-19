p = println
the_code = :(1+2)
p(typeof(the_code))
# p(names(the_code))
p(the_code.head)
p(the_code.args)
p(the_code.typ)

quote_code = quote
    a = 45
    b = a^2
    a - b
end
p(typeof(quote_code))

dump(:(2+3*4))

e1 = Expr(:call, *, 3, 4)
p(eval(e1))

e2 = Expr(:call, *, 3, :a)
# eval(e2)
a = 4
p(eval(e2))

p("\$ for interpolation")
e5 = :($a + b)
p(e5)