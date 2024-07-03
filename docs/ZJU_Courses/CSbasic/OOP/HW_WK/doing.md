## HW1

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523183246612.png" alt="image-20240523183246612" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523183259069.png" alt="image-20240523183259069" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523183313684.png" alt="image-20240523183313684" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523183324499.png" alt="image-20240523183324499" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523183832009.png" alt="image-20240523183832009" style="zoom:67%;" />

![image-20240523183554480](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523183554480.png)

> C99才支持单行注释。所以之前的TC是不支持单行注释的。完美解释了我实验课用TC注释一直出错（滑稽）

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523184110509.png" alt="image-20240523184110509" style="zoom:67%;" />

> `getline(s,5)`设置长度，有一个空位要留给`\0`
>
> `cin.getline()`属于istream流，而`getline()`属于string流

> 当同时使用`cin>>`, `getline()`时，需要注意的是，在`cin>>`输入流完成之后，`getline()`之前，需要通过
>
> ```cpp
> str="\n";
> getline(cin,str);
> ```
>
> 的方式将回车符作为输入流cin以**清除缓存**，如果不这样做的话，在控制台上就不会出现getline()的输入提示，而直接跳过，因为程序默认地将之前的变量作为输入流。
>

## HW2

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523190224599.png" alt="image-20240523190224599" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523190418309.png" alt="image-20240523190418309" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523191056927.png" alt="image-20240523191056927" style="zoom:67%;" />

> 答案应该是1

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523191348169.png" alt="image-20240523191348169" style="zoom:67%;" />

> ？？？？？？？

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523191610950.png" alt="image-20240523191610950" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523200451432.png" alt="image-20240523200451432" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523200534078.png" alt="image-20240523200534078" style="zoom:67%;" />

## HW3

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523200754084.png" alt="image-20240523200754084" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523200830615.png" alt="image-20240523200830615" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523200910928.png" alt="image-20240523200910928" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523200942137.png" alt="image-20240523200942137" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523201003596.png" alt="image-20240523201003596" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523201024408.png" alt="image-20240523201024408" style="zoom:67%;" />

## HW4

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523201151496.png" alt="image-20240523201151496" style="zoom: 50%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523201207340.png" alt="image-20240523201207340" style="zoom: 67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523201236819.png" alt="image-20240523201236819" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523201307771.png" alt="image-20240523201307771" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523201331092.png" alt="image-20240523201331092" style="zoom:67%;" />

[C++：友元（看这一篇就够了）_c++ 友元-CSDN博客](https://blog.csdn.net/weixin_46098577/article/details/116596183)

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523201518358.png" alt="image-20240523201518358" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523201538591.png" alt="image-20240523201538591" style="zoom:67%;" />

[C++中的静态成员变量和静态成员函数 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/397907673)

> ？

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523202151192.png" alt="image-20240523202151192" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523202331626.png" alt="image-20240523202331626" style="zoom:67%;" />

> ？

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523202454106.png" alt="image-20240523202454106" style="zoom: 80%;" />

## HW6

![111111](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/111111.png)

[【C++】 内联函数详解（搞清内联的本质及用法）-CSDN博客](https://blog.csdn.net/qq_35902025/article/details/127912415)

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523202838957.png" alt="image-20240523202838957" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523202858902.png" alt="image-20240523202858902" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523202916572.png" alt="image-20240523202916572" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523202938545.png" alt="image-20240523202938545" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523202959561.png" alt="image-20240523202959561" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523203033417.png" alt="image-20240523203033417" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523203118162.png" alt="image-20240523203118162" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523203134428.png" alt="image-20240523203134428" style="zoom: 67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523203204794.png" alt="image-20240523203204794" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523203216305.png" alt="image-20240523203216305" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523203236089.png" alt="image-20240523203236089" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523203254261.png" alt="image-20240523203254261" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240523203302617.png" alt="image-20240523203302617" style="zoom:67%;" />

## HW7