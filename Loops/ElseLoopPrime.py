for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j=num//i;
            print(num,' equals ',i,' * ',j);
            break;
    else:
        print(num,' is prime numeber');
        
