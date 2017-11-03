def sublist(to_search,to_find):
  small = len(to_find)-1
  big = len(to_search)-1
  i=0
  index = None
  while( i <= big-small ):
    j = 0
    while(j  <= small ):
      if(to_search[j+i] == to_find[j]):
        j+=1
      else:
        i+=1 
        break
      if(j==small+1):
        index = i
        return index
  return index

list_to_find = [3,4,5]
list_from_find =[1,2,3,4,5,6] 

start = sublist( list_from_find,list_to_find )

if(start == None):
  print("not found")
else:
  print("Start : "+str(start)+" , End : "+str(start+len(list_to_find)-1))
