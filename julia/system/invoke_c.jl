t = ccall( (:clock, "libc"), Int32, ())
println(t)

path = ccall((:getenv, "libc"), Cstring, (Cstring,), "SHELL")
println(unsafe_string(path))