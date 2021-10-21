# Insert your code here...
import numpy as np
import time

def bubble_list(some_list):

    for j in range (0,len(some_list)-1):

        for i in range (0,len(some_list)-j-1):

            if some_list[i] > some_list[i+1]:
                
                some_list[i],some_list[i+1] = some_list[i+1],some_list[i]

    return some_list


# my_list0 = np.random.randint(0,100,size=500)
# bubble_list(my_list0)
# t0 = time.time()
# print(t0)
# time.sleep(3)
# my_list1 = np.random.randint(0,100,size=3000)
# bubble_list(my_list1)
# t1 = time.time()
# print(t1)
# t2 = t1 - t0
# print(f'Time elapsed: {t2} seconds')

def time_sort(n): 

    T = []
    t = []
    
    for i in range (0,n,500):

        my_list = np.random.randint(0,100,size = i)
        bubble_list(my_list)
        T.append(time.time())
        
    for j in range (1,len(T)):
        
        t.append(T[j] - T[j-1])

    return t

time_sort(3000)
