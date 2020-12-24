def search(arr, n, x): 

	for i in range(0, n): 
		if (arr[i] == x): 
			return i 
	return -1

if __name__ == '__main__':
	arr=[6, 15, 3, 22, 8, 93] 
	x = 8
	n=len(arr)
	result =search(arr,n,x)
	if(result==-1):
		print("Element is not present in array")
	else:
		print("Element is present at index : ", result)

