Greetings = "Good Morning"
# if else loop
if Greetings == "Morning":
    print("Condition matches")
else:
    print("Condition do not matches")
print("if else loop is completed")

# for loop
obj = [2,4,5,7,8]
for i in obj:
    print(i)

summ = 0
for j in range(1, 6): # by default it will be j++ for every iteration
    summ = summ + j
print(summ)

for k in range(1, 10, 2): # this will be k+2 for every iteration
    print(k)