class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        max = 0
        for i in range(len(gain)):
            alt += gain[i]
            if alt > max: max = alt
        return max