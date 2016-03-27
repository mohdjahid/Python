#open a file
fo=open("foo.txt","r+");
str=fo.read(10);
print('Read string is : ',str);
#Check current osition
position=fo.tell();
print('Current position : ',position);
#Repositioning pointer at the begining once again
fo.seek(0,0);
     #offset,0
             # 0 means begining
             # 1 maens current position
             # 2 means end of file
str=fo.read(10);
print('Read string is : ',str);
