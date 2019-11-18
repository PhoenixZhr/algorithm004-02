"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*2 for i in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        # 无状态 a[i] = a[i - 1] + nums[i]
        # a[i][0,1] 0: 不偷，1: 偷
        # a[i][0] = max(a[i - 1][0], a[i - 1][1]) 当前房子不偷，则为之前的值，之前的值包含
        # 了偷与不偷两种情况
        # a[i][1] = a[i - 1][0] + nums[i] 当前房子偷，则为前一个不偷的值加当前值
        for i in range(n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[n - 1][0], dp[n - 1][1])

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[n - 1]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[n - 1]
        
    # 国际站极简写法
    # f(0) = nums[0]
    # f(1) = max(num[0], num[1])
    # f(k) = max( f(k-2) + nums[k], f(k-1) )
    def rob(self, nums):
        
        last, now = 0, 0
        
        for i in nums: last, now = now, max(last + i, now)
                
        return now
            