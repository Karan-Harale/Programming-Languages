for number in range(0,99):
    cp=number
    rev=0
    while(number>0):
        rem=number%10
        rev=(rev*10)+rem

        number=number//10
    if cp==rev:
        print(cp)
    else:
        pass