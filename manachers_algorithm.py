from itertools import islice


class Solution:

    def longest_palindrome(self, s: str) -> str:
        """
        search outwards from each character using manacher's algorithm
        """

        if len(s) < 2:
            return s

        processed_string = '#'.join('^{}S'.format(s))
        length = len(processed_string)
        lps = [0] * length
        center = right = max_lps_length = max_lps_position = 0

        for offset, _ in islice(enumerate(processed_string), 1, length - 1):

            # check if within previous range of previous largest palindrome
            if offset < right:
                # left|mirror = 2 * center - offset
                lps[offset] = min(lps[2 * center - offset], right - offset)

            # check if within range and if so, expand from current character to left and right and compare them
            while (offset + lps[offset] + 1 < length and offset - lps[offset] - 1 > 0 and processed_string[
                (offset + lps[offset] + 1)] == processed_string[
                       (offset - lps[offset] - 1)]):
                lps[offset] += 1

            if lps[offset] > max_lps_length:
                max_lps_length = lps[offset]
                max_lps_position = offset

            if offset + lps[offset] > right:
                center = offset
                right = offset + lps[offset]

        start = (max_lps_position - max_lps_length) // 2
        end = start + max_lps_length - 1
        return s[start:end + 1]


s1 = Solution()
print(s1.longestPalindrome("SQQSYYSQQS"))
