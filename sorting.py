def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                
    return arr
def selection(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[min]<arr[j]:
                min=j
        arr[j],arr[min]=arr[min],arr[j]
    return arr
        
    
    
    
    
    
    
    
    
    

arr=list(map(int,input().split()))
print(bubble(arr))
print(selection(arr))