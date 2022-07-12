
def pos_check(a, val):
    return(all(x > val for x in a))

def all_unique(lst):
  return len(lst) == len(set(lst))

def txtInList(A):
    x=A.split(' ')
    y=[]
    for el in x:
        y.append(int(el))
    return y

T=int(input("Enter the number of testcases: "))
l=[]
for i in range(T):
    N=int(input("Enter the number of integers in the list: "))
    A=input("Enter the values of elements in a list: ")
    a=txtInList(A)
    if (pos_check(a,0)) and all_unique(a):
        pass
        k=int(input("Enter the position of integer in the unsorted list: "))
        l.append((N,a,k))

        for el in l:
            n,a,k=el
            vr=a[k-1]
##    a.sort()

            for i in range(len(a)):
    # Find the minimum element in remaining 
    # unsorted array

            
                    min_idx = i
                    for j in range(i+1, len(a)):
                        if a[min_idx] > a[j]:
                            min_idx = j
   
    # Swap the found minimum element with 
    # the first element        
                        a[i], a[min_idx] = a[min_idx], a[i]
                
# Driver code to test above
##            for i in range(len(a)):
##               print("%d" %a[i],end=" ") 
    
        print(a.index(vr)+1)
    else:
        print (" There is negative integer in a list or/and repeated one. ")