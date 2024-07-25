import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args , **kwargs)
        end= time.time()
        print(func.__name__ + " took " + str((end-start)* 1000) + " mil sec")
        return result
    return wrapper
@time_it
def cal_Squar(numb):
     
    result = []
    for num in numb:
        result.append(num*num)    
    return result
@time_it
def cal_cube(numb):     
    result = []
    for num in numb:
        result.append(num*num*num)     
    return result

array = range(1,1000)
out = cal_Squar(array)
out_cube = cal_cube(array)
 
