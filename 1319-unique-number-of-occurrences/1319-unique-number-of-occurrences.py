class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence = {}

        for num in arr:
            if num in occurrence:
                occurrence[num] += 1
            else:
                occurrence[num] = 1    
        
        occurrence_list = []

        for i in occurrence:
            occurrence_list.append(occurrence[i])

        if len(occurrence_list) == len(set(occurrence_list)):
            return True
        else:
            return False