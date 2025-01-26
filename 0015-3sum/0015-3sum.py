class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tripStore = set()
        for i in range(len(nums)):
            psum_store = set()
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                if target in psum_store:
                    temp = [nums[i], nums[j], target]
                    temp.sort()
                    tripStore.add(tuple(temp))
                else:
                    psum_store.add(nums[j])
        return list(tripStore)
        # st = set()

        # for i in range(n):
        #     hashset = set()
        #     for j in range(i + 1, n):
        #         # Calculate the 3rd element:
        #         third = -(arr[i] + arr[j])

        #         # Find the element in the set:
        #         if third in hashset:
        #             temp = [arr[i], arr[j], third]
        #             temp.sort()
        #             st.add(tuple(temp))
        #         hashset.add(arr[j])

        # # store the set in the answer:
        # ans = list(st)
        # return ans