import socket
import sys

def chunks(l,n):
	return [l[i:i+n] for i in range (0, len(l),n)]

def rol(n,b):
	return ((n<<b)|(n>>(32-b))) & 0xffffffff

def sha1(data):

	bytes = ""
	#h0 = 0x67452301
	#h1 = 0xEFCDAB89
	#h2 = 0x98BADCFE
	#h3 = 0x10325476
	h0 = 0x01234567
	h1 = 0x89ABCDEF
	h2 = 0xFEDCBA98
	h3 = 0x76543210
	h4 = 0xC3D2E1F0
	
	for n in range(len(data)):
		bytes+='{0:08b}'.format(ord(data[n]))
	
	bits = bytes+"1"
	pbits = bits

	while len(pbits)%512 != 448:
		pbits+="0"

	pbits+='{0:64}'.format(len(bits)-1)

	for c in chunks(pbits,512):
		words = chunks(c,32)
		w = [0]*80
		for n in range(0,14):
				w[n] = int(words[n],2)

		w[14] = 0
		w[15] = 0
		#print w[14]
		#print w[15]
		#print "----------------------------------------"
		for i in range(16,80):
			w[i] = rol((w[i-3]^w[i-8]^w[i-14]^w[i-16]),1)
			#print w[i]
		a = h0
		b = h1
		c = h2
		d = h3
		e = h4

		for i in range(0,80):
			if 0 <= i <= 19:
				f = (b & c) | ((~b) & d)
				k = 0x5A927999
			elif 20<=i<=39:
				f = b ^ c ^ d
				k = 0x6ED9EBA1
			elif 40<= i <= 60:
				f = (b & c) | (b & d) | (c & d)
				k = 0x9F1BBCDC
			elif 60<= i <= 80:
				f = b ^ c ^ d
				k = 0xCA62C1D6
			
			temp  = rol(a,5) + f + e + k + w[i] & 0xffffffff

			b = a
			a = temp
			e = d
			d = c
			c = rol(b,30)

		h0 = h0 + a & 0xffffffff
		h1 = h1 + b & 0xffffffff
		h2 = h2 + c & 0xffffffff
		h3 = h3 + d & 0xffffffff
		h4 = h4 + e & 0xffffffff

	return '%08x%08x%08x%08x%08x' % (h0,h1,h2,h3,h4)
		

if __name__ == "__main__":
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address = ('localhost',1260)
	sock.connect(server_address)
	try:
		message = raw_input("Enter your message: ")
		#message = "helloeveryoneIamSagarDeshpande"
		sock.send(message)
		digest = sha1(message)
		print "Digest: "+digest
		sock.send(digest)
	finally:
		print "Closing socket"
		sock.close()
		
