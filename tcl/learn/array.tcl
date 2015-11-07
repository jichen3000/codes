#-- The key is specified in parens after the array name
set         capital(France) Paris

#-- The key can also be substituted from a variable:
set                  country France
puts       $capital($country)

#-- Setting several elements at once:
array set   capital         {Italy Rome  Germany Berlin}

# puts [array $capital]
#-- Retrieve all keys:
array names capital    ;#-- Germany Italy France -- quasi-random order
puts [array names capital]

#-- Retrieve keys matching a glob pattern:
puts [array names capital F* ];#-- France

# anonymous array
set (example) 1
puts $(example)
