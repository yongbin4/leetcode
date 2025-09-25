from collections import OrderedDict
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        dic = OrderedDict()
        for key in arr2:
            dic[key] = []
        
        remainder = []
        for key in arr1:
            # key is in arr1
            if key in dic.keys():
                dic[key].append(key)
            # key is not in arr1
            else:
                remainder.append(key)
        result = []
        for key in dic.keys():
            result += dic[key]
        remainder.sort()
        result = result + remainder
        return result