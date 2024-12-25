choco = int(input('how many chocolates you want? '))
i = 1
av = 20

while i<=choco:
    if(i>av):
        print("Sorry , Not Available ")
        break
    print("Chocolate" , i)
    i+=1
else:
    print("Thank You for contact")