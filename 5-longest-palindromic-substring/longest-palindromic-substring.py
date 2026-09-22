class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left+1, right-1 are the bounds of the palindrome
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd-length palindrome (center at i)
            l1, r1 = expand(i, i)
            if r1 - l1 > end - start:
                start, end = l1, r1

            # Even-length palindrome (center between i, i+1)
            l2, r2 = expand(i, i + 1)
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]