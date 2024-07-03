# Const

#### Pointers and constants

```cpp
string p("Fe");
const string *p = &p1;
string const *p = &p1;
string *const p = &p1;
```

```cpp
char c;
const char cc;

char *cp;
const char * ccp;

ccp = &c;
ccp = &c;

cp = &cc;	//illegal
ccp = &cc;
```

```cpp
char *const p = "abc";
*q = 'c';//legal
q++;	//illegal
```

```cpp
char *string p = "abc";
//(*p) is a const char
*p = 'b'; //illegal
```

#### String Literals

```cpp
char *s = "ass";
// == const char* s
//Don't try and change the character values 

//If you want to change the string, put it in an array:
char s[] = "Hello, world!";

```

