use 5.012;

my @num_list = (2,3,4,1,2);
say @num_list;
sub by_num {
    $a <=> $b;
}
my @sorted_num_list = sort by_num @num_list;

say @sorted_num_list;
say @num_list;

sub by_str { 
    $a cmp $b; 
}
my @str_list = qw( mm colin niu );
my @sorted_str_list = sort by_str @str_list;
say "@sorted_str_list";