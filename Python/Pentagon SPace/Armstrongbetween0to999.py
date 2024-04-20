for number in range(0,999):
    cp=number
    length=len(str(number))
    sums=0
    while(number>0):
        rem=number%10
        number=number//10
        sums+=rem**length
    if cp==sums:
        print(sums)
    else:
        pass