import json
import unittest

class TestClass(unittest.TestCase):
	def test1(self):
		self.assertEqual(func("input2.json"),True)
	def test2(self):
		self.assertEqual(func("input3.json"),False)

def place(data,row,colm):
  for r in range(row):
      if(data[r]==colm):
        return False
      elif(abs(data[r]-colm)==abs(r-row)):
        return False
  return True

def queen(data,row):
   for colm in range(8):
          if place(data,row,colm):
             data[row]= colm
             if row==7:
                 return True
             else:
                  if(queen(data,row+1)):
                     return True
                  else:
                       data[row]=-1

   if(colm==8):
          return False

def printboard(data):
	board=[['_']*8 for _ in range(8)]
	for i in range(8):
		board[i][data[i]]="Q"
	for i in range(8):
		for j in range(8):
			print board[i][j]+" ",
		print ""
	print ""

def func(filename):
   with open(filename) as f:
     pos=json.load(f)
 
     data=[-1]*8
     pos=pos['start']
     if(pos>0 and pos<8):
        data[0]=pos

        if(queen(data,1)):
           printboard(data)
           return True
        else:
            print "incorrect configuration"
            return false
     else:
        print "Incorrect"
        return False

func("input1.json")
unittest.main()
