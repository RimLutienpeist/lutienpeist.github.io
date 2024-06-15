### The constructor

If a class has a constructor, the compiler automatically calls that constructor at the point an object is created

The  name of the constructor is the same as the name of the class.

#### How a constructor does?

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240429143708544.png" alt="image-20240429143708544" style="zoom: 33%;" />

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240429144147516.png" alt="image-20240429144147516" style="zoom: 33%;" />

#### Constructors with arguments

The constructor can have arguments to allow you to specify how an object is created, give it initialization values, and so on.

#### The default constructor

A *default constructor* is one that can be called with no arguments

#### “auto” default constructor

If you have a constructor, the compiler ensures that construction always happens.

If (and only if) there are no constructors for a class (struct or class), the compiler will automatically create one for you.

### The destructor

In C++, cleanup is as important as initialization and is therefore guaranteed with the destructor

- The destructor is named after the name of the class with a leading tilde (`~`). 
- The destructor never has any arguments
- The destructor **is called automatically** by the compiler when the object goes out of scope.
- 



<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240429144500299.png" alt="image-20240429144500299" style="zoom:33%;" />

### Storage allocation

 The compiler allocates all the storage for a scope **at the opening brace of that scope.**

### Aggregate initialization

```cpp
int a[5] = {1,2,3,4,5};
int b[6] = {5};
int c[] = {1,2,3,4};
	- sizeof c / sizeof *c
struct x { int i; float f; char c; };
	- X x1 = {1, 2.2, 'c'};
X x2[3] = { {1, 1.1, 'a'}, {2, 2.2, 'b'} }
struct Y { float f; int i; Y(int a); };
Y y1[] = { Y(1), Y(2), Y(3) };
```

### Fields,parameters,local variables

All three kinds of variable are able to store a value that is appropriate to their defined type.

- Fields (member variables) are defined outside constructors and methods
- Fields are used to store data that persists throughout the life of an object. 
  - they maintain the current state of an object. They have a lifetime that lasts as long as their object lasts.
- Fields have class scope: their accessibility extends throughout the whole class
- Formal parameters：即传参变量
- Local variables ：即内部新定义的，若与外面的变量同名会屏蔽外面的

### Initialization vs. assignment

#### 初始化 (Initialization):

- 初始化是指在创建变量时为其指定初始值的过程。

  初始化通常发生在以下场景：

  - 声明变量并为其指定值：`int x = 10;`
  - 使用构造函数创建对象时：`MyClass obj(5);`
  - 使用列表初始化语法创建集合类对象：`std::vector<int> numbers {1, 2, 3};`

#### 赋值 (Assignment):

- 赋值是指在变量已经创建之后，改变其现有值的过程。
- 赋值使用赋值运算符 (`=`) 完成：`x = 20;`
- 赋值会改变变量原有的值，将其替换为新的值。

| 特征     | 初始化                               | 赋值             |
| -------- | ------------------------------------ | ---------------- |
| 发生时机 | 创建变量时                           | 变量创建之后     |
| 目的     | 为变量指定初始值                     | 改变变量现有值   |
| 相关语法 | 声明变量并赋值, 构造函数, 列表初始化 | 赋值运算符 (`=`) |

```cpp
class MyClass {
public:
  int value;

  // 构造函数，初始化 value 成员变量
  MyClass(int val) : value(val) {}
};

int main() {
  // 初始化变量
  int x = 10;
  double pi = 3.14159;

  // 对象初始化
  MyClass obj1(20);

  // 赋值操作
  x = 30;
  pi = 22 / 7.0; // 改变 pi 的值

  return 0;
}
```

### Function overloading

Same functions with different arguments list, auto-cast.

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


void f(short i);  
void f(double d);

f(‘a’);  f(2);
f(2L);
f(3.2);
```

### Default arguments

```cpp
Stash(int	size, int	initQuantity = 0);
```

To define a function with an argument list, **defaults must be added from right to left.**

```cpp
int harpo(int n, int m = 4, int j = 5);
int chico(int n, int m = 6, int j);//illeagle
int groucho(int k = 1, int m = 2, int n = 3);
beeps = harpo(2);
beeps = harpo(1,8);
beeps = harpo(8,7,6);
```

### const object

#### Const member functions

Cannot modify their objects

```cpp
int Date::get_day() const {
	day++; //ERROR modifies data member
	set_day(12); // ERROR calls non-const member
	return day; // ok
}

int Date::set_day(int d){
	//...error check d here...
	day = d; // ok, non-const so can modify
}
```

Function members that do not modify data should be declared const

const member functions are safe for const objects

#### Const objects

```cpp
// non-const object
Date when(1,1,2001); // not a const
int day = when.get_day(); // OK
when.set_day(13); // OK

// const object
const Date birthday(12,25,1994); // const
int day = birthday.get_day(); // OK
birthday.set_day(14); // ERROR
```

#### Constant in class

```cpp
class A {
	const int i;
};
//has to be initialized in initializer list of the constructor
```

#### Compile-time constants *in* *classes*

```cpp
class HasArray {
	const int size;
	int array[size]; // ERROR!
	...
};

//Make the const value static:
static const int size = 100;
//static indicates only one per class (not one per object)

//Or use “anonymous enum” hack:
Class HasArray{
    enum { size = 100 };
    int array[size];  // OK!
    …
}
```

### type of function parameters and return value

> ???

#### way in

void f(Student i);

a new object is to be created in f

void f(Student *p);

better with const if no intend to modify the object

void f(Student& i);

better with const if no intend to modify the object

#### way out

Student f();

a new object is to be created at returning

Student* f();

what should it points to?

Student& f();

what should it refers to?

#### hard decision

```cpp
//define a pair functions of alloc and free
char *foo()
{
	char *p;
	p = new char[10];  
    strcpy(p, "something");  
    return p;
}

//Let user take resp., pass pointers in & out
void bar()
{
	char *p	= foo();  
    printf("%s", p);  
    delete p;
}
```

#### tips

1. Pass in an object if you want to store it
2. Pass in a const pointer or reference if you want to get the values
3. Pass in a pointer or reference if you want to do something to it
4. Pass out an object if you create it in the function
5. Pass out pointer or reference of the passed in only
6. Never new something and return the pointer
