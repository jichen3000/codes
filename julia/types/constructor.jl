type Family
    name::String
    members::Array{String, 1}
    big::Bool
    Family(name::String) = new(name, String[], false)
    Family(name::String, members) = new(name, members, length(members) < 4)
end

fam = Family("Bates-Smith", ["Alan", "Julia", "Jeff", "Stephan", "Viral"])
println(fam)
