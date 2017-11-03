def Interpolation(arr,low,high,toFind):
  while(low<= high and toFind >= arr[low] and toFind <= arr[high]):
    pos = low + ( (toFind-arr[low])*(high-low) // (arr[high]-arr[low]) )
    
    if( arr[pos] == toFind):
      return pos
    elif(arr[pos] < toFind):
      low = pos+1
    else:
      high = pos-1
  return "Not found"

ar = [1,9,3,5,4,2,6,8,7] #Input list
to_search = 6 #Element to find
L = 0 #Lower index of input
H = len(ar) -1 #Highest index of list

print(Interpolation( sorted(ar) , L , H , to_search ))
