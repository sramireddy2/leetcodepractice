class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
       
        for char in s:
            freq[ord(char) - ord('a')] += 1

        maxfreq = max(freq)

        if maxfreq > (len(s) + 1) // 2:
            return ""

        result = []

        while len(result) < len(s):
            maxindex = freq.index(max(freq))
            maxchar = chr(maxindex + ord('a'))
            result.append(maxchar)
            freq[maxindex] -= 1
            if freq[maxindex] == 0:
                continue

            temp = freq[maxindex]
            freq[maxindex] = float('-inf')
            maxind2 = freq.index(max(freq))
            maxchar2 = chr(maxind2 + ord('a'))
            result.append(maxchar2)
            freq[maxind2] -= 1
            freq[maxindex] = temp

        return "".join(result)
                    