class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        have = 0
        needCount = len(need)

        res = [-1, -1]
        resLen = float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # We just satisfied this character's required amount
            if c in need and window[c] == need[c]:
                have += 1

            # Window currently contains everything we need
            while have == needCount:
                # Save smallest window
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Remove leftmost character
                leftChar = s[l]
                window[leftChar] -= 1

                # If removing it makes us fall below what's required,
                # the window is no longer valid
                if leftChar in need and window[leftChar] < need[leftChar]:
                    have -= 1

                l += 1

        l, r = res

        if resLen == float("inf"):
            return ""

        return s[l:r + 1]