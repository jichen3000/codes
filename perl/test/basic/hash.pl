use 5.012;

my %fa = ('jc', 'colin ji', 'mm', 'MM');
# $fa{'jc'} = "colin ji";
# $fa{'mm'} = 'MM';


foreach my $person (qw( jc mm )){
    print "$person is $fa{$person}\n";
}

my @arr = %fa;
say "@arr";

my %host_names = (lab189=>'13.189', 'test-host'=>'2.101', mac=>'13.189');
my %ips = reverse %host_names;
my @arr = %ips;
say "@arr";
say "%host_names";

say keys %host_names;
say values %host_names;
# size
my $count = keys %host_names;
say "size : $count";

while ( my ($key, $value) = each %host_names) {
    print "$key => $value\n";
}




