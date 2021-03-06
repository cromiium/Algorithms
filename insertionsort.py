import numpy as np          #copied from quicksort.py

print("Enter size of desired list")
size_of_list = int(input())
orig_list = np.random.randint(0,high=999,size=size_of_list)
print(orig_list)

'''
insertionsort:
    inserts element A[j] into the sorted sequences A[1..j-1]
'''

def insert_sort(sorting_list:list) -> list:
    for index in range(1,len(orig_list)):
        insertion_index = index
        while(insertion_index > 0 and sorting_list[insertion_index-1] > sorting_list[insertion_index]):
            sorting_list[insertion_index], sorting_list[insertion_index-1] = sorting_list[insertion_index-1], sorting_list[insertion_index]
            insertion_index -= 1
    return sorting_list

sorted_list = insert_sort(orig_list)
print(sorted_list)