class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1 = {}
        count2 = {}
        for s in s1:
            count1[s] = count1.get(s, 0) + 1
        l = 0
        for r in range(len(s2)):
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
            if count1== count2:
                return True
        return False
