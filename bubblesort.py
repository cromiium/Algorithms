import numpy as np          #copied from quicksort.py

print("Enter size of desired list")
size_of_list = int(input())
orig_list = np.random.randint(0,high=999,size=size_of_list)
print(orig_list)
def bubble_sort(sorting_list:list) -> list:
    for i in range (len(sorting_list)):
        for j in range(0,len(sorting_list)-1):
            if sorting_list[j] > sorting_list[j+1]:
                sorting_list[j], sorting_list[j+1] = sorting_list[j+1], sorting_list[j]
    return sorting_list
    
print(bubble_sort(orig_list))

