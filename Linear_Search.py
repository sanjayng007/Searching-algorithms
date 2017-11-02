arr = [1,2,3,4,5]
to_find = 5
for i in arr:
  if(i == to_find):
    print("Found at index :" + str(arr.index(i)))
    break
