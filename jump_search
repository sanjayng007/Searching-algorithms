import math
def jump_search(arr,i,jump_dist,to_search):
  if(i> len(arr)-1):
    return "not found"
  elif(arr[i] == to_search):
    return i
  elif(arr[i] < to_search):
    return jump_search(arr, i+jump_dist , jump_dist , to_search)
  else:
    for j in range(i-jump_dist, i):
      if(arr[j] == to_search):
        return j
ar=[1,2,3,4,5,6,7,8,9,10]
search = 8
n = len(ar)
m = int(math.sqrt(n))
print(jump_search(ar,0,4,search))

"""
  m: optimal step size 
  n : total number of elements
  m = sqrt(n)
"""
