use 5.012;
print 1, 2, 3;
print "jc", "mm";

say "";
my @array = qw(fred barney);
print @array;
print "@array";
say "";

my($user, $days_to_die) = ("jc", 4);
printf "Hello, %s; your password expires in %d days!\n", 
    $user, $days_to_die;