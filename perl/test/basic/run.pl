use 5.012;

system 'date'; # use this one
# exec 'date';

my $now = `date`;
say "now: $now";

my @list = `ls -l`;
say "list : @list";