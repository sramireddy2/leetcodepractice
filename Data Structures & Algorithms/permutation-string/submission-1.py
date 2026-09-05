class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): #not valid
            return False

        s1count, s2count = [0] * 26, [0] * 26 # make buckets and count characters of the window
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1

        matches = 0 #count matches in the first window if all 26 match then true
        for i in range(26):
            matches += (1 if s1count[i] == s2count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)): #sliding window
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a') # add right character
            s2count[index] += 1
            if s1count[index] == s2count[index]: #update match counter
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a') #remove left
            s2count[index] -= 1
            if s1count[index] == s2count[index]: #update match counter
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            l += 1 #move left pointer
        return matches == 26 #check last window

