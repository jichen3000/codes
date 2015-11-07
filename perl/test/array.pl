use 5.010;
$rocks[0] = 'bedrock';
$rocks[1] = 'slate';
$rocks[2] = 'lava';
$rocks[3] = 'crushed rock';
$rocks[99] = 'schist';

say $rocks[$#rocks];
say $rocks[-1];

@ll = (1,2,3);
say @ll;
say $ll[2];
say (1,2,3);
say (1..10);
say (0..$#rocks);
say qw(fred barney betty wilma dino);

($fred, $barney, $dino) = ("flintstone", "rubble", undef);
($aa, $bb) = ("aa", "bb");

@arr = 5..9;
$fred = pop @arr;
say @arr;
say $fred;

push @arr, 100;
say @arr;

@array = qw( pebbles dino fred barney betty ); 
@removed = splice @array, 1, 2; # remove dino, fred
# @removed is qw(dino fred)
# @array is qw(pebbles barney betty)
say @removed;
say @array;

@array = qw( pebbles dino fred barney betty );
@removed = splice @array, 1, 2, qw(wilma); # remove dino, fred
# @removed is qw(dino fred)
# @array is qw(pebbles wilma
# barney betty)
say @removed;
say @array;

print "array : @array\n";
print "array : (@array)\n";
print "this is $array[3]\n";


@people = qw( fred barney betty );
@sorted = sort @people; # list context: barney, betty, fred 
$number = 42 + @people; # scalar context: 42 + 3 gives 45
say @sorted;
say $number;

@wilma = undef;
@betty = ( );