#Code not working syntax error where here
#Define a function here
def temp_conv(var):
    try:
        return int(var);
    except ValueError, Argument: #here
        print('The Argument doesn''''t contain number ''',Argument);

temp_conv('xyz');        
