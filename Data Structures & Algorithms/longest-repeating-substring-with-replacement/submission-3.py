class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        left = 0
        longest = 0
        alphabet_start = ord("A")

        for right, char in enumerate(s):
            counts[ord(char) - alphabet_start] += 1

            # Keep the most frequent character; replace the rest.
            # Recompute the true maximum after each left removal.
            while (right - left + 1) - max(counts) > k:
                counts[ord(s[left]) - alphabet_start] -= 1
                left += 1

            # The current window now requires at most k replacements.
            longest = max(longest, right - left + 1)

        return longest