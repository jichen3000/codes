p = println
# (31+42)::Float64
convert(Int64, 16.0)
Int64(16.0)

promote(1, 2.5, 3//4) #returns (1.0, 2.5, 0.75) 
promote(1.5, im) #returns (1.5 + 0.0im, 0.0 + 1.0im) 
promote(true, 'c', 1.0) #returns (1.0, 99.0, 1.0)

println(promote_type(Int8, Int16))
# promote_rule(::Type{Int8}, ::Type{Int16}) = Int64

p(supertype(Int64))
p(subtypes(Signed))
p(Bool <: Integer)
p(issubtype(Bool, Integer))