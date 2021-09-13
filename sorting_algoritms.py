"""
sort algorithms
"""
#selection sort
#time complexity O(n*n)
def find_smallest(arr):#finding smallest valuee in the array
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if(smallest>arr[i]):
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def selection_sort(arr):
    newArr=[]
    for i in range (len(arr)):
        index=find_smallest(arr)
        newArr.append(arr[index])
        arr.pop(index)
    return newArr
#qiuck sort
#time complexity on avearge is O(nlog n) in owrest case O(n*n) depending on the pivot
#fastest sorting algorithm
def quick_sort(arr):
    if(len(arr)<2):
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i<=pivot]
        greater=[i for i in arr[1:] if i>pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)

#bubble sort

if __name__ == '__main__':
    l=[12,56,845,23,45,23,45,76,4,3,8,9,4,6]
    print(l)
    print(selection_sort(l))
    print(quick_sort(l))
