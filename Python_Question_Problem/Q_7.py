#  write a program check wether the passed better is a vowel or not

letter = input("Enter the character : ")

if(letter in "aeiou") or  (letter in "AEIOU"):
    print("Is is a vowel")
else:
    print("It is not a vowel")