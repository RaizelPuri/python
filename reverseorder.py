num=int(input("Enter a number"))
num=abs(num)
count=0
if num==0:
 count=1
else:
 count+=1
 num=num //10
print("total digits=" ,count)