puts [expr 2/3.]
puts [format %.2f [expr 2/3.]]

set n [expr 2/3.]
puts $n
puts [format %.2f $n]
puts [expr $n * 3]

set n 1
puts [incr n] 

proc tcl::mathfunc::fac x {expr {$x < 2? 1: $x * fac($x-1)}}
 
puts [expr fac(100)]

set i [expr 1/0.]
puts {"infinit:" $i}

set j NaN
puts [expr {$j == $j}]
puts [expr {$j != $j}]

if [expr {$j != $j}] {
    puts "true"
}