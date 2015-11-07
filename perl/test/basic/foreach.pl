use 5.010;
foreach $rock (reverse(qw/ bedrock slate lava /)) {
    print "One rock is $rock.\n"; # Prints names of three rocks
}

$rock = 123;
say "rock: $rock";
@rocks = qw/ bedrock slate lava /; 
foreach $rock (@rocks) {
    $rock = "\t$rock"; # put a tab in front of each element of @rocks
    $rock .= "\n"; # put a newline on the end of each 
}
print "The rocks are:\n", @rocks;
say "rock: $rock";

foreach (1..10) { # Uses $_ by default 
    print "I can count to $_!\n";
}

# use 5.012;
@rocks = qw/ bedrock slate rubble granite /; 
while( my( $index, $value ) = each @rocks ) {
    say "$index: $value"; 
}

@rocks = qw/ bedrock slate rubble granite /; 
foreach $index ( 0 .. $#rocks ) {
    print "$index: $rocks[$index]\n"; 
}