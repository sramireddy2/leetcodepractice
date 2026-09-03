class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            buckets = [0] * 26
            for c in s:
                buckets[ord(c) - ord('a')] += 1
            res[tuple(buckets)].append(s)

        return list(res.values())