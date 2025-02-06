class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        low = 0
        high = len(arr) - 1
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] <= k:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends