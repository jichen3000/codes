email_pattern = r".+@.+"
input = "john.doe@mit.edu"
println(ismatch(email_pattern, input)) #> true


visa = r"^(?:4[0-9]{12}(?:[0-9]{3})?)$"  # the pattern
input = "4457418557635128"
ismatch(visa, input)  #> true
if ismatch(visa, input)
    println("credit card found")
    m = match(visa, input)
    println(m.match) #> 4457418557635128
    println(m.offset) #> 1
    println(m.offsets) #> []
    println(m.captures) #> []
end

