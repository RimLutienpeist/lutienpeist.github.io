# Compiling, Linking and Building 

C/C++ Applications

## 1. GCC (GNU Compiler Collection)

#### 1.1 A Brief History and Introduction to GCC

GCC, formerly for "*GNU C Compiler*", has grown over times to support many languages such as C (`gcc`), C++ (`g++`), Objective-C, Objective-C++, Java (`gcj`), Fortran (`gfortran`), Ada (`gnat`), Go (`gccgo`), OpenMP, Cilk Plus, and OpenAcc. 

 It is now referred to as "*GNU Compiler Collection*".

#### 1.4 Installing GCC on Windows

For Windows, you could either install Cygwin GCC, MinGW GCC or MinGW-W64 GCC. Read "[How to install Cygwin and MinGW](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Cygwin_HowTo.html)".

- Cygwin GCC: Cygwin is a Unix-like environment and command-line interface for Microsoft Windows. Cygwin is huge and includes most of the Unix tools and utilities. It also included the commonly-used Bash shell.
- MinGW: MinGW (Minimalist GNU for Windows) is a port of the GNU Compiler Collection (GCC) and GNU Binutils for use in Windows. It also included MSYS (Minimal System), which is basically a Bourne shell (`bash`).
- MinGW-W64: a fork of MinGW that supports both 32-bit and 64-bit windows.

#### 1.6 Getting Started

The GNU C and C++ compiler are called `gcc` and `g++`, respectively.

#### 1.8 Headers (.h), Static Libraries (.lib, .a) and Shared Library (.dll, .so)

A library is a collection of pre-compiled object files that can be linked into your programs via the linker. Examples are the system functions such as `printf()` and `sqrt()`.

There are two types of external libraries: *static library* and *shared library*.

1. A static library has file extension of "`.a`" (archive file) in Unixes or "`.lib`" (library) in Windows.
   1. When your program is linked against a static library, the machine code of external functions used in your program is copied into the executable.
   2. A static library can be created via the *archive* program "`ar.exe`".
2. A shared library has file extension of "`.so`" (shared objects) in Unixes or "`.dll`" (dynamic link library) in Windows. 
   1. When your program is linked against a shared library, only a small table is created in the executable. Before the executable starts running, the operating system loads the machine code needed for the external functions - a process known as *dynamic linking*. 
   2. Dynamic linking makes executable files smaller and saves disk space, because one copy of a library can be shared between multiple programs. 
   3. Furthermore, most operating systems allows one copy of a shared library in memory to be used by all running programs, thus, saving memory.
   4. The shared library codes can be upgraded without the need to recompile your program.

## 2. GNU Make

The "`make`" utility automates the mundane aspects of building executable from source code. "`make`" uses a so-called `makefile`, which contains rules on how to build the executables.

Running `make` without argument starts the target "`all`" in the `makefile`. A makefile consists of a set of rules. 

A rule consists of 3 parts: a target, a list of pre-requisites and a command, as follows:

```makefile
target: pre-req-1 pre-req-2 ...
	command
```

- The *target* and *pre-requisites* are separated by a colon (`:`). 
- The *command* must be preceded by a tab (NOT spaces).

**exp**.

##### Variables

A variable begins with a `$` and is enclosed within parentheses `(...)` or braces `{...}`. 

Single character variables do not need the parentheses. For example, `$(CC)`, `$(CC_FLAGS)`, `$@`, `$^`.

##### Automatic Variables

Automatic variables are set by make after a rule is matched. There include:

- `$@`: the target filename.
- `$*`: the target filename without the file extension.
- `$<`: the first prerequisite filename.
- `$^`: the filenames of all the prerequisites, separated by spaces, discard duplicates.
- `$+`: similar to `$^`, but includes duplicates.
- `$?`: the names of all prerequisites that are newer than the target, separated by spaces.

```makefile
all: hello.exe

hello.exe: hello.o
	 gcc -o hello.exe hello.o

hello.o: hello.c
	 gcc -c hello.c
     
clean:
	 rm hello.o hello.exe
```

or

```makefile
all: hello.exe
 
# $@ matches the target; $< matches the first dependent
hello.exe: hello.o
	gcc -o $@ $<

hello.o: hello.c
	gcc -c $<
     
clean:
	rm hello.o hello.exe
```

1. In the above example, the rule "`all`" has a pre-requisite "`hello.exe`". `make` cannot find the file "`hello.exe`", so it looks for a rule to create it. 
2. The rule "`hello.exe`" has a pre-requisite "`hello.o`". Again, it does not exist, so `make` looks for a rule to create it. 
3. The rule "`hello.o`" has a pre-requisite "`hello.c`". `make` checks that "`hello.c`" exists and it is newer than the target (which does not exist). It runs the command "`gcc -c hello.c`". The rule "`hello.exe`" then run its command "`gcc -o hello.exe hello.o`". 
4. Finally, the rule "`all`" does nothing.

More importantly, if the pre-requisite is not newer than than target, the command will not be run. In other words, the command will be run only if the target is out-dated compared with its pre-requisite.

You can also specify the target to be made in the `make` command. For example, the target "`clean`" removes the "`hello.o`" and "`hello.exe`". 

You can then run the `make` without target, which is the same as "`make all`".

```makefile
> make clean
rm hello.o hello.exe
 
> make
gcc -c hello.c
gcc -o hello.exe hello.o
```

!!! bug "No targets specified and no makefile found. Stop."
	使用自定义makefile注意两点，一个是需要cd到makefile所在的目录，一个是makefile命名为Makefile或makefile，而不是MAKEFILE

#### 2.2 More on Makefile

##### Syntax of Rules

A general syntax for the rules is:

```makefile
target1 [target2 ...]: [pre-req-1 pre-req-2 ...]
	[command1
	 command2
	 ......]
```

The rules are usually organized in such as way the more general rules come first. 

The overall rule is often name "`all`", which is the default target for `make`.

##### Phony Targets (or Artificial Targets)

A target that does not represent a file is called a phony target. For example, the "`clean`" in the above example, which is just a label for a command. 

If the target is a file, it will be checked against its pre-requisite for out-of-date-ness. 

Phony target is always out-of-date and its command will be run. 

The standard phony targets are: `all`, `clean`, `install`.

#### 2.3 A Sample Makefile

This sample makefile is extracted from Eclipse's "C/C++ Development Guide -Makefile".

```makefile
# A sample Makefile
# This Makefile demonstrates and explains 
# Make Macros, Macro Expansions,
# Rules, Targets, Dependencies, Commands, Goals
# Artificial Targets, Pattern Rule, Dependency Rule.

# Comments start with a # and go to the end of the line.

# Here is a simple Make Macro.
LINK_TARGET = test_me.exe

# Here is a Make Macro that uses the backslash to extend to multiple lines.
OBJS =  \
 Test1.o \
 Test2.o \
 Main.o

# Here is a Make Macro defined by two Macro Expansions.
# A Macro Expansion may be treated as a textual replacement of the Make Macro.
# Macro Expansions are introduced with $ and enclosed in (parentheses).
REBUILDABLES = $(OBJS) $(LINK_TARGET)

# Here is a simple Rule (used for "cleaning" your build environment).
# It has a Target named "clean" (left of the colon ":" on the first line),
# no Dependencies (right of the colon),
# and two Commands (indented by tabs on the lines that follow).
# The space before the colon is not required but added here for clarity.
clean : 
  rm -f $(REBUILDABLES)
  echo Clean done

# There are two standard Targets your Makefile should probably have:
# "all" and "clean", because they are often command-line Goals.
# Also, these are both typically Artificial Targets, because they don't typically
# correspond to real files named "all" or "clean".  

# The rule for "all" is used to incrementally build your system.
# It does this by expressing a dependency on the results of that system,
# which in turn have their own rules and dependencies.
all : $(LINK_TARGET)
  echo All done

# There is no required order to the list of rules as they appear in the Makefile.
# Make will build its own dependency tree and only execute each rule only once
# its dependencies' rules have been executed successfully.

# Here is a Rule that uses some built-in Make Macros in its command:
# $@ expands to the rule's target, in this case "test_me.exe".
# $^ expands to the rule's dependencies, in this case the three files
# main.o, test1.o, and  test2.o.
$(LINK_TARGET) : $(OBJS)
  g++ -g -o $@ $^

# Here is a Pattern Rule, often used for compile-line.
# It says how to create a file with a .o suffix, given a file with a .cpp suffix.
# The rule's command uses some built-in Make Macros:
# $@ for the pattern-matched target
# $< for the pattern-matched dependency
%.o : %.cpp
  g++ -g -o $@ -c $<

# These are Dependency Rules, which are rules without any command.
# Dependency Rules indicate that if any file to the right of the colon changes,
# the target to the left of the colon should be considered out-of-date.
# The commands for making an out-of-date target up-to-date may be found elsewhere
# (in this case, by the Pattern Rule above).
# Dependency Rules are often used to capture header file dependencies.
Main.o : Main.h Test1.h Test2.h
Test1.o : Test1.h Test2.h
Test2.o : Test2.h

# Alternatively to manually capturing dependencies, several automated
# dependency generators exist.  Here is one possibility (commented out)...
# %.dep : %.cpp
#   g++ -M $(FLAGS) $< > $@
# include $(OBJS:.o=.dep)
```