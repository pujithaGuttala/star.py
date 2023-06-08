a=int(input())
i=0
while i<=a:
    k=1
    while k<=a+i:
        print(" ",end="") 
        k=k+1
    b=1
    while b<=a-i:
        print("*",end=" ")
        b+=1
   
    print()
    i=i+1

