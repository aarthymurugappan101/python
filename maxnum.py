def findLargest(numArr):
    largest = numArr[0]
    for num in numArr:
        if(num >largest):
            largest = num
            return largest

        
numArr =[2,5,3]
print(findLargest(numArr))



    