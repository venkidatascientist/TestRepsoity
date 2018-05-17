#lower,higher=int(input('enter lower value  - ')),int(input('enter higher value - '))
for num in range(1,10):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)