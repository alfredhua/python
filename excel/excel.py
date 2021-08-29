import pandas as pd 

df=pd.read_csv('website.csv')
# df.info()        # 数据类型，内存消耗等信息
# df.describe()    # 统计特征，均值方差等

df.head(n=5)  # 可以添加参数n，表示显示几行
print(df.head(n=5))

print(df.tail())