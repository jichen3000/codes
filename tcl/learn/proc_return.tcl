proc foo {a {b bar}} {
    set result {}
    lappend result $a $b

    if {$b == "bar"} {
        puts "=="
    } else {
        puts "!="
    }

    return $result
}

set return_list [foo "1" "2"]
puts $return_list

set return_list [foo "1"]
puts $return_list

proc bar {a {b bar}} {
    array set   capital         {Italy Rome  Germany Berlin}

    # return [array get capital]
}
# bar "1"
# array set return_list  [bar "1"]
# puts $return_list
# set a_i a
# puts $return_list($a_i)
