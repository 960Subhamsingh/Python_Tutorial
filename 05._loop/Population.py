# 1. Population Growth Calculation

# Initial Population: 10000
# Growth Rate: 10% annually
# Duration: 10 years

curr_pop = 10000
for i in range(10, 0, -1):
    print(i, curr_pop)
    curr_pop = curr_pop / 1.1