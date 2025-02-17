class Solution:
    def countFreq(self, arr, target):
        low = 0
        high = len(arr) - 1
        floor = -1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > target:
                high = mid - 1
            elif arr[mid] == target:
                floor = mid
                high = mid - 1
            else:
                low = mid + 1
        
        if floor == -1:
            return 0
        
        low = 0
        high = len(arr) - 1
        ceil = -1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] == target:
                ceil = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ceil - floor + 1
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends