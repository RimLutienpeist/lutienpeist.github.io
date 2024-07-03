## References

声明引用时，必须有引用的变量，而且不能用右值初始化引用，右值就是 `i*3+1` 之类的，

不能用其它引用进行初始化，指针不能指向引用，指针可被引用，没有引用数组这种东西

```cpp
void func(int &);
func (i * 3); // Warning or error!

char c = 'A';
char &r = c;
r = 'B';
cout << "c: " << c << endl;
cout << "b: " << b << endl;
//输出都是 B

int y = 1;
void f (int& x);
f(y)
//别名x在函数被调用时初始化
```

`const int& z = x;` 这里的 `const` 只对限制引用， 但 x 依然可写

然后引用作为参数在函数里可以直接影响本值

```cpp
void f(int &x){
    x++;
}
int main(){
    int a = 51;
    cout << "a=" << a << endl;
    f(a);
    cout << "a=" << a << endl;
}
//51 52
```

- References
  - can't be null
  - are dependent on an existing variable, they are an alias for an variable
  - can't change to a new "address" location
- Pointers
  - can be set to null
  - pointer is independent of existing objects
  - can change to point to a different address

## Container

Collection objects are objects that can store other objects.

容器在 STL 中，**STL** = **Standard Template Library**

**Library** includes

- A `pair` class (pairs of anything, int/int, int/char, etc)
- containers
  - `vector` (expandable array)
  - `deque` (expandable array, expands at both ends)
  - `list` (double-linked)
  - `sets` and `maps`
- Basic Algorithms (`sort`, `search`, etc)
  - All identifiers in library are in std namespace

### Vector

每个容器对应一个头文件，需要 include. 如 `#include<vector>`.

```cpp
#include <iostream>
#include <vector>
using namespace std;
int main( ) {
    vector<int> x; // Declare a vector of ints (no worry about size)
    
    for (int a=0; a<1000; a++)
   		x.push_back(a); // Add elements
    
    // Have a pre-defined iterator for vector class, can use it to print out the items in vector
    vector<int>::iterator p;
    for (p=x.begin(); p<x.end(); p++)
    	cout << *p << " ";
    return 0;
}
```

`vector<int>::iterator` 是一个类型，p 发挥了类似链表里指针的作用

> 但 p 并不是指针，利用了 C++ 的运算符重载

```cpp
//Constructor
vector<Elem>c;
vector<Elem>c1(c2);

//Methods
V.size(); // num items
V.empty(); // empty?
==, !=, <, >, <=, >=
V.swap(v2); // swap

//Iterators
I.begin() // first position
I.end() // last position

//access
V.at(index)
V[index]
V.front() // first item
V.back() // last item

//Add/Remove/Find
V.push_back(e)
V.pop_back()
V.insert(pos, e)
V.erase(pos)
V.clear()
V.find(first, last, item)
```

vector 的空间是保证连续的，物品是保证按push顺序存放的

被 push 的元素是被复制到 vector 里面，类型会自动转化为 vector 的类型

### List 

```cpp
x.push_back(item)
x.push_front(item)
x.pop_back()
x.pop_front()
x.remove(item)

#include <iostream>
#include <list>
#include <string>
using namespace std;
int main()
{
    list<string>s;
    s.push_back("hello");
    s.push_back("world");
    s.push_front("tide");
    s.push_front("crimson");
    s.push_front("alabama");
    list<string>iterator:: p;
    for (p=s.begin(); p!=s.end(); p++)
        cout << *p << " ";
    cout << endl;
}

list<int> L;
for(int i=1; i<=5; ++i)
L.push_back(i);
//delete second item.
L.erase( ++L.begin() );
copy( L.begin(), L.end(),ostream_iterator<int>(cout,",")); //Prints: 1,3,4,5,
```

list 空间是动态分配的（见缝插针），后申请的空间不能保证在先申请的空间后面，所以这里用 `p!=s.end()` 

### Maps

存储的是一堆二元映射，每个映射有一个 key 和 一个 value，表示 key->value

能想象到会有 method 是通过输入 key 获取 value

> 其实就是有类型拓展的数组嘛，index 和值可以改成任意类型了

```cpp
#include <map>

map<long,int> root;
root[4] = 2;
root[1000000] = 1000;
long l;
cin >> l;
if (root.count(l))
    cout<<root[l]
else cout<<“Not perfect square”;
```

- Use `empty()` on `list<>`

  ```cpp
  if ( my_list.count() == 0 ) { ... } // Slow
  if ( my_list.empty() ) {...} // Fast
  ```

## Iterators

迭代子，专门用于遍历容器的一种变量类型，以 list 为例：

```cpp
list<int>::iterator li; //Declaring
list<int>L;li = L.begin(); //Front of container
li = L.end(); //Past the end

li=L.begin();
++li; // Second thing - Can increment
*li = 10; //Can be dereferenced
```
现成的工具：

```cpp
for(type variable_name : array/vector_name) {
    ...
}

//for-each loop，获得的值都是只读的

int arr[]={1,2,3,4,5}; //array initialization
cout<<"The elements are: ";
for(int i : arr) // auto
{
    cout<<i<<" ";
}
```

for-each loop 不需要预先初始化迭代器，缺点是不能获得下标，不能逆序遍历，不能跳过某个单元，不能修改容器的值

## Pitfalls

- Accessing an invalid

  ```cpp
  vector<int> v;
  v[100]=1; // Whoops!
  ```

  Solutions

  - use `push_back()`
  - Preallocate with constructor.
  - Reallocate with `reserve()`
  - Check `capacity()`

- Inadvertently inserting into `map<>`

  ```cpp
  if (foo["bob"]==1)
  //silently created entry “bob”
  ```

  Solutions: Use `count()` to check for a key without creating a new entry：`if ( foo.count("bob") )`

> count()方法返回值是一个整数，1表示有这个元素，0表示没有这个元素

- Use invalid iterator

  ```cpp
  list<int> L;
  list<int>::iterator li;
  li = L.begin();
  L.erase(li);
  ++li; // WRONG
  // Use return value of erase to advance
  li = L.erase(li); // RIGHT
  ```
