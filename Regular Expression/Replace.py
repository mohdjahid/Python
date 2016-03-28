import re
phone='2004-959-559 # This is Phone Number';

#Delete Python-style comment
phone=re.sub(r'#.*$',"",phone);
print('Phone Number : ',phone);

#Remove anything other than digit
phone=re.sub(r'\D',"",phone);
print('Phone Number : ',phone);
