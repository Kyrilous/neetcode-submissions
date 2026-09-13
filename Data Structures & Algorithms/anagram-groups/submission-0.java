class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
            HashMap<String, List<String>> map = new HashMap<>();

            for(String word : strs){
                int[] count = new int[26];

                // Count each other
                for(char c : word.toCharArray()){
                    count[c-'a']++;
                }

                StringBuilder key = new StringBuilder();

                for(int num : count){
                    key.append('#');
                    key.append(num);
                }

                String finalString = key.toString();

                if (!map.containsKey(finalString)) {
                    map.put(finalString, new ArrayList<>());
                }
                map.get(finalString).add(word);

            }
            return new ArrayList<>(map.values());



    }
}
