class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        # find integeters separated by dots so 1.2 has two part 1 and 2 1.001 | 1 and 1
        version1_list = version1.split(".")
        version2_list = version2.split(".")
        
        min_length = min(len(version1_list), len(version2_list))
                
        for i in range(min_length):
            if int(version1_list[i]) > int(version2_list[i]):
                return 1
            elif int(version2_list[i]) > int(version1_list[i]):
                return -1

        if len(version1_list) > len(version2_list):
            for i in range(min_length, len(version1_list)):
                if int(version1_list[i]) > 0:
                    return 1
        else:
            for i in range(min_length, len(version2_list)):
                if int(version2_list[i]) > 0:
                    return -1

        return 0