def binary(arr,to_find,low,high):
  mid = (high+low)//2
  if(high < low):
    return "not found"
  elif( arr[mid] == to_find ):
    return mid
  elif(arr[mid] > to_find):
    return binary(arr , to_find,low,mid-1)
  else:
    return binary(arr,to_find,mid+1,high)
    
arr = [1,2,3,4,5,6,7,8,9,10]
print(binary(arr,10,0,10))
print(binary(arr,11,0,10))
