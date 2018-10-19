# if <cond> <statement> end is written as <cond> && <statement>
a = 10
if a == 10 println(true) end
a == 10 && println(true)
# if !<cond> <statement> end is written as <cond> || <statement>
if !(a==9) println(false) end
a==9 || println(false)

b = if a==10
    "aa"
else
    "bb"
end

println(b)