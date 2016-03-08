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
	  ������������и�cooldown�����ʾ���������֮������ơ�����ĳһ����ԣ���Ʊ������״̬
	buy sell cooldown sell �� cooldown ���ǿ��Ժϲ���Ϊһ��״̬����Ϊ�����������ն�û��
	��Ʊ��������Ҫ�Ľ����sell�������й�Ʊ��õ���������������ǿ���������DP����ֱ�
	��¼��ǰ�ֹɸ�δ�ֹɵ�״̬��Ȼ�������Ŀ�е�������������������DP����ı��ʽ��
	  ����������������������sellDp��buyDp��������¼��ǰ�ֹɺ�δ�ֹɵ�״̬��
	  
	  ���ڵ�������δ�ֹɵ�״̬������������������ֿ��ܣ�һ�ǽ���û����������δ�ֹɵ�״̬
	һ������������ֹ��ˣ��������ˡ���������ֻҪȡ������֮������ֵ���ɣ�   
	   - sellDp[i] = max(sellDp[i-1], buyDp[i-1]+prices[i])
	  
	  ���ڵ������ճֹɵ�״̬������������������ֿ��ܣ�һ�ǽ���û����������ֹ�״̬һ����
	����ǰ�컹û�ֹɣ��������˹�Ʊ��������Ϊcooldown��ԭ�����Խ������ƱҪ׷�ݵ�ǰ���
	״̬������ֻҪȡ������֮������ֵ���ɣ����ʽ���£�
	   - buyDp[i] = max(buyDp[i-1], sellDp[i-2]-prices[i])
	  
	  ��������Ҫ��Ľ���ǣ�
	  - sellDp[n-1]	��ʾ���һ�����ʱ����û�й�Ʊʱ���ۼƵ��������  
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
		
		
	
	
	
	
	
	
	
	
	