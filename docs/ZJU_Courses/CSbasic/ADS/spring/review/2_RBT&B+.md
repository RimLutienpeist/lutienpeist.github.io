# REVIEW2 | Red Black Tree & B+ Tree

## 红黑树

> **代码小技巧**
>
> 让叶子节点的空儿子从指向null改成指向哨兵。
>
> 即，让每个leaf指向一个值特殊的虚拟节点，就不用每次访问儿子都需要if是不是null，方便访问左儿子和右儿子。
>
> 这个虚拟节点被叫做 **哨兵/外部节点**。

### 性质

1. 每个节点要么红，要么黑
2. 根节点黑
3. 叶子节点黑，即哨兵是黑
4. 红节点儿子全黑
5. For each node, all simple paths from the node to descendant leaves contain the same number of **black** nodes.
   1. 是到哨兵，不是到叶子节点

### 黑高

即从该节点到哨兵的黑色节点数，不算自己和哨兵

#### 黑高定理

1. A red-black tree with N internal nodes has height at most 2ln(N +1).
   1. 
2. bh(Tree) $\textgreater$ h(Tree) / 2  
   1. root的黑高大于高度的一半
   2. 由性质四易得

### 操作

> RBT操作比较复杂，情况多，难记忆，多做题

看导图即可，不过得另外花时间看下原来的笔记，就看下这些操作是怎么推导出来的

## B+ Tree

### 定义

B+ 树是一种用树状形式维护有序数列比较信息的数据结构，其增改操作拥相对于二叉树结构更加稳定的对数时间复杂度，通常用于数据库和操作系统的文件系统中。

![image-20240421104117796](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240421104117796.png)

> 即，root不存在只有一个child的情况
>
> 所有叶子同深度

例：2-3-4树

![image-20240421104203609](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240421104203609.png)

所有真实的数据都被存储在叶子结点中，形成一个有序的数列。而非叶子结点中第 `i` 个键值等于其第 `i+1` 棵子树的最小值（在下图中表现为颜色相同的一对上下结点），因此非叶结点最多存 `M−1` 个值。

- m阶B+数每个结点最多有m个子树，有m-1个数值。

- 3阶B+数又称2-3树；4阶又称2-3-4树。

### 操作

> **取底符号**
>
> ⌊ x ⌋ : 不大于x的**最大**整数
>
> **取顶符号**
>
> 『x  : 不小于x的**最小**整数

> 看王道

插入后检查结点，超了就对半分  

#### 插入

![image-20240421105527636](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240421105527636.png)

> 见qq聊天记录