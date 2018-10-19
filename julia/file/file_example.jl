file_name = "some.dat"
open(file_name, "w") do the_file
    write(the_file, "first\n")
    write(the_file, "second\n")
    write(the_file, "third\n")
end

data_file = open(file_name)
for line in readlines(data_file)
    println(line)
end
close(data_file)


open(file_name) do the_file
    for line in eachline(the_file)
        print(line)
    end
    println("")
end