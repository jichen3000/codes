p = println

cmd = `ls`
p(typeof(cmd))
p(success(cmd))
p(run(cmd))

the_dir = ".."
cmd = `ls $the_dir`
run(cmd)


# run(`echo $("\nhi\nJulia")` |> `cat` |> `grep -n J`)