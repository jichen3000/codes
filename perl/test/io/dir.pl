use 5.012;
use File::Spec::Functions;

my $etc = '/etc';
opendir my $dh, $etc or die "Cannot open $etc: $!";
for my $file (readdir $dh) {
    next if $file eq '.' or $file eq '..';
    my $file_path = catfile($etc, $file);
    say "file: $file_path";
}
closedir $dh;