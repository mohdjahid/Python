def printinfo(arg,*values):
    print('Number of arguments are');
    print(arg);
    for var in values:
        print(var);
    return;

printinfo(10);
printinfo(10,20,30,40,50);
