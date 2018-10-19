# type Point{T}
#     x::T
#     y::T 
# end

type Point{T <: Real}
    x::T
    y::T 
end


add{T}(x::T, y::T) = x + y