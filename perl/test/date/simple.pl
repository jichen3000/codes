use 5.012;
use DateTime;

my $dt = DateTime->from_epoch(epoch=>time);
say $dt;
say $dt->year;

my $duration = DateTime::Duration->new( days=>10 );
my $dt3 = $dt + $duration;
say $dt3;