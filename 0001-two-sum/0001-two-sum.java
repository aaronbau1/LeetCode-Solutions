class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> store = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (store.containsKey(diff)) {
                return new int[] {i, store.get(diff)};
            } else {
                store.put(nums[i], i);
            }
        }
        return new int[] {0,0};
    }
}