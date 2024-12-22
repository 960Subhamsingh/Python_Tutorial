#  nested comprehension
x = [[j for j in range(5)] for i in range(10)]

print(x)

input_l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = [x for x in input_l if x % 2 == 0]

states = ['Gujarat', 'Maharashtra', 'Rajasthan']
capitals = ['Gandhinagar', 'Mumbai', 'Jaipur']
state_capitals = {state: capital for state, capital in zip(states, capitals)}

def c(z ,y,s=12):
    print(z,y)
    pass
c(1,y=3)


def add (a,b):
    return a+b

if __name__ == "__main__":
    print("Run")