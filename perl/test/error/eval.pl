use 5.012;

my $fred = 1;
my $dino = 0;
my $barney = eval { $fred / $dino } // 'NaN';
print "I couldn't divide by \$dino: $@" if $@;

unless( eval { $fred / $dino } ) {
    print "I couldn't divide by \$dino: $@" if $@; 
}

# example for try catch:
# local $@;
# eval {
#     die "some " if ...
# };
# if ($@ =~ //){

# }

# use Try::Tiny;
# try {

# }
# catch{

# }
# finally{
    
# }