arr = [1,3,4,5,6,7]
start = 0
end = len(arr)-1
while(start<end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start+=1
    end-=1
print(arr)