def binary(arr2,tofind2,low,high):
  mid2 = (low+high)//2
  if(low > high):
    return "not found"
  elif(arr2[mid2] == tofind2):
    return mid2
  elif(arr2[mid2] < tofind2):
    return binary(arr2 , tofind2 , mid2+1 , high)
  else:
    return binary(arr2 , tofind2 , low , high-1)

def exponential( arr, tofind ):
  bound = 1
  size = len(arr)-1
  while(bound < size and arr[bound] < tofind):
    bound *= 2
  low1 = bound//2
  if(bound > size and bound //2 < size):
    high = size
    return binary(arr,tofind , low1 , high)
  elif(bound <=size):
    return binary(arr,tofind , bound//2 , bound)
  else:
    return "not found"
    
x=[0,1,2,3,4,5,6,7,8,9]
y = x
print(exponential(y,3))
