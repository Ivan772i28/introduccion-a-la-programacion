a=0
b=1
print ("0-",a)
print ("1-",b)
i=2
while i<=10:
    c=a+b
    print (i,"-",c)
    a=b
    b=c
    i+=1
    """
    otra forma de hacerlo
    for i in range(2,11):
        c=a+b
        print (i,"-",c)
        a=b
        b=c
    """