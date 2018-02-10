while True:
	print("Enter '0' for exit.")
	v1= input("Enter any character: ")
	if v1 == '0':
		break
	else:
		if((v1>='a' and v1<='z') or (v1>='A' and v1<='Z')):
			print(v1, "is an alphabet.\n")
		else:
			print(v1, "is not an alphabet.\n")
