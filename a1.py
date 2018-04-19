import unittest
def binary_search(arr,size,key):
 low=0
 high=size-1
 mid=int((low+high)/2)

 while low<=high:
   temp=0
   if key == arr[mid]:
     print "element",key,"found at",mid+1,"\n"
     return mid+1
     temp=1
     break
 
   elif key>arr[mid]:
     low= mid+1
     mid=int((low+high)/2)

   else:
     high=mid-1
     mid=int((low+high)/2)

 
 if temp==0:
  print "Not found"
  return 0

class mytest(unittest.TestCase):
   def test_positive(self):
     self.assertEqual(binary_search([10,20,30,40,50],5,40),4)
   def test_negative(self):
     self.assertEqual(binary_search([10,20,30,40,50],5,4),0)

arr=[]
size=int(input("how many elements you want to enter:"))
for i in range(0,size):
  print "enter element:"
  arr.append(input())

print "entered array elemt"
print(arr);
print "-------testing................"
arr.sort()
print "sorted array:"
print(arr)

key=int(input("enter element to be searched:"))
position=binary_search(arr,size,key)
unittest.main() 



