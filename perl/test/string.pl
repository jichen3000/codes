use utf8;
use 5.010;
use warnings;

say "hello"."world";
say 5 x 4.8;
say 1==1;
say "123" lt "345";
say !!"fred";
say !!"0";
say "";

$ss = "123 \n\n";
say $ss.'e';
say chomp($ss); # only remove one
say $ss.'e';

say defined($aaa);


# my @fields = split /separator/, $string;
my @fields = split /,/, "123,456";
say "@fields";

my @fields = split ',', "123,456";
say "@fields";

my $x = join ":", 4, 6, 8, 10, 12; # $x is "4:6:8:10:12"
say $x;

my @arr = (1,2);
my $x = join ":", @arr; # $x is "4:6:8:10:12"
say $x;
