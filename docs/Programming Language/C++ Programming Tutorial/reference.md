# Reference

### 定义

**引用**就是某一变量（目标）的一个别名，对引用的操作与对变量直接操作完全一样。

定义引用的表示方法与定义指针相似，只是用`&`代替了`*`。

其格式为：`类型` `&` `引用变量名` = `已定义过的变量名`。

- 引用的特点：
  - 一个变量可取多个别名，即被多次引用。
  - 只能在初始化的时候指定引用的变量 ，且初始化后不能转而引用其他变量。

### 示例

**基础引用**

```c++
void TestReference1 ()
{
     int a = 1;
     int& b = a;
 
     cout<<"a:address->" <<&a<< endl;
     cout<<"b:address->" <<&b<< endl;
 	//same address
    
    //没有 const 可以修改别名的值，引用的值也会相应变化
     a = 2;
     b = 3;
     int& c = b;// 引用一个引用变量，别名的别名
     c = 4;
}
```

**const引用**

```c++
void TestReference2 ()
{
     int d1 = 4;
     const int & d2 = d1;
     d1 = 5;//d1改变，d2的值也会改变。
     //d2 = 6;//这句会报错，不能给常量（不能被修改的量）赋值。
 
     const int d3 = 1;
     const int & d4 = d3;
     //int&d5 = d3;//会报错
     const int & d6 = 5;
    
    
    //引用不同类型的变量，选哟类型转换，会生成一个const临时变量用于被引用，所以引用需要初始化为const
     double d7 = 1.1;
	//cannot bind non-const lvalue reference of type 'int&' to an rvalue of type 'int'
     const int& d9 = d7;
}
```

**引用作参数**

```c++
1.【值传递（常见情况）】如果形参为非引用的传值方式，则生成局部临时变量接收实参的值
void Swap (int left, int right) 
}
 
2.【引用传递】如果形参为引用类型，则形参是实参的别名。
    
void Swap (int& left, int& right)//使用引用的话，不做临时拷贝，&的使用说明此处只是原参数的另一个名字而已，所以修改时直接在原参数的基础上修改变量值。
{
     int temp = right;
     right = left ;
     left = temp ;
}
 
3.【指针传递】
    
void Swap (int* pLeft, int* pRight)//传入的是地址，因为地址是唯一的，所以指针通过地址的访问进而可修改其内容。
{
     int temp = *pLeft;
     *pLeft = *pRight;
     *pRight = temp;
}
```

### 注意

（1）&在这里不是求地址运算，而是起标识作用。

（2）类型标识符是指目标变量的类型。

（3）声明引用时，必须同时对其进行初始化。

（4）引用声明完毕后，相当于目标变量名有两个名称，即该目标原名称和引用名，且不能再把该引用名作为其他变量名的别名。

（5）对引用求地址，就是对目标变量求地址。即引用名是目标变量名的一个别名。引用在定义上是说引用不占据任何内存空间，但是编译器在一般将其实现为const指针，即指向位置不可变的指针，所以引用实际上与一般指针同样占用内存。

（6）不能建立引用的数组，但是可以建立数组的引用。

（7）引用常见的使用用途：作为函数的参数、函数的返回值。

### 总结

1. 不要返回一个临时变量的引用。

2. 如果返回对象出了当前函数的作用域依旧存在，则最好使用引用返回，因为这样更高效。

### 引用和指针的区别和联系

相对而言，引用比指针更安全。

指针比引用更为灵活，但是其风险也很大。

使用指针时一定要检查指针是否为空(NULL)，且空间回收后指针最好置零，以免野指针的发生造成内存泄漏等问题。

#### Ⅰ.引用和指针的区别和联系：

★不同点：

1. 指针是一个实体，而引用仅是个别名；
 2. 引用使用时无需解引用(*)，指针需要解引用；
 3. 引用只能在定义时被初始化一次，之后不可变；指针可变；
 4. 引用不能为空，指针可以为空；
 5. “sizeof 引用”得到的是所指向的变量(对象)的大小，而“sizeof 指针”得到的是指针本身(所指向的变量或对象的地址)的大小；
7. 指针和引用的自增(++)运算意义不一样；
7. 从内存分配上看：程序为指针变量分配内存区域，而引用不需要分配内存区域。

★相同点：

两者都是地址的概念，指针指向一块儿内存，其内容为所指内存的地址；引用是某块儿内存的别名。

#### Ⅱ.const在C和C++中的含义（笔试热点）：

> 没看

⑴C中的const，功能比较单一，较容易理解：
作用：被修饰的内容不可更改。
使用场合：修饰变量，函数参数，返回值等。（c++中应用场合要丰富的多）
特点： 是运行时const，因此不能取代#define用于成为数组长度等需要编译时常量的情况。同时因为是运行时const，可以只定义而不初始化,而在运行时初始化。如 const int iConst;。 另外，在c中，const变量默认是外部链接，因此在不同的编译单元中如果有同名const变量，会引发命名冲突，编译时报错。
⑵c++中的const：

a、非类成员const：

①const变量默认是内部连接的，因此在不同的编译单元中可以有同名的const 变量定义。

②编译时常量，因此可以像#define一样使用，而且因为上面一点，可以在头文件中定义const变量，包含的不同的cpp文件（编译

单元）中使用而不引起命名冲突。

③编译器默认不为const变量分配内存，除非：1. 使用 extern 申明， 2：程序中有引用const 变量的地址。

④c++中临时对象/内置变量默认具有const属性。

b、类中的const：

①与c语言中的const一样，只是运行时常量，不能作为数组维数使用，即不能取代#define。在类中使用下面两种方式取代#define： 1：static const... 

2 : enum{....}//enum 不占存储空间。

②类中的const 变量占用存储空间。

③类中的const成员变量需要在构造函数初始化列表中初始化。

④const 对象：在该对象生命周期内，必须保证没有任何成员变量被改变。const对象只能调用const成员函数。

⑤const成员函数： void fun() const ... 不仅能被const对象调用，也能被非const对象调用，因此，如果确认一个任何成员函数不改

变任何成员变量，应该习惯性将该函数定义成const类型。

⑥如果一个对象被定义成const，那么该const对象“可能”会被放入到ROM当中，这在嵌入式开发当中有时非常重要。