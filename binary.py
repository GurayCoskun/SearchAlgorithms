
def binarySearch (arr, low, high, x): 
	if high >= low: 
		
		mid = low + (high - low) // 2
		if arr[mid] == x: 
			return mid 
		elif arr[mid] > x: 
			return binarySearch(arr, low, mid-1, x) 
		else: 
			return binarySearch(arr, mid + 1, high, x) 

	else: 
		return -1


if __name__ == '__main__':
	arr=[1,2,3,4,5,6,7,8,9]
	x=6
	result = binarySearch(arr,0, len(arr)-1,x)
	if(result==-1):
		print("Element is not present in array")
	else:
		print("Element is present at index %d" % result)
