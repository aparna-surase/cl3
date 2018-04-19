def cipher(ptext,key=None):
	ctext=""
	if key is not None:
		for symbol in ptext:
			if symbol.isalpha():
				num=ord(symbol)
				num+=key
				if symbol.isupper():
					if(num > ord('Z')):
						num -=26
					elif(num <ord('A')):
						num +=26
				elif symbol.islower():
					if(num > ord('z')):
						num -=26
					elif(num <ord('a')):
						num +=26
				ctext+=chr(num)

			else:
				ctext+=symbol
	else:
		arr="abcdefghijklmnopqrstuvwxyz"
		key="qwertyuiopasdfghjklzxcvbnm"
		for symbol in ptext:
			if symbol.isalpha():
				if symbol.islower():
					index=arr.find(symbol)
					ctext +=key[index]
				elif symbol.isupper():
					index=arr.find(symbol.lower())
					ctext +=key[index.upper()]
			else:
				ctext +=symbol
	return ctext

if __name__=='__main__':
	ptext=raw_input("Enter message for encryption ")
	ctext=""
	case=int(raw_input("\n1.caeser cipher\n2.monoalphabetic cipher\n\n Enter yoir choice:"))
	if case==1:
		key=int(raw_input("Enter key between [0-26]"))
		ctext=cipher(ptext,key)
		print "ciphertect:",ctext
	elif case==2:
		#key=raw_input("Enter key between [0-26]")
		ctext=cipher(ptext)
		print "ciphertect:",ctext
	else:
		print "Invalid choice"
		exit()
