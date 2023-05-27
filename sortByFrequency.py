class Solution(object):
    import collections
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c_dict = collections.Counter(s)
        sorted_c = sorted(c_dict, key=lambda x: (-c_dict[x], x))
        result = ''.join([char*c_dict[char] for char in sorted_c])
        return result