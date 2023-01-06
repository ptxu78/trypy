# 此demo演示 检查路透社新闻数据集
import numpy as np
import lda
import lda.datasets

# X是一个文档术语矩阵 (稀疏矩阵也可以被接受)
# DocumentTerm Matrix: 是每个Document中每个term（单词，或是词汇表vocab）出现的次数
X = lda.datasets.load_reuters()
# print(X)
# print(type(X))
# print(X.shape) # 395 * 4258
# print(X.sum())

# vocab 词汇表 是长度为4258的字符串元组
vocab = lda.datasets.load_reuters_vocab()
# print(vocab)
# print(type(vocab))
# print(vocab.__len__())

# titles 标题集
titles = lda.datasets.load_reuters_titles()
# print(titles)
# print(type(titles))
# print(titles.__len__())


# 设定提取主题数量, 迭代次数, 随机状态数(写1即可)
model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
# 开始迭代
model.fit(X)  # model.fit_transform(X) is also available

topic_word = model.topic_word_  # model.components_ also works
print(topic_word)
print(type(topic_word))
print(topic_word.__len__())

n_top_words = 8
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))

