import threading
import xml.etree.ElementTree as et
import unittest


class TestClass(unittest.TestCase):
	def test1(self):
		self.assertEqual(func("input.xml"),True)
	def test2(self):
		self.assertEqual(func("lolnoob"),False)



class Sort:
	arr=[]
	def __init__(self,a):
		self.arr=a

	def Partition(self,p,q):
		pivot=self.arr[p]
		i=p
		for j in range(p+1,q+1):
			if(self.arr[j]<pivot):
				i+=1
				temp=self.arr[i]
				self.arr[i]=self.arr[j]
				self.arr[j]=temp
		temp=self.arr[i]
		self.arr[i]=self.arr[p]
		self.arr[p]=temp	
		return i
	
	def QuickSort(self,p,q):
		if(p<q):
			r=self.Partition(p,q)
			t1=threading.Thread(target=self.QuickSort,args=(p,r-1))
			t2=threading.Thread(target=self.QuickSort,args=(r+1,q))
			t1.start()
			t2.start()
			t1.join()
			print t1.getName()
			t2.join()
			print t2.getName()
		return self.arr


def func(filename):
	try:
		name=filename.split(".")
		if(name[1]=='xml'):
			tree=et.parse(filename)
			root=tree.getroot()
			a=map(int,root.text.split())
			obj=Sort(a)
			a=obj.QuickSort(0,(len(a)-1))
			print "Sorted Array:",a
			return True
	except Exception as e:
		#raise e
		print "ERROR BRUH"
	return False

if __name__ == '__main__':
	func("input.xml")

unittest.main()
