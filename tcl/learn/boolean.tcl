foreach b {0 1 2 13 true false on off no yes n y a} {
    puts "$b -> [expr {$b?1:0}]."
}