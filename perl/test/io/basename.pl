use File::Basename;
# use File::Basename qw( basename );
use File::Spec;
use Path::Class;
use 5.012;

my $name = "/usr/local/bin/perl";
my $basename = basename $name;
say $basename;

my $new_name = File::Spec->catfile('/usr', 'local');
say $new_name;

my $lib_dir = dir(qw( usr lib local ));
my $sub_dir = $lib_dir->subdir( 'perl' );
my $parent_dir = $lib_dir->parent;

say $lib_dir;
say $sub_dir;
say $parent_dir;
