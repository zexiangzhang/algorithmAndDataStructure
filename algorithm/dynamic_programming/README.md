# dynamic programming (动态规划学习摘要)

	数组中的动态规划
	子数组、子序列中的动态规划
	背包问题
	矩阵中的动态规划
	动态规划与字符串匹配
	状态压缩动态规划
	区间中的动态规划
	树形动态规划
	数位动态规划

## 思想
	如果一个决策的前面若干步骤已经确定从而进入某种状态之后，
	后面的步骤从按照当前状态开始的最优解必然是整体（包括该状态的情况下）的最优解，则该问题满足最优原理
	换句话说，在求解（整体问题）的最优解的时候，后面的步骤选择只与当前状态有关，而与如何到达这个状态的步骤无关
	问题满足最优原理之后，我们可以把某个状态到目标的最优解记录下来，这样当通过不同的步骤走到相同的状态的时候，就不需要重复搜索了
	有一些问题还可以推出递推公式进行求解
	设计动态规划算法的时候，最核心的就是如何设计状态，使得状态的可能性尽量少，却又同时满足最优原理
	例如: 
	    如果状态被设置为所有到达该状态步骤组成，显然符合最优原理，但这就和原来的问题一样了，并没有让问题更简单
    动态规划方法安排求解顺序，对每个子问题只求解一次，并将结果保存下来
    如果随后再次需要此子问题的解，只需查找保存的结果，而不必重新计算
    因此动态规划算法是付出额外的内存空间来节省计算时间

###  相关问题
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[数组中的动态规划](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/dynamic_programming/dp_in_array/)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[子数组、子序列中的动态规划](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/dynamic_programming/dp_in_sub_array_or_sub_sequence/)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[背包问题](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/dynamic_programming/knapsack_problem/)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[矩阵中的动态规划](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/dynamic_programming/dp_in_matrix/)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[动态规划与字符串匹配](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/dynamic_programming/dp_in_string/)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[状态压缩的动态规划](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/dynamic_programming/dp_in_state_compression/)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[区间中的动态规划](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/dynamic_programming/dp_in_section/)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[树形dp](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/dynamic_programming/dp_in_tree/)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[数位dp](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/dynamic_programming/dp_in_number_index/)<br/></font>


## 与递归的区别
    动态规划是自底向上,一般都脱离了递归，由循环迭代完成计算
    递归是自顶向下，自身调用自身

# Update Continue......
