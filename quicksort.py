import numpy as np

#print("Enter size of desired list")
#size_of_list = input()
orig_list = np.random.randint(0,high=999,size=100)
print(orig_list)

'''
quicksort:
    divide:
        partition array into 2 subarrays such that A[p..q-1] and A[q+1..r]
        such that all elements in A[p..q-1] are smaller than A[q] and all
        elements of A[q+1..r] are larger than A[q]
    conquer:
        sort the two subarrays by recursively callikng quicksort
    combine:
        subarrays are sorted so A[p..r] should be sorted
'''

def quick_sort(sorting_list:list) -> list:
    if len(sorting_list) <= 1:
        return sorting_list
    else:
        return(quick_sort([element for element in sorting_list[1:] if element <=sorting_list[0]])
            + [sorting_list[0]] + quick_sort([element for element in sorting_list[1:] if element > sorting_list[0]])
        )

sorted_list = quick_sort(orig_list)
print(sorted_list)