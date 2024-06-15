# Dynamic memory allocation

在C++程序中，所有内存需求都是在程序执行之前通过定义所需的变量来确定的。 

但是可能存在程序的内存需求只能在运行时确定的情况。 例如，当需要的内存取决于用户输入。 

在这些情况下，程序需要动态分配内存，C ++语言将运算符new和delete合成在一起。

```c++
Type* pointer = new Type;
//...
delete pointer;

//array
Type* pointer = new Type[N];
//...
delete[] pointer;

```

| 1.C++中通过new关键字进行动态内存申请  |
| ------------------------------------- |
| 2.C++中的动态内存分配是基于类型进行的 |
| 3.delete关键字用于内存释放            |

#### eg

```c++
int * foo;
foo = new int [5];
```

![img](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/20180907115436709)

```cpp
#include <stdio.h>
 
int main()
{
    int* p = new int;
    
    *p = 5;
    *p = *p + 10;
    
    printf("p = %p\n", p);
    printf("*p = %d\n", *p);
    
    delete p;
    
    p = new int[10];
    
    for(int i=0; i<10; i++)
    {
        p[i] = i + 1;
        
        printf("p[%d] = %d\n", i, p[i]);
    }
    
    delete[] p;
    
    return 0;
}

p = 007F77D8
*p = 15
    
p[0] = 1
p[1] = 2
p[2] = 3
p[3] = 4
p[4] = 5
p[5] = 6
p[6] = 7
p[7] = 8
p[8] = 9
p[9] = 10
```

#### new与malloc的区别

| new关键字是C++的一部分              | malloc是由C库提供的函数        |
| ----------------------------------- | ------------------------------ |
| new以具体类型为单位进行内存分配     | malloc以字节为单位进行内存分配 |
| new在申请单个类型变量时可进行初始化 | malloc不具备内存初始化的特性   |

#### new初始化

```cpp
int* pi = new int(1);
float* pf = new float(2.0f);
char* pc = new char('c');


*pi = 1
*pf = 2.000000
*pc = c
```

#### Tips

1. Use `delete []` if you used `new []` to allocate an array.
2. It's safe to apply `delete `to the `null `pointer (nothing happens).