## Backtracking

回溯法是加上剪枝（pruning）操作的遍历法，即回溯法会边遍历边预判，通过pruning缩小可能解空间

一个解是由一组元素组成的。先找到正确的第一个元素作为遍历的开头，在此基础上找到匹配的第二个元素，以此类推

递进到某一个位置发现找不到匹配的了，就回到上一个位置，换下一个匹配的元素，以此类推，即，走迷宫发现走不通就回头换条路

1. 构造空间树；
2. 进行遍历；
3. 如遇到边界条件，即不再向下搜索，转而搜索另一条链；
4. 达到目标条件，输出结果。

### 过程

在脑子里建树，深度优先遍历（即后续遍历），根据题目给的规则灵活剪

代码如下：

```cpp
bool Backtracking ( int i )
{   Found = false;
    if ( i > N )
        return true; /* solved with (x1, …, xN) */
    for ( each xi  Si ) { 
        /* check if satisfies the restriction R */
        OK = Check((x1, …, xi) , R ); /* pruning */
        if ( OK ) {
            Count xi in;
            Found = Backtracking( i+1 );
            if ( !Found )
                Undo( i ); /* recover to (x1, …, xi-1) */
        }
        if ( Found ) break; 
    }
    return Found;
}
```

#### 八皇后问题

#### The Turnpike Reconstruction Problem

#### α-β pruning

## Divide and Conquer

![image-20240409104757802](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240409104757802.png)

分为了`a`个子问题，每个子问题规模为`N/b`，合并的开销为`f(N)`

### Methods for solving recurrences

代入法，猜出上界，归纳法证明,，常猜 $O(NlogN)$

递归树法，边画边猜，看手写笔记

**主方法**

![image-20240409113937447](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240409113937447.png)

第一个就是叶子特别多时，就只看叶子

第   个是根特别大，就只看根

#### Closest Points Problem

## Dynamic Programming

> 刷题补天

