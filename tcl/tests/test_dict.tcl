array set val [list a 1 c 6 d 3]

foreach {k v} [array get val * ] {
    puts $k:$v
}

set e_f [dict create dog chien cat chat cow vache horse cheval]
puts $e_f
puts [dict get $e_f dog]

dict set e_f snake fsss

puts $e_f
dict for {k v} $e_f {
    puts $k:$v
}