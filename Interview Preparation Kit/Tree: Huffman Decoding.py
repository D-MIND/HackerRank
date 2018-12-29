def decodeHuff(root, s):
	#Enter Your Code Here
    out = []
    temp = root
    for char in s:
        if char == "0":
            temp = temp.left
        else:
            temp = temp.right
        if temp.right == None and temp.left == None:
            out.append(temp.data)
            temp = root
    
    print("".join(out))
