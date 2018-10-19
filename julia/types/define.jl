p = println
type Point
    x::Float64
    y::Float64
    z::Float64
end

a = Point(2,4,1.3)
p(a)
p(a.x)
# p(supertype(a))
p(isa(Point, Any))

b = Point(2,3,4)
p(b)

p(methods(Point))

immutable Vector3D
    x::Float64
    y::Float64
    z::Float64
end

abstract Employee
type Developer <: Employee
    name::String
    iq
    favorite_lang::String
end

p(methods(Employee))

Developer(name, iq) = Developer(name, iq, "Ruby")
colin = Developer("Colin", 120)
p(colin)


type Person
    firstname::String
    lastname::String
    sex::Char
    age::Float64
    children::Array{String, 1}
end
p1 = Person("Alan", "Bates", 'M', 45.5, ["Jeff", "Stephan"])

people = Person[]
p(people)
push!(people, p1)
push!(people, Person("Julia", "Smith", 'F', 27, ["Viral"]))
p(people)

fullname(p::Person) = "$(p.firstname) $(p.lastname)"

p(fullname(p1))