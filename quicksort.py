from numpy.random import randint as randi

print("Enter size of desired list")
size_of_list = int(input())
orig_list = randi(0,high=999,size=size_of_list)
print(orig_list)

''' From CLRS Introduction to Algorithms:
quicksort:
    divide:
        partition array into 2 subarrays such that A[p..q-1] and A[q+1..r]
        such that all elements in A[p..q-1] are smaller than A[q] and all
        elements of A[q+1..r] are larger than A[q]
    conquer:
        sort the two subarrays by recursively calling quicksort
    combine:
        subarrays are sorted so A[p..r] should be sorted
'''

def quick_sort(sorting_list:list) -> list:
    if len(sorting_list) <= 1: #base case
        return sorting_list
    else: #divide+conquer+combine all inline
        return(quick_sort([element for element in sorting_list[1:] if element <=sorting_list[0]])
            + [sorting_list[0]] + quick_sort([element for element in sorting_list[1:] if element > sorting_list[0]])
        )

sorted_list = quick_sort(orig_list)
print(sorted_list)