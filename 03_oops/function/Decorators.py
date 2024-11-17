import time

def cal_Squar(numb):
    start = time.time()
    result = []
    for num in numb:
        result.append(num*num)
    end = time.time()
    print('cal_Squar ' + str((end-start)*1000) + "mil sec")
    return result
def cal_cube(numb):
    start = time.time()
    result = []
    for num in numb:
        result.append(num*num*num)
    end = time.time()
    print('cal_cube ' + str((end-start)*1000) + "mil sec")
    return result

array = range(1,1000)
out = cal_Squar(array)
out_cube = cal_cube(array)
 
