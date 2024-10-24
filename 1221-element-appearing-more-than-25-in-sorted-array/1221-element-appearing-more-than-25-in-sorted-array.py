class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        max = arr[0]
        freq = 1
        local_max = arr[0]
        local_freq = 1
        for i in range(1, len(arr)):
            # print(f"el {arr[i]} prev el {arr[i-1]}")
            if arr[i] == arr[i-1]:
                local_freq += 1
                if local_freq > freq:
                    freq = local_freq
                    max = local_max
                    # print(f"local_freq {local_freq} max {local_max}")
            else:
                local_max = arr[i]
                local_freq = 1
        return max
            
