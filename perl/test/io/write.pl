use autodie;
use 5.012;

my $log_filename = 'test.log';
open LOG, '>', $log_filename;

print LOG "put some\n";
select LOG;
print "put some2\n";

close LOG;

select STDOUT;
open LOG, $log_filename;
while (<LOG>) {
    chomp;
    print "$_";
}

print "ok\n";

# die "file existed!" if -e $log_filename;

# how old
say -M $log_filename > 1;
# size
say -s $log_filename;

# virtual filehanler
say -r $log_filename and -w _;

say glob '*.log';
say <*.log>;