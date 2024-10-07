#  write  a program to find number of vowels in a string

name = input(" Enter here ")

vowel= 0
for i in name:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="O" or i=="U" or i=="I"):
        vowel+=1
print("Number of vowel in your string ", vowel)
