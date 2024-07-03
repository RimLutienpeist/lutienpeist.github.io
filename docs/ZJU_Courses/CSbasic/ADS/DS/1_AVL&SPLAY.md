## AVL

### Define

![image-20240401105718762](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240401105718762.png)

### Height

![image-20240401105802233](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240401105802233.png)

###  Trouble Finder

![image-20240401105931695](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240401105931695.png)

## Splay 树

Splay 树，即伸展树，想要解决的问题和 AVL 树类似，只不过 Splay 树希望达到的目标是在**摊还(Amortized)**复杂度 $O(logN)$ 的情况下完成大部分对点操作。

为使 AVL 保持平衡，我们需要维护从根节点到 Trouble Maker 这条路径上所有点的平衡因子。而 Splay 则不再维护这些信息，这意味着我们无法保证 Splay 树的状态都是平衡的，但是我们希望它尽可能平衡。

对于一个树，我们对其节点进行的操作可能是：**增**点、**删**点、**改**点、**查**点等等，而不同类型的操作开销可能不尽相同。

### 摊还分析

#### 分析对象

开始分析之前，我们首先需要明确分析的目标：

对于 Splay，它不存在明显的减势和增势行为，所有我们提到的操作都依赖于**将目标点旋转到根**来实现，而这也成为其主要开销。

> 部分常数操作显然被覆盖，插入之类的操作之所以能被忽略的原因，可以参考 ltgg 的**[这篇文章](https://www.yuque.com/27rabbit/gi2sf3/veonae)**）

其中我们会用到若干次 `zig`、`zig-zag`、`zig-zig` 的操作。

![image-20240401110520213](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240401110520213.png)![image-20240401110900510](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240401110900510.png)

#### 势能函数

![image-20240401110550940](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240401110550940.png)

> 我们定义一棵**二叉树**的秩为从为**从根节点开始**到**其叶节点**中**最长的一条树链**上结点的个数。

![image-20240401110700328](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240401110700328.png)

#### zig

#### zig-zag

#### zig-zig