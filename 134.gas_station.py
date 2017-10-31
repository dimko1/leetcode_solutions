# url: https://leetcode.com/problems/gas-station/description/
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station
# (i+1). You begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

# Note:
# The solution is guaranteed to be unique.


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        # check edge cases && cases when it is not enough gas
        if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost): return -1

        balance = 0
        position = 0

        for i in xrange(len(gas)):
            balance += gas[i] - cost[i]  # take all the gas from station and spend for next trip
            if balance < 0:  # we need more gas! (c) Starcraft Drones
                position = i + 1  # let's start on next point
                balance = 0
        return position

c = Solution()
# should not be able to complete circle
print c.canCompleteCircuit([4],[5])
# should be able to complete circle
print c.canCompleteCircuit([4, 4],[5, 1])
