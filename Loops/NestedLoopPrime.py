i=2;
while(i<100):
    j=2;
    while(j<=(i/j)):
        if not (i%j):break; # if i%j gives a non-zero number than it is true
        j=j+1;
    if(j>i/j): print(i,' is prime');
    i=i+1;
