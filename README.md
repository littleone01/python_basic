## 背景

`MovieLens`数据集是一个广泛用来研究推荐系统算法的一个数据集。这个数据集包含了来自[电影推荐网站](https://movielens.org/)多年积累的数据。我们将基于这个数据集练习数据的处理和分析。

从 [grouplens](http://files.grouplens.org/datasets/movielens/ml-latest-small.zip) 下载数据集 MovieLens 1M Dataset。
数据集包含6个文件：
- `tags.csv` 用户给电影打的标签:
    - userId
    - movieId
    - tag
    - timestamp
- `ratings.csv` 用户给电影的评分:
    - userId
    - movieId
    - rating
    - timestamp
- `movies.csv` 电影信息:
    - movieId
    - title
    - genres
- `links.csv` 链接到其他资源的`id`:
    - movieId
    - imdbId
    - tmbdId

## 需求

读取rates.csv文件，完成：

1. 将每1分做为一档，电影的评分共分为5档，(0:1], (1,2], (2, 3], (3, 4], (4, 5], 通过pandas包求出每个评分档共有多少部电影

2. 添加一个comment列，对4分以上的电影标‘推荐’，其他标‘不推荐’，输出到一个comment.csv中

## 提交方式

github工程源代码文件链接+结果截图
