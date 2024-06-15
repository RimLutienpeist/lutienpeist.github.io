p ↔ q: q\p if and only if q

tautology: 同义反复，即命题的左右式本质上是一样的

列真值表时，每一个属性实际上只有T和F两种情况

> a) [¬p ∧ (p ∨ q)] → q 
>
> b) [(p → q) ∧ (q → r)] → (p → r) 
>
> c) [p ∧ (p → q)] → q 
>
> d) [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r
>
> Show that each conditional statement in Exercise 10 is a tautology without using truth tables.
>
> 1. [¬p∧(p∨q)] → q ≡ ¬[¬p∧(p∨q)]∨q ≡ ¬¬p∨¬(p∨q)]∨q ≡ p∨¬(p∨q)∨q ≡ (p∨q)∨¬(p∨q) ≡ T
> 2. 

合取范式（ conjunctive normal form (CNF)）
任何命题公式，最终都能够化成的形式，这种先 ∨ 析 取  再 ∧ 合 取  的范式，被称为 “ 合取范式”。

析取范式（disjunctive normal form (DNF)）
任何命题公式，最终都能够化成 的形式，这种先 ∧ 合取 再 ∨ 析 取  的范式，被称为 “析取范式”。
![image-20240413174220231](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240413174220231.png)

![在这里插入图片描述](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/8f969e2fc32248f9800880902e80d803.png)

简化方法：在一个 **合取范式的** 子句（**clause**）中，同一个逻辑 **literal** 只出现一次。

![例1](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/20190802173754399.PNG)

![image-20240413180955677](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/image-20240413180955677.png)

\9. Let P (x) be the statement “x can speak Russian” and let Q(x) be the statement “x knows the computer language C++.” Express each of these sentences in terms of P (x), Q(x), quantifiers, and logical connectives. The domain for quantifiers consists of all students at your school. 

a) There is a student at your school who can speak Russian and who knows C++. 

b) There is a student at your school who can speak Russian but who doesn’t know C++. 

c) Every student at your school either can speak Russian or knows C++. 

d) No student at your school can speak Russian or knows C++.

. a) ∃x(P (x) ∧ Q(x)) 	b) ∃x(P (x) ∧ ¬Q(x)) 	c) ∀x(P (x)∨Q(x)) 	d) ∀x¬(P (x) ∨ Q(x)) 
