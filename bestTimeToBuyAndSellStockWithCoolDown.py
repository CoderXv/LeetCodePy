# --- Introduction ---
"""
	- Say you have an array for which the ith element is the prices of a given stock on 
	day i.Design an algorithm to find the maximum profit. You may complete as many 
	transactions as you like(ie, buy one and sell one share of the stock multiple times)
	with the following restrictions:
	- You may not engage in multiple transactions at the same time(ie, you must sell 
	the stock before you buy again).
	- After you sell your stock, you cannot buy stock on next day.(ie, cooldown 1 day)
"""


# --- Solution ---
"""
	  本题的限制是有个cooldown，本质就是买与卖之间的限制。对于某一天而言，股票有三种状态
	buy sell cooldown sell 和 cooldown 我们可以合并成为一种状态，因为我们手中最终都没有
	股票，最终需要的结果是sell，即手中股票获得的最大利润。所以我们可以用两个DP数组分别
	记录当前持股跟未持股的状态。然后根据题目中的限制条件，理清两个DP数组的表达式。
	  这里我们引进两个个数组sellDp和buyDp，用来记录当前持股和未持股的状态。
	  
	  对于当天最终未持股的状态，最终最大利润有两种可能，一是今天没动作跟昨天未持股的状态
	一样，二是昨天持股了，今天卖了。所以我们只要取这两者之间的最大值即可：   
	   - sellDp[i] = max(sellDp[i-1], buyDp[i-1]+prices[i])
	  
	  对于当天最终持股的状态，最终最大利润有两种可能，一是今天没动作跟昨天持股状态一样，
	二是前天还没持股，今天买了股票，这里因为cooldown的原因，所以今天买股票要追溯到前天的
	状态。我们只要取这两者之间的最大值即可，表达式如下：
	   - buyDp[i] = max(buyDp[i-1], sellDp[i-2]-prices[i])
	  
	  最终我们要求的结果是：
	  - sellDp[n-1]	表示最后一天结束时手里没有股票时的累计的最大利润  
"""

# --- Solution ---
class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int 
		"""
		if prices == None or len(prices) == 1:
			return 0
		
		sellDp = [0]*len(prices)
		buyDp = [0]*len(prices)
		
		# init the list 
		sellDp[0] = 0
		buyDp[0] = -prices[0]
		
		for i in range(1, len(prices)):
			sellDp[i] = max(sellDp[i-1], buyDp[i-1]+prices[i])
			if i >= 2:
				buyDp[i] = max(buyDp[i-1], sellDp[i-2]-prices[i])
			else:
				buyDp[i] = max(buyDp[i-1], -prices[i])
		
		return sellDp[len(prices)-1] 
		
# --- Optimised Version ---
class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int 
		"""
		if prices == None or len(prices) == 1:
			return 0
		
		sell = 0
		pre_sell = 0
		buyDp = -prices[0]
		
		for i in range(1, len(prices)):
			sell = max(sell, buyDp + prices[i])
			if i >= 2:
				buyDp = max(buyDp, pre_sell - prices[i])
			else:
				buyDp = max(buyDp, prices[i])
		
		return sell
		
		
	
	
	
	
	
	
	
	
	