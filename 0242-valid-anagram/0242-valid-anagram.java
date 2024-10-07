class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap <Character, Integer> store = new HashMap<>();
        if (s.length() != t.length()) return false;
        
        for (char k : s.toCharArray()) {
            store.put(k, store.getOrDefault(k, 0) + 1);
        }

        for (char k : t.toCharArray()) {
            System.out.println(store.get(k));
            if (!store.containsKey(k) || store.get(k) == 0) {
                return false;
            } else {
                store.put(k, store.get(k) - 1);
            }
        }
        // for (char k : store.keySet()) {
        //     System.out.println("key " + k + " value " + store.get(k));
        // }

        return true;
    }
}