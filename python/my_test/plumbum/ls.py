import plumbum

ls = plumbum.local["ls"]
print ls()

ls["-l"] & plumbum.FG