# write a program divisible by 3 and 5 with while loop
a = 1
count =0
while(a<=100):
    if(a%3==0 or a%5==0):
        a+=1
    else:
        print(a,end=" ")
        a+=1
        count+1

print("\n")

# add all the divisble number by 3 and 5
count= 0
for i in range(1,100):
    if(i%3==0 or i%5==0):
        count+=i
        continue
print(count)
    