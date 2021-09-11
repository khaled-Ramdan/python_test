def binarySearch(list,item):#searching for a specific target
    st=0;en=len(list)-1
    while st<=en:
        mid=int((st+en)/2)
        if(list[mid]>item):
            en=mid-1
        elif(list[mid]<item):
            st=mid+1
        else:
            return mid
    return None
#minimizing the error
def upperbound(list,item):#first element bigger than target
    st,en=0,len(list)-1
    while st<en:
        mid=int((st+en)/2)
        if(list[mid]<=item):
            st=mid+1
        else:
            en=mid
    if(st>=len(list)):
        return None
    else:
        return st

def lowerbound(list,item):#first element bigger than or equal target
    st,en=0,len(list)-1
    while st<en:
        mid=int((st+en)/2)
        if(list[mid]<item):
            st=mid+1
        else:
            en=mid
    if(st>=len(list)):
        return None
    else:
        return st
#maximuzing valid vlaue
def check(mid,item):
    pass
def most_valid_vlue(list,item):
    st,en=0,len(list)-1
    while st<en:
        mid=int((st+en+1)/2)
        if(check(mid,item)):#still valid value
            st=mid
        else:
            en =mid-1
    if(st>=len(list)):
        return None
    else:
        return st    

if __name__ == '__main__':
    l=["ali","khaled","ahmed","mahmoud","amr","esraa","said"]
    ll=[1,865,23,45,66,21,36,12,4,59,215]
    ll.sort()
    l.sort()
    print(ll)
    a=(input("ENter a target: "))
    print(ll[most_valid_vlue(ll,int(a))])

