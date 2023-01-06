import pandas as pd
import matplotlib.pyplot as plt


def func_pie():
    def my_autopct(pct):
        return ('%.1f' % pct + '%') if pct > 2 else ''

    labels = ['Cross Entropy', 'Mse Loss', 'Binary Cross Entropy With Logits', "L1 Loss", "Smooth L1 Loss",
              "Binary Cross Entropy", "Ctc Loss", "KL Div", "Margin Rankding Loss"]
    sizes = [594, 312, 98, 21, 19, 10, 2, 1, 1]
    explode = (0.02, 0.01, 0, 0, 0, 0, 0, 0, 0)  # 元素凸出距离
    colors = ['tomato', 'lightskyblue', 'goldenrod', 'green', 'y']
    # 饼图绘制函数
    plt.figure(figsize=(13, 6))
    plt.pie(sizes, explode=explode, radius=0.3, labels=labels, colors=colors, \
            autopct=my_autopct, shadow=False, pctdistance=0.8, \
            startangle=90, textprops={'fontsize': 8, 'color': 'w'})
    # plt.title('')
    plt.axis('equal')
    plt.legend(loc=1)
    plt.savefig('age.png', dpi=600)


print(func_pie())