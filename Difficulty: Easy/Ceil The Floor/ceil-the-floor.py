#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        ceil = float("inf")
        floor = float("-inf")
        
        for val in arr:
            if val < x:
                floor = max(floor, val)
            elif val > x:
                ceil = min(ceil, val)
            else:
                floor = val
                ceil = val
        
        if ceil == float("inf"):
            ceil = -1
        if floor == float("-inf"):
            floor = -1
        return [floor, ceil]
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends