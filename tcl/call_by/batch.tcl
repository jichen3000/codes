proc run_test {name} {
    puts "name : $name  "
    
    global run_state
    # print ethTxFrameDataRate
    set result_timestamp 123
    set send_rate 30
    set receive_rate 30
    puts "Report: timestamp: ($result_timestamp), ethTxFrameDataRate: ($send_rate), ethRxFrameDataRate: ($receive_rate)."
    return "{\"timestamp\": $result_timestamp, \"send_rate\": $send_rate, \"receive_rate\": $receive_rate}"
}

if {[expr {$argc != 2}]} {
    puts "$argv"
    puts "$argc"
    puts "Usage: bptcl $argv0 name"
    exit
}
set name [lindex $argv 0] 

set result [run_test $name]
puts "tcl_result\&\&\&$result\&\&\&"
