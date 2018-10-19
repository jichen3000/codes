p = println
d1 = Dict(1 => 4.2, 2 => 5.3)

dmus = Dict( :first_name => "Louis", :surname => "Armstrong", :occupation =>
"musician", :date_of_birth => "4/8/1901" )

println(in((:first_name=>"Louis"), dmus))
println(haskey(dmus,:first_name))

println(dmus)

# keys1 = ["J.S. Bach", "Woody Allen", "Barack Obama"]
# values1 =  [ 1685, 1935, 1961]
# d5 = Dict(keys1, values1)
# println(d5)

dpairs = ["a", 1, "b", 2, "c", 3]
d6 = Dict(dpairs[i] => dpairs[i+1] for i in 1:2:length(dpairs))
p(d6)

for item in dmus
    p(item)
    p(typeof(item))
    p(item[1])
    # p(key)
end

for (key,value) in dmus
    p(key,"=>",value)
end