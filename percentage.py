#take marks as input from user
print("enter marks obtained in 4 subjects:")
math=int(input("maths:"))
english=int(input("english:"))
science=int(input("science:"))
hindi=int(input("hindi:"))

#let's calculate the percentage of marks
sum=math+english+science+hindi
print("sum of math,english,science and hindi=",sum)

perc=(sum/400)*100

print (end="percentage mark=")
print(perc)