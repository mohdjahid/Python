import re
line='Cats are smarter than dogs';
matchObj=re.match(r'dogs',line,re.M|re.I);

if matchObj:
    print('matchGroup() : ',matchObj.group());
else:
    print('No Match!!!');
    
searchObj=re.search(r'dogs',line,re.M|re.I);
if searchObj:
    print('searchGroup() : ',searchObj.group());
else:
    print('No Match!!!');    
    
