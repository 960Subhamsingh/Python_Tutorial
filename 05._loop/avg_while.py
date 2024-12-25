# Average of Numbers Until 0
count = 0
total = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    total += number
    count += 1
if count > 0:
    average = total / count
    print(f"Average of entered numbers: {average}")
else:
    print("No numbers entered.")