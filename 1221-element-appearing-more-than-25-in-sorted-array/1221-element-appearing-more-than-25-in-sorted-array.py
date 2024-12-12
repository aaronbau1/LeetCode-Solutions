class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # store = {}
        # if len(arr) == 1:
        #     return arr[0]
        # for num in arr:
        #     if store.get(num):
        #         store[num] += 1
        #         if store[num] > len(arr) / 4:
        #             return num
        #     else:
        #         store[num] = 1
        if len(arr) == 1:
            return arr[0]
        local_count = 1
        local_int = arr[0]
        for i in range(1, len(arr)):
            if arr[i] != local_int:
                if local_count > len(arr) / 4:
                    return local_int
                local_count = 1
                local_int = arr[i]
            else:
                local_count += 1
        return local_int