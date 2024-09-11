class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for i in range(len(gain)):
            newAlt = altitudes[i] + gain[i] 
            altitudes.append(newAlt)
        highest = max(altitudes)
        return highest