puts "There are $argc arguments to this script"
puts "The name of this script is $argv0"
if {$argc > 1} {
    puts "The other arguments are: $argv" 
    set first [lindex $argv 0] 
    exit
    puts "first: $first"
}

# puts "You have these environment variables set:"
# foreach index [array names env] {
#     puts "$index: $env($index)"
# }