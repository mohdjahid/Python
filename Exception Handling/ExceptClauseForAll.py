try:
    fb=open("foo.bar",'r');
except:
    print('File not found');
else:
    print('File read successfully');

print('Exception has handled');
