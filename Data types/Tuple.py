#Similar to list however:
#       1. tuples are enclosed within paranthesis ()
#       2. can't be updated
#       3. They are read-only list
tuple=('abcd',768,3.14,'john',70.2 );
tinytuple=(123,'john');
print(tuple);
print(tuple[0]);
print(tuple[1:3]);
print(tuple[2:]);
print(tuple*2);

tuple[2]=200; # Error 'tuple' object doesn't support assignment operation 

