arr = [1,2,3,4,5]
to_find = 5
for i in range(len(arr)):
  if(arr[i] == to_find):
    print("Found at index :" + str(i))
    break
