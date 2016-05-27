set aa "123\
456"

puts $aa

puts [concat "a" "b"]

set a abc
set b 127
set c $a$b

set c [format {%s%s} \
        $a $b]

puts $c

# set var 0
# for {set i 1} {$i <= 10} {incr i} {
#     append var "," $i
# }
# puts $var