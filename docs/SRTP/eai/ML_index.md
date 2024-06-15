> 原文
>
> [一文看懂机器学习「3种学习方法+7个实操步骤+15种常见算法」 (easyai.tech)](https://easyai.tech/ai-definition/machine-learning/)

> 定位
>
> 本文属于科普文，主要介绍概念

# 机器学习 – machine learning | ML

> Field of study that gives computers the ability to learn without being explicitly programmed.
>
> 机器学习 研究和构建的 是一类特殊算法（**而非某一个特定的算法**），能够让计算机自己在数据中学习从而进行预测。

机器学习包含了很多种不同的算法，深度学习就是其中之一，其他方法包括决策树，聚类，贝叶斯等。

![人工智能、机器学习、深度学习的关系](https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/ai-ml-dl.png)

> **深度学习**
>
> 深度学习的灵感来自大脑的结构和功能，即许多神经元的互连。
>
> 人工神经网络（ANN）是模拟大脑生物结构的算法。

## 机器学习的基本思路

> 抽象->求解->评估

1. 把现实生活中的问题**抽象成数学模型**，并且很清楚模型中**不同参数的作用**
2. 利用**数学方法**对这个数学模型进行求解，从而解决现实生活中的问题
3. **评估**这个数学模型，是否真正的解决了现实生活中的问题，解决的如何？

> 不是所有问题都可以转换成数学问题的。
>
> 那些没有办法转换的现实问题 AI 就没有办法解决。
>
> 同时最难的部分也就是把现实问题转换为数学问题这一步。

## 机器学习的原理

> 下面以监督学习为例

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/ml-step-3.png" alt="机器学习原理说明3" style="zoom: 33%;" />

- 认字的卡片在机器学习中叫——**训练集**
- “一条横线，两条横线”这种区分不同汉字的属性叫——**特征**
- 不断学习的过程叫——**建模**
- 学会了识字后总结出来的规律叫——**模型**

**通过训练集，不断识别特征，不断建模，最后形成有效的模型，这个过程就叫“机器学习”！**

## 机器学习的基本方法

机器学习根据训练方法大致可以分为3大类：

1. 监督学习
2. 非监督学习
3. 强化学习

除此之外，“半监督学习”之类的都是基于上面3类的变种，本质没有改变。

### 监督学习

监督学习是指我们给算法一个数据集，并且给定正确答案。机器通过数据来**学习正确答案**的计算方法。

> **举个🌰**
>
> 我们准备了一大堆猫和狗的照片，我们想让机器学会如何识别猫和狗。
>
> 当我们使用监督学习的时候，我们需要给这些照片打上**标签**（即“正确答案”），即哪些是猫，哪些是狗。
>
> 机器通过大量学习，就可以学会在新照片中认出猫和狗。

这种通过大量人工打标签来帮助机器学习的方式就是监督学习。这种学习方式效果好，但成本高。

Detail：[一文看懂监督学习（基本概念+4步流程+9个典型算法）- 产品经理的人工智能学习库 (easyai.tech)](https://easyai.tech/ai-definition/supervised-learning/)

**非监督学习**

非监督学习中，给定的数据集没有“正确答案”，所有的数据都是一样的。

无监督学习的**任务**是从给定的数据集中，**挖掘出潜在的结构**。

> **举个🌰**
>
> 我们把一堆猫和狗的照片给机器，不给这些照片打任何标签，但是我们希望机器能够将这些照片分分类。
>
> 与监督学习一样，最后都会分为两类，但是注意，非监督学习只是分类，不会识别。
>
> 虽然照片分为了猫和狗，但是机器并不知道哪个是猫，哪个是狗。

Detail：[一文看懂无监督学习（基本概念+使用场景+2类典型算法） (easyai.tech)](https://easyai.tech/ai-definition/unsupervised-learning/)

**强化学习**

强化学习更接近生物学习的本质，因此有望获得更高的智能。

它关注的是**智能体**如何**在环境中采取一系列行为**，从而获得**最大**的累积回报。

通过强化学习，一个智能体应该知道在什么状态下应该采取什么行为。

Detail：[一文看懂什么是强化学习？（基本概念+应用场景+主流算法） (easyai.tech)](https://easyai.tech/ai-definition/reinforcement-learning/)

## 机器学习实操的7个步骤

机器学习在实际操作层面一共分为7步：

1. 收集数据：十分重要，**数据的数量和质量直接决定了预测模型的好坏**
2. 数据准备：数据清洗等工作
   - 当数据本身没有什么问题后，将数据分成3个部分：训练集（60%）、验证集（20%）、测试集（20%），用于后面的验证和评估工作。
3. 选择一个模型：有些非常适合图像数据，有些非常适合于序列（如文本或音乐），有些用于数字数据，有些用于基于文本的数据。
4. 训练：这个过程就不需要人来参与的，机器独立就可以完成，整个过程就好像是在做算术题。
   - 因为机器学习的本质就是**将问题转化为数学问题，然后解答数学题的过程**。
5. 评估：之前预留的验证集和测试集发挥作用的地方。评估的指标主要有 准确率、召回率、F值。
   - 看到模型如何对尚未看到的数是如何做预测的
6. 参数调整
   - 当我们进行训练时，我们隐含地假设了一些参数，我们可以通过认为的调整这些参数让模型表现的更出色。
7. 预测（开始使用）
   - 我们上面的6个步骤都是为了这一步来服务的。这也是机器学习的价值。

Detail：https://www.youtube.com/watch?v=nKW8Ndu7Mjw

<img src="https://raw.githubusercontent.com/RimLutienpeist/image-hosting/main/3dataset.png" alt="数据要分为3个部分：训练集、验证集、测试集" style="zoom:33%;" />

## 15种经典机器学习算法

| 算法                                                         | 训练方式   |
| :----------------------------------------------------------- | :--------- |
| [线性回归](https://easyai.tech/ai-definition/linear-regression/) | 监督学习   |
| [逻辑回归](https://easyai.tech/ai-definition/logistic-regression/) | 监督学习   |
| [线性判别分析](https://easyai.tech/ai-definition/linear-discriminant-analysis/) | 监督学习   |
| [决策树](https://easyai.tech/ai-definition/decision-tree/)   | 监督学习   |
| [朴素贝叶斯](https://easyai.tech/ai-definition/naive-bayes-classifier/) | 监督学习   |
| [K邻近](https://easyai.tech/ai-definition/k-nearest-neighbors/) | 监督学习   |
| [学习向量量化](https://easyai.tech/ai-definition/learning-vector-quantization/) | 监督学习   |
| [支持向量机](https://easyai.tech/ai-definition/svm/)         | 监督学习   |
| [随机森林](https://easyai.tech/ai-definition/random-forest/) | 监督学习   |
| [AdaBoost](https://easyai.tech/ai-definition/adaboost/)      | 监督学习   |
| 高斯混合模型                                                 | 非监督学习 |
| [限制波尔兹曼机](https://easyai.tech/ai-definition/restricted-boltzmann-machine/) | 非监督学习 |
| [K-means 聚类](https://easyai.tech/ai-definition/k-means-clustering/) | 非监督学习 |
| 最大期望算法                                                 | 非监督学习 |