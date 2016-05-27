proc info:wholeproc procname {
    set result [list proc $procname]
    set args {}
    foreach arg [info args $procname] {
        if {[info default $procname $arg value]} {
            lappend args [list $arg $value]
        } else {
            lappend args $arg
        }
    }
    lappend result [list $args]
    lappend result [list [info body $procname]]
    return [join $result]
}
proc foo {a {b bar}} {
    puts "$a $b"
}

puts [info:wholeproc foo]
puts [foo "mm" "jc"]
