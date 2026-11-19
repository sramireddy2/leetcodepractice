
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        required = Counter(t)
        window = {}
        formed = 0
        needed = len(required)

        left = 0
        best_start = 0
        best_length = len(s) + 1

        for right, char in enumerate(s):
            # Only required characters affect validity.
            if char in required:
                window[char] = window.get(char, 0) + 1

                # Count a requirement only when we first meet it.
                if window[char] == required[char]:
                    formed += 1

            # A valid window may contain removable extra characters.
            while formed == needed:
                current_length = right - left + 1
                if current_length < best_length:
                    best_start = left
                    best_length = current_length

                outgoing = s[left]
                if outgoing in required:
                    window[outgoing] -= 1

                    # Removing an extra occurrence does not break validity.
                    if window[outgoing] < required[outgoing]:
                        formed -= 1

                left += 1

        if best_length == len(s) + 1:
            return ""

        # Slice once, rather than copying every improving candidate.
        return s[best_start:best_start + best_length]
