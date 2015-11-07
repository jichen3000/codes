# Initialise the state
after 10000 set state timeout
set server [socket -server accept 12345]
proc accept {args} {
   puts "in accept"
   global state connectionInfo
   set state accepted
   set connectionInfo $args
}

# Wait for something to happen
vwait state

# Clean up events that could have happened
close $server
after cancel set state timeout

# Do something based on how the vwait finished...
switch $state {
   timeout {
      puts "no connection on port 12345"
   }
   accepted {
      puts "connection: $connectionInfo"
      puts [lindex $connectionInfo 0] "Hello there!"
   }
}