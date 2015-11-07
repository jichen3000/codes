use strict;

# while (defined(my $line = <STDIN>)) {
#     print "I got $line";
# }

# only in this while, $_ is the input line.
# while (<STDIN>) {
#     print "I got $_";
# }

while (<>) {
    print "I got $_";
}