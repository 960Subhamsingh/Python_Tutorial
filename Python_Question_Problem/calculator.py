# # Python program for simple calculator
  
# # Function to add two numbers 
# def add(num1, num2):
#     return num1 + num2
  
# # Function to subtract two numbers 
# def subtract(num1, num2):
#     return num1 - num2
  
# # Function to multiply two numbers
# def multiply(num1, num2):
#     return num1 * num2
  
# # Function to divide two numbers
# def divide(num1, num2):
#     return num1 / num2


  
def vegan_calculator(m, y):
  
    # coverting years to months
    months_vegan = y * 12 + m
  
    # calculating things saved
    water = 4164 * months_vegan
    grain = 20.4 * months_vegan
    forest = 2.7 * months_vegan
    co2 = 9 * months_vegan
  
    # printing the statistics
    print("You have been vegan for " + str(months_vegan) + " months.")
    print("\nYou have successfully saved :")
    print(str(water) + " litres of water")
    print(str(round(grain)) + " kgs of grain")
    print(str(round(forest)) + " square metres of forest")
    print(str(round(co2)) + " kgs of carbon dioxide")
  
# Driver code
if __name__=="__main__":
    months = 4
    years = 2
    vegan_calculator(months, years)
