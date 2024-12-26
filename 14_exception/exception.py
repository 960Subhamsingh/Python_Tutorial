num=input("Enter only Number")
num2=input("Enter only Number")
try:
    avg=(int(num)+int(num2))/2
except Exception as err:
    print(err)
finally:
    print(avg)
    # print("final statement")