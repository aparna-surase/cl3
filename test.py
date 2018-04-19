import math
try:
   input = raw_input
except NameError:
   pass
try:
   chr = unichr
except NameError:
   pass
p=int(input('Enter prime p: '))
q=int(input('Enter prime q: '))
print("Choosen primes:\np=" + str(p) + ", q=" + str(q) + "\n")
n=p*q
print("n = p * q = " + str(n) + "\n")
phi=(p-1)*(q-1)
print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l
print("Choose an e from a below coprimes array:\n")
print(str(coprimes(phi)) + "\n")
e=int(input())
d=modinv(e,phi)
print("\nYour public key is a pair of numbers (e=" + str(e) + ", n=" + str(n) + ").\n")
print("Your private key is a pair of numbers (d=" + str(d) + ", n=" + str(n) + ").\n")
	
def encrypt_block(m):
    #c = modinv(m**e, n)
    c = (pow(m,e))%n
    print "C: ",c
    if c == None: print('No modular multiplicative inverse for block ' + str(m) + '.')
    return c
def decrypt_block(c):
    #m = modinv(c**d, n)
    m = (pow(c,d))%n
    if m == None: print('No modular multiplicative inverse for block ' + str(c) + '.')
    return m
def encrypt_string(s):
    st = ""
    for x in list(s):
	print "1: ",x
	a = ord(x)
	if a>96:
		a-=71
	else:
		a-=65
        a = encrypt_block(a)
	print "3: ",a
	a = chr(a)
	print "4: ",a
	st = st+a
    print "My string: ",st
    return st
    #return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def decrypt_string(s):
    print s
    st = ""
    for x in list(s):
	print "1: ",x #;
	a = ord(x)
	print "2: ",a	#59
        a = decrypt_block(a)
	if 0<=a<=25:
		a+=65
	else:
		a+=71
	print "3: ",a	
	a = chr(a)
	print "4: ",a
	st = st+a
    return st
    #return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
s = input("Enter a message to encrypt: ")
#print("\nPlain message: " + s + "\n")
enc = encrypt_string(s)
print enc
#print("Encrypted message: " + enc + "\n")
dec = decrypt_string(enc)
print "Decrypted String: "
print dec
#print("Decrypted message: " + dec + "\n")
