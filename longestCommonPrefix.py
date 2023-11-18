class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs)
        common = []

        first = sorted_strs[0]
        last = sorted_strs[len(sorted_strs)-1]

        for i in range(len(first)):
            if (first[i] != last[i]):
                break
            common.append(first[i])

        result = "".join(str(element) for element in common)
        return result


        