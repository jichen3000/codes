proc fmtable table {
   set maxs {}
   foreach item [lindex $table 0] {
       lappend maxs [string length $item]
   }
   foreach row [lrange $table 1 end] {
       set i 0
       foreach item $row max $maxs {
           if {[string length $item]>$max} {
               lset maxs $i [string length $item]
           }
           incr i
       }
   }
   set head +
   foreach max $maxs {append head -[string repeat - $max]-+}
   set res $head\n
   foreach row $table {
       append res |
       foreach item $row max $maxs {append res [format " %-${max}s |" $item]}
       append res \n
   }
   append res $head
}

set table {
   {1 short "long field content"}
   {2 "another long one" short}
   {3 "" hello}
}
puts [fmtable $table]