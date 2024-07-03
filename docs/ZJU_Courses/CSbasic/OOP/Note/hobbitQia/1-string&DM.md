## String

### Assignment for string

```cpp
char charr1[20];
char charr2[20] = "jaguar"; 
string str1;
string str2 = "panther"; 
carr1 = char2; // illegal 
str1 = str2; // legal
```

> 这里 `"panther"` 是一个字符串字面量。
>
> 在C语言中，形如`"hello world"`的字符串即为**字符串字面量**（常量），与之对比的是**字符串变量**，形如`char arr[] = "hello world"`，两者的存储属性截然不同
>
> 字符串字面量和字符数组有一个很重要的差别：前者是只读的，若程序试图修改字符串字面量，那么结果是**未定义**的；后者是可读可写的（除非主动使用const修饰）。

### Concatenation for string

```cpp
string str3("aaa");
str3 = str1 + str2;
str1 += str2;
str1 += "lalala";
```

### Length

`s.length()` 得到字符串的长度。(C++ 中字符串没有 `\0`.)

> 确切来说，编译器可能会在末尾加上 `\0`，但是字符串对象里面包含了长度信息，不会受这个 `\0`影响

## Dynamically Allocated Memory

`new` 返回指向地址空间的指针，但 `new` 知道地址空间的类型（与 `malloc` 不同）

- `new int;`
- `new Stash;`
- `new int[10];`

`delete` 

- `delete p;`
- `delete[] p;`

如果要删除的是一个对象，那么会执行其析构函数

```cpp
int * psome = new int [10];
delete[] psome;
```

> `new` 看成 `malloc`，`delete` 看成 `free`

**注意**

1. `p1 = new int;` 返回一块四个字节的空间的地址，同时有一个表记录这个地址有我们申请的四字节，同理 `p2 = new int [10];` 也会在表中记录
2. `delete` 不会去抹掉内存上的数据，只是将表中条目去掉
3. `p2++; delete p2;` 是一个异常操作，会找不到 p2
4. `delete p2;` 认为 `p2` 指的是一个对象，所以只将第一个对象析构，`delete [] p2;` 就是告诉系统不止一个对象，会帮我们将所有对象都析构