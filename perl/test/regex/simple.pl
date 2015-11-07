$_ = "yabba dabba doo"; 
if (/abba/) {
    print "It matched!\n"; 
}

while (<>) { # take one input line at a time
    chomp;
    if (/YOUR_PATTERN_GOES_HERE/) {
        print "Matched: |$`<$&>$'|\n"; # the special match vars 
    } else {
        print "No match: |$_|\n"; 
    }
}

$_ = "He's out bowling with Barney tonight."; 
s/Barney/Fred/; # Replace Barney with Fred 
print "$_\n";