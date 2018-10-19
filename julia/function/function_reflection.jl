# how a function is represented internally
println(code_lowered(+, (Int, Int)))

# see the type-inferred form: 
println(code_typed(+, (Int, Int)))

println(code_llvm(+, (Int, Int)))
println(code_native(+, (Int, Int)))