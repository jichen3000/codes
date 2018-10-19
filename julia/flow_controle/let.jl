anon = Array{Any}(2) # returns 2-element Array{Any,1}: #undef  #undef
for i = 1:2
    anon[i] = ()-> println(i)
    i += 1 
end

anon[1]()
anon[2]()

anon = Array{Any}(2)
for i = 1:2
    let i = i
        anon[i] = ()-> println(i)
    end
    i += 1
end
anon[1]()
anon[2]()
