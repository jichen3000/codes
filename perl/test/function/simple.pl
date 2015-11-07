use 5.010;
use strict;
my $n = 0;
sub marine {
    $n += 1; # Global variable $n 
    print "Hello, sailor number $n!\n";
    $n;
}

say &marine;
say &marine;

sub add {
    if (@_ != 2){
        print "only support tow arguments!\n";
        return;
    }
    my($first, $second) = @_;
    $first + $second;
}

say &add(1,2);
say &add(1,2,3);


sub max {
    my($max_so_far) = shift @_; # the first one is the largest yet seen 
    foreach (@_) { # look at the remaining arguments
        if ($_ > $max_so_far) { # could this one be bigger yet? 
            $max_so_far = $_;
        } 
    }
    $max_so_far; 
}

say max(3,2,5,6)