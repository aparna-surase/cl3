from bitstring import BitArray
from flask import Flask
from flask import render_template
from flask import request
app=Flask(__name__)

def booth(m,r,x,y):
	total_length=x+y+1
	mA=BitArray(int=m,length=total_length)
	print mA
	A=mA<<(y+1)
	print A
	mA1=BitArray(int=-m,length=total_length)
	print mA1
	S=mA1<<(y+1)
	print S
	P1=BitArray(int=r,length=y)
	P1.prepend(BitArray(int=0,length=x))
	P=P1<<(1)
	print "A:",A.bin
	print "S:",S.bin
	
	for i in range(1,y+1):
		if P[-2:]=="0b01":
			P = BitArray(int=P.int+A.int,length=total_length)
		if P[-2:]=="0b10":
			P = BitArray(int=P.int+S.int,length=total_length)
       		P=BitArray(int=(P.int>>(1)),length=total_length)
	P=P[:-1]
	print "P:",P.bin
	return P.bin,P.int


@app.route('/')
def f():
	return render_template("a3.html")

@app.route('/',methods=['POST'])
def g():
	text1=int(request.form['text1'])
	text2=int(request.form['text2'])
	n,m=booth(text1,text2,8,8)
	return "Answer in binary"+str(n)+"</br>answer"+str(m)+"</br>"

if __name__=='__main__':
   app.run('localhost',debug='True')
