type Point
    x::Float64
    y::Float64
end
type Vector2D
    x::Float64
    y::Float64
end
VecOrPoint = Union{Vector2D, Point}

p=Point(2,5)
v=Vector2D(3,2)
println(isa(p, Vector2D))
println(isa(p, VecOrPoint))