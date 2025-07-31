print("Enter Marks Obtained in 4 subjects: ")
math = int(input("maths "))
english = int(input("english "))
urdu = int(input("urdu "))
history = int(input("history "))

sum=math+english+urdu+history
print("sum of math,english,urdu,history")

perc = (sum/400)*100
print(end="Percentage Mark = ")
print(perc)