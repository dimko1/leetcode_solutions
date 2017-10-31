# url = https://leetcode.com/problems/restore-ip-addresses/description/
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#
# Comments:
# Basically this solution can be resolved with using some DFS,
# however straight forward solution will have same speed + more clear to read


class Solution(object):
    def restoreIpAddresses(self, s):
        res = []

        def isValid(i):
            # check length
            if len(i) > 3 or len(i) == 0: return False
            # check value
            if int(i) > 255: return False
            # check double zero
            if i[0] == "0" and len(i) > 1: return False

            return True

        # generate parts
        for i in xrange(1, 4):
            for j in xrange(i + 1, i + 4):
                for k in xrange(j + 1, j + 4):
                    first, second, third, fourth = s[0:i], s[i:j], s[j:k], s[k:]
                    # validate
                    if isValid(first) and isValid(second) and isValid(third) and isValid(fourth):
                        res.append(first + '.' + second + '.' + third + '.' + fourth)
        return res


