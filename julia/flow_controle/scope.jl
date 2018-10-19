x=9
function funscope(n)
    x = 0 # x is in the local scope of the function
    for i = 1:n
        # local x # x is local to the for loop x=i+1
        if (x == 7)
            println("This is the local x in for: $x") # 7
        end
    end
    x
    println("This is the local x in funscope: $x") # 0
    global x = 15
end

funscope(10)


