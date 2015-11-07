set y "some"
set x 1
puts "some $y $x"

proc sreverse str {
    set res ""
    for {set i [string length $str]} {$i > 0} {} {
        append res [string index $str [incr i -1]]
    } 
    set res
}
 
puts [sreverse "A man, a plan, a canal - Panama"]

set example {foo bar grill}
puts $example

set      x {foo bar}
llength  $x        ;#--> 2
lappend  x  grill  ;#--> foo bar grill
lindex   $x 1      ;#--> bar (indexing starts at 0)
lsearch  $x grill  ;#--> 2 (the position, counting from 0)
lsort    $x        ;#--> bar foo grill
linsert  $x 2 and  ;#--> foo bar and grill
lreplace $x 1 1 bar, ;#--> foo bar, and grill
puts $x
puts [lsort    $x]

set test {{a b} {c d}}
lset test 1 1 x
puts $test

proc in {list el} {expr {[lsearch -exact $list $el] >= 0}}
puts [in {a b c} b]

proc lremove {_list el} {
  upvar 1 $_list list
  puts $list
  set pos [lsearch -exact $list $el]
  set list [lreplace $list $pos $pos]
}
 
set t {foo bar grill}
lremove t bar
puts $t

proc transpose matrix {
   foreach row $matrix {
       set i 0
       foreach el $row {lappend [incr i] $el}
   }
   set res {}
   set i 0
   foreach e [lindex $matrix 0] {lappend res [set [incr i]]}
   set res
}
 
puts [transpose {{1 2} {3 4} {5 6}}]
