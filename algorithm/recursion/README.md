# recursion (递归相关)

###  递归的核心思想
     递归的核心思想是分解。把一个很复杂的问题使用同一个策略将其分解为较简单的问题，如果这个的问题仍然不能解决则再次分解，直到问题能被直接处理为止。
     比如求 1+1/2+1/3+...+1/n的和，如果按照正常的思维，就会使用一个循环，把所有的表示式的值加起来，这是最直接的办法。如果使用递归的思维，过程就是这样的，要求1+1/2+1/3+...+1/n的值，可以先求s1=1+1/2+1/3+...+1/(n-1)的值，再用s1加上1/n就是所求的值，而求s1的过程又可以使用上面的分解策略继续分解，最终分解到求1+1/2的值，而这个问题简单到可以直接解决，自此问题得到解决。
     递归强调的分治的策略，再举个例子，有一种排序算法叫归并排序，其思想是这样的：要对一个无序的数组进行排序，可以将这个数组分解为2个小数组，然后对这两个数组分别排序，再把排好序的两个数组合并。而这一过程中只有“对两个数组分别排序”是无法直接解决的，但是这个问题可以使用上面的策略进行再次的分解，最后这个问题就被分解到对2个元素的数组进行排序，而这个问题简单到可以直接处理。
     上面提到的分解的策略，或者说算法，抽象出来就是函数，因为在这个过程中我们要不同的使用这个策略来不断的分解问题，所以代码上就体现为这个函数会不断的调用自身。还有一点，并不是所有的递归都是可以实现的，或者说有意义的。如果在分解的过程中，问题最终不能分解到一个可以直接解决的问题，则这个过程是没有意义，也就是无限的循环。

### 递归与枚举的区别：
	枚举的子问题之间的平等的, 横向的, 相互独立的
	递归将问题划分为逐级， 纵向的， 相互关联的

### 递归与迭代的区别：
	递归是越来越接近最终值，范围越来越小，并且返回值参与前一个调用的运算
	迭代可以无止境。与前一个调用之间没有运算操作。平级向下执行(循环的实现)

### 简单实例
	阶乘
	def factorial(n) {
		if (n==1) {
			return 1;
		}
		return n * factorial(n-1)
	}

###  相关问题
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[字符串解码](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/recursion/codes/decode_string.py)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[数字三角形](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/recursion/codes/digital_triangle.py)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[翻转二叉树](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/recursion/codes/invert_binary_tree.py)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[汉诺塔](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/recursion/codes/hanoi.py)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[相同的树](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/recursion/codes/same_tree.py)<br/></font>
<font size = 3>&nbsp;&nbsp;&nbsp;&nbsp;[对称二叉树](https://github.com/zexiangzhang/algorithmAndDataStructure/tree/master/algorithm/recursion/codes/symmetric_tree.py)<br/></font>

# Update Continue......
