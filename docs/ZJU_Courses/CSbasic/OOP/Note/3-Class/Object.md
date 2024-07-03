### C vs. C++

![image-20240415224113364](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240415224113364.png)

***Objects* *=* *Attributes* *+ Services***

- Data: the properties or status
- Operations: the functions

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240415224146542.png" alt="image-20240415224146542" style="zoom:50%;" />

### Stash

#### Container

**Container** is an object that holds other objects.

- For most kinds of containers, the common interface is **put()** and **get()**.


**Stash** is a container that stores objects and can be **expanded** during running.

- Each element in Stash is a **clone** of the object.

```cpp
struct Stash {
    int size; // Size of each space
    int quantity; // Number of storage spaces
    int next; // Next empty space
    // Dynamically allocated array  
    unsigned char* storage;
    // Functions!
    void initialize(int size);  
    void cleanup();
    int add(const void* element);  void* fetch(int index);
    int count();
    void inflate(int increase);
};
```

##### Implementation of the functions

We just defined in the header file that there will be these functions in this struct.

All the bodies of these functions will be in a source file.

##### Call the functions in a struct

```cpp
Stash a;  
a.initialize(10);
```

#### Objects

In C++, an object is just a variable, and the purest definition is “a region of storage”.

The struct variables mentioned before are just objects in C++.

### Object vs. Class

- Objects	(cat)
  - Represent things, events, or concepts
  - Respond to messages at run-time
- Classes	(cat class)
  - Define properties of instances
  - Act like **types** in C++

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240422121214511.png" alt="image-20240422121214511" style="zoom:50%;" />

### OOP Characteristics

1. Everything is an object.

2. A program is a bunch of objects telling each other what to do by sending messages.

3. Each object has its own memory made up of other objects.

4. Every object has a type.

5. All objects of a particular type can receive the same messages.

### Definition of a class

In C++, separated `.h` and `.cpp` files are used to define one class.

- Class declaration and prototypes in that class are in  the header file (.h).
- All the bodies of these functions are in the source file (.cpp).

#### compile unit

- The  compiler sees only one ` .cpp` file, and generates ` .obj ` file
- The linker links all ` .obj` into one executable  file
- To provide information about functions in other `.cpp` files, use` .h`

#### The header files

> Header = interface

The header is a contract between you and the user  of your code.

![image-20240426123934968](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240426123934968.png)

- Only  declarations are allowed to be in .h  
  - extern
  - variables
  - function prototypes class/struct 
  - declaration

`#include <xx>`:same as `#include <xx.h>`

```cpp
//Standard header file structure
#ifndef HEADER_FALG
#defien HEADER_FALG
//Type declaration here ...
#endif //HEADER_FLAG
```

- Tips  for header
  1. One class declaration per header file
  2. Associated with one source file in the same prefix of file name.
  3. The contents of a header file is surrounded with #ifndef #define…  #endif
  4. `#pragma` once equivalent to `#ifndef…#endif`

