class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_freq = {}
        window_freq = {}

        # frequency of s1
        for ch in s1:
            s1_freq[ch] = s1_freq.get(ch, 0) + 1

        # first window
        for i in range(len(s1)):
            window_freq[s2[i]] = window_freq.get(s2[i], 0) + 1

        if s1_freq == window_freq:
            return True

        left = 0

        for right in range(len(s1), len(s2)):

            # add new character
            window_freq[s2[right]] = window_freq.get(s2[right], 0) + 1

            # remove old character
            window_freq[s2[left]] -= 1

            if window_freq[s2[left]] == 0:
                del window_freq[s2[left]]

            left += 1

            if window_freq == s1_freq:
                return True

        return False


obj = Solution()
print(obj.checkInclusion("abc", "lecabee"))