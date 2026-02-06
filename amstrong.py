num=int(input("enter a number:"))
temp=num
sum=0
o=len(str(temp))
while temp > 0:
    digit=temp % 10
    sum=sum+digit**o
    temp=temp//10

if sum == num:
    print(num,"is a palindrome")    
else:
    print(num,"not a plindome")