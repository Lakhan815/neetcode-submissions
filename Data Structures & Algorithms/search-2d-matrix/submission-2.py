'''
1. Do a binary search on the first int of every array
2. Go until you find an array that's first int is <= target and the following int is > int
    2.1. Edge case: <= target and follwing is null
3. After finding the array, do BS on that array to find the target
4. If target exists, return true else return false
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        topR=0
        bottomR=len(matrix)-1
        while(topR<=bottomR):
            midR = (topR+bottomR)//2
            if(matrix[midR][0]<=target):
                left=0
                right=len(matrix[midR])-1
                while(left<=right):
                    mid=(right+left)//2
                    if(matrix[midR][mid]==target):
                        return True
                    elif(matrix[midR][mid]<target):
                        left=mid+1
                    else:
                        right=mid-1
                    topR=midR+1
            elif(matrix[midR][0]>target):
                bottomR=midR-1
                continue
        return False

