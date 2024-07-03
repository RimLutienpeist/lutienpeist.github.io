#### The Makefile utility

- Targets
  1. Good division to components
  2. Minimum compilation when something is changed
  3. Easy maintenance of project structure, dependencies and creation

> Note that the Makefile mechanism is not limited to C programs

##### Project structure

Project structure and dependencies can be represented as a DAG (= Directed Acyclic Graph)

**e.g**

– Program contains 3 files

– main.c., sum.c, sum.h

– sum.h included in both .c files

– Executable should be the file sum

![image-20240426125212956](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240426125212956.png)

```makefile
sum: main.o	sum.o
gcc –o	sum main.o	sum.o

main.o: main.c sum.h  gcc –c main.c

sum.o: sum.c sum.h  gcc –c sum.c


//Equivalent makefiles
//.o depends (by default) on corresponding	.c  file.
sum: main.o sum.o
gcc –o sum main.o sum.o

main.o: sum.h  gcc –c main.c

sum.o: sum.h  gcc –c sum.c
```

![image-20240426125340238](C:\Users\89620\AppData\Roaming\Typora\typora-user-images\image-20240426125340238.png)

```makefile
sum: main.o	sum.o
gcc –o	$@	main.o	sum.o
main.o	sum.o: sum.h  gcc –c $*.c
```

