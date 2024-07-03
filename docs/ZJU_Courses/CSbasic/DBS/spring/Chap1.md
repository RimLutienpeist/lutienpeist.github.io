# Chap 1: Introduction

> 本章的难点是会出现大量专业名词。
>
> 本章内容不用特别记，大致看一下即可。
>
> 本部分笔记主要是介绍各自数据库系统里的概念，每个都简单讲一下，算是为后面的内容打概念基础。多看下专业术语（行话）。

# 春学期

> 春学期是些比较基础的

> **英文单词**
>
> 1. interrelated 相关的
> 2. retrieve 取回
> 3. mechanisms 机制
> 4. manipulation 操纵
> 5. enterprise 公司
> 6. concurrency 并发，同时发生
> 7. Parallelism 并行，同时执行
> 8. anomalous 异常
> 9. duplication 重复
> 10. balance  余额

## Outline

- 数据库基本概念、基本特征、基本应用
- ~~数据库发展历史~~（考试不考）

## *何为Database

> Database的中文为‘数据库’。因早期翻译问题，“数据库”其实更适合翻译“data warehouse（数据仓库）”，而database更符合“数据基地”一说，基地与仓库显然功能大大不同。

Database is a collection of **interrelated（相互关联的）** data about a enterprise, which is managed by a **DBMS(Database Management System)**.

数据库系统是一个在OS之上的软件。

!!!note "文件vs数据库"
	在C语言中，我们需要存储数据往往是存入文件，但是各文件之间是“孤立的”，是没有相互的联系的，它们之间的关系只有你知道，这是相当麻烦的事。而数据库解决了这一问题。	
	![image-20240124160028648](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240124160028648.png)

The primary goal of a **DBMS** is to provide a way to store and retrieve database information that is both convenient and efficient.

Management of data involves both **defining structures** for storage of information and **providing mechanisms** for the manipulation of information.

The **database system** must ensure the safety of the information stored,despite system crashes or attempts at unauthorized access.

If data are to be shared among several users, the system must provide **concurrency control** mechanisms to avoid possible anomalous results.

> 这里不考定义，了解内容
>
> ~~有讨论要写，要举数据库例子~~

## *Database AppIications

> 没有数据库就没有信息时代
>
> 数据库储存数据方式很多
>
> 我们这课最重要的是学关系型数据库，以表格形式管理

## Purpose of Database Systems

In the early days, database applications were built directly on top of file systems, which leads to: 

- **Data redundancy（数据冗余）** and **inconsistency（不一致）**
  - Multiple file formats, duplication of information in different files
  - 一处改了其它处也要改
- **Data isolation** — multiple files and formats
  - 数据各自孤立，没有一个有效的统一结构
- Difficulty in **accessing data（存取数据）**
  - Need to write a new program to carry out each new task

### 如果没有数据库系统

#### Integrity problem

- Integrity constraints become "buried" in program code rather than being stated explicitly（显式的）
- Example: "account balance>=1"
- Hard to add new constraints or change existing ones

#### Atomicity problem

An atomic transaction is an indivisible and irreducible series of database operations such that either all occur, or none occur.

Failures may leave database in an inconsistent state with partial updates carried out

Example: Transfer of funds from one account to another should either complete or not happen at all

> 43:00左右，重新听一下没听到

#### Concurrent access anomalies

- Concurrent access needed for performance
- Uncontrolled concurrent accesses can lead to inconsistencies
- Example: Two people reading a balance (say 100) and updating it by saving money (say 50 each) at the same time

#### Security problems

- Hard to provide user access to some, but not all, data
- Authentication（认证）
- Privilege（权限）
- Audit（审计）
  - 权力监督，监督管理员

### Characteristics of Databases

- data persistence(数据持久性)
- convenience in accessing data(数据访问便利性)
- data integrity（数据完整性）
- concurrency control for multiple users（多用户并发控制 ）
- failure recovery（故障恢复）
- security control（安全控制）

> XML专门描述半结构化内容
>
> 本课XML不做要求

![image-20240226143033076](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226143033076.png)

> 关系的形式即表格的形式

## View of Data

**Three-level** abstraction of databases

![image-20240226143945870](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226143945870.png)

优点：

- 
  Hide the complexities 
- Enhance the adaptation to changes

不同level间通过mapping连接。不同level有相对的独立性，增强了第二个优点

## schema and instance

> 数据库系统里的两个专业术语，在OO里叫class和object，C++里叫type和variable/value

![image-20240226144541265](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226144541265.png)

## Database Languages

![image-20240226144834649](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226144834649.png)

### Data Definition Language (DDL)

![image-20240226145012147](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226145012147.png)

用于定义数据的数据为元数据，也存储在数据库里

### Data Manipulation Language (DML)

![image-20240226145543995](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226145543995.png)

> 过程式三大结构：顺序，分支，循环
>
> 写陈述式要摈弃过程式的写法

### SQL Query Language

![image-20240226145908449](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226145908449.png)

## Database Access from Application Program

![image-20240226150733092](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226150733092.png)

## Database Design

![image-20240226151033652](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226151033652.png)

> entity 实体
>
> 关系有一对一，一对多，多对多

> 后面的是夏学期内容，开始难了

# 夏学期

## Database Engine

![image-20240226152257502](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226152257502.png)

### Storage Manager

![image-20240226152801561](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226152801561.png)

![image-20240226154028062](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226154028062.png)

> 大作业是做一个简单的数据库引擎

### Query Processor

![image-20240226154011706](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226154011706.png)

### Query Procession

![image-20240226153952859](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226153952859.png)

### Transaction Management

![image-20240226153926058](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226153926058.png)

## Database User

![image-20240226153826958](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226153826958.png)

![image-20240226154218698](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226154218698.png)

![image-20240226154230500](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226154230500.png)

### Database Administrator（DBA）

![image-20240226154256764](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240226154256764.png)

**Chap1	END**