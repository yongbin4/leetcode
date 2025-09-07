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
        max_length = max(len(version1_list), len(version2_list))
        if len(version1_list) > len(version2_list):
            diff = len(version1_list) - len(version2_list)
            for i in range(diff):
                version2_list.append("0")
        else:
            diff = len(version2_list) - len(version1_list)
            for i in range(diff):
                version1_list.append("0")
                
        for i in range(max_length):
            if int(version1_list[i]) > int(version2_list[i]):
                return 1
            elif int(version2_list[i]) > int(version1_list[i]):
                return -1
            elif int(version2_list[i]) == int(version1_list[i]):
                print(int(version2_list[i]) == int(version1_list[i]))
                continue
        return 0