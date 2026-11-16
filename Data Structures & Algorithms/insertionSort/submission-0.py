class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []

        res = [pairs[:]]             
        index = 1
        while index <= len(pairs) - 1:
            j = index
            # keep moving the item left while it's smaller than its neighbor
            while j > 0 and pairs[j].key < pairs[j - 1].key:
                temp = pairs[j]
                pairs[j] = pairs[j - 1]
                pairs[j - 1] = temp
                j -= 1
            res.append(pairs[:])      
            index += 1

        return res