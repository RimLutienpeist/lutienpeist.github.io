## access control

`private` 只在**类（不是对象）**内部（内部变量、函数）可以访问，我们是可以利用指针访问同一个类不同对象的私有变量：

```cpp
struct B {
private:
    int j;
public:
    void f(B *p) {
        p->j = 'A';
    }
}

B b, bb;
B.f(&bb);
```

这样是正确的，b 和 bb 是同一个类的不同对象

`protected`，不让外界访问，但可以让继承者访问

**Friends** 友元

其他函数，结构就可以访问本对象的变量，只有自己可以决定友元。

```cpp
struct X {
private:
    int i;
public:
    void initialize();
    friend void g(X*, int i);
    friend void Y::y();
}
```

- class defaults to private
- struct defaults to public.

## Initialization

- Initialization

```cpp
Student::Student(string s):name(s) {}
```

before constructor

`:` 后面的就是初始化列表，只在构造函数中使用，会在构造函数执行之前调用 Initializer list 的构造

且列表里变量的初始化顺序，是按照函数里声明的顺序进行，与列表里的排列顺序无关

> - Assignment
>
>   ```cpp
>   Student::Student(string s) {name=s;}
>   ```
>
> inside constructor. string must have a default constructor.
>
> (先构造出string的对象name, 再赋值)

```cpp
class Point {
private:
    const float x, y;
public:
    Point(float xa = 0.0, float ya = 0.0) : y(ya), x(xa) {}
};
```

这里的 `const` 变量不能被赋值，只能被初始化

初始化可以在class里 `const float x = 1.0;` ，但这样所有类的对象的值都是一样的

## Overloaded constructors

我们可以有重名的函数，但是必须要有不同之处，以便编译器区分，如参数个数不同，参数类型不同

```cpp
void print(char * str, int width); // #1 
void print(double d, int width); // #2 
void print(long l, int width); // #3 
void print(int i, int width); // #4 
void print(char *str); // #5 
print("Pancakes", 15); 
print("Syrup"); 
print(1999.0, 10); 
print(1999, 12); 
print(1999L, 15);
```

```cpp
void f(short i);
void f(double d);
f('a');
f(2);
f(2L);
f(3.2);

//除了最后一个，其他都是不能分辨的。
```

## Default arguments

默认值必须从右到左

```cpp
Stash(int size, int initQuantity = 0);

int harpo(int n, int m = 4, int j = 5);
int chico(int n, int m = 6, int j); // illegal
int groucho(int k = 1, int m = 2, int n = 3);
beeps = harpo(2);
beeps = harpo(1,8);
beeps = harpo(8,7,6);
```

默认值只能出现在函数原型

```cpp
void f(int i, int j = 10);
int main()
{
    ...
}
void f(int i, int j = 10){	// error
    ...
}
```

## Overhead for a function call

### inline function