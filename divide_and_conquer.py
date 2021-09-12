#divide and conquer algorithm
'''
if you have a farme with lenght l and width w .
you want to split the farme into maximam area equal squares.
what is are of each square?
'''
def solve(l,w):
    a=max(l,w)
    b=min(l,w)
    if (a%b==0):
        return b
    else:
        return solve(b,  a % b )
#sum of array elements using recursion
def sum_Array_numbers(arr,i=0,sum=0):
    if(i==len(arr)):
        return sum
    else:
        sum+=arr[i]
        return sum_Array_numbers(arr,i+1,sum)

if __name__ == '__main__':
     w=int(input("Enter lenght: "))
     l=int(input("Enter width: "))
     xx=solve(w,l)
     print(f"Number of squares = {(w*l)/(xx**2)}\nlenght of each square= {xx}")
    #l=[1,2,3,6]
    #print(sum_Array_numbers(l))
