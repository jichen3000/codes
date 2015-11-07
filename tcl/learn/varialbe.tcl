set foo    42     ;# creates the scalar variable foo
set bar(1) grill  ;# creates the array bar and its element 1
set baz    $foo   ;# assigns to baz the value of foo
set baz [set foo] ;# the same effect
puts [info exists foo]   ;# returns 1 if the variable foo exists, else 0
unset foo         ;# deletes the variable foo

# the $foo notation is only syntactic sugar for [set foo]. 

set foo   42
set bar1   foo
set grill bar1
puts [set [set [set grill]]] ;# gives 42

puts [set [set grill]]


set balance 0

proc deposit {amount} {
    global balance
    set balance [expr {$balance + $amount}]
    puts $balance
}

deposit 4

proc withdraw {amount} {
    set ::balance [expr {$::balance - $amount}]
 }

puts [info vars] ;#-- lists all visible variables
info locals
info globals

# To make all global variables visible in a procedure (not recommended):
eval global [info globals]


# #include <stdio.h>
# int main(void) {
#   int    i =      42;
#   int *  ip =     &i;
#   int ** ipp =   &ip;
#   int ***ippp = &ipp;
#   printf("hello, %d\n", ***ippp);
#   return 0;
# }
set i    42
set ip   i
set ipp  ip
set ippp ipp
puts "hello, [set [set [set [set ippp]]]]"
puts "hello, [set [set [set $ippp]]]"


proc const {name value} {
  uplevel 1 [list set $name $value]
  uplevel 1 [list trace var $name w {error constant ;#} ]
}
 
const x 11
# incr x