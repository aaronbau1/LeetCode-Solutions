class Solution {
    public String largestOddNumber(String num) {
        String result = "";
        if (Integer.valueOf(num.charAt(num.length() - 1)) % 2 == 1) return num;
        for (int i = num.length() - 1; i >= 0; i--) {
            String string_temp = String.valueOf(num.charAt(i));
            int int_temp = Integer.parseInt(string_temp);
            if (int_temp % 2 == 0) {
                result = num.substring(0, i);
            } else {
                return result;
            }
        }
        return result;
    }
}