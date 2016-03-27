#Similar to array in C but it is heterogenuous
list=['abcd',786,3.14,'john',70.2];
tinylist=[123,'john'];

print(list);          #['abcd',786,3.14,'john',70.2]
print(list[0]);       #abcd
print(list[1:3]);     #[786,3.14]
print(list[2:]);      #[3.14,'john',70.2]
print(tinylist*2);    #[123,'john',123,'john']                  // String Two Times
print(list+tinylist); #['abcd',786,3.14,'john',70.2,123,'john'] //Concatented String
