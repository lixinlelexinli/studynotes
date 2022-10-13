https://blog.csdn.net/qq_36560894/article/details/105317973?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-1&spm=1001.2101.3001.4242

文章目录
参考
目的
计算原理
Python实现
参考
https://www.cnblogs.com/liugl7/p/10874958.html
参考上文的原理以及框架，在其基础上做了一定的修改及提炼

目的
我们在做图像领域的任务或者项目时，通常需要对图像进行归一化处理，使输入网络的数据呈现一个稳定的分布。这就需要我们求得图像各通道（R、G、B）的均值以及方差。

计算原理
一般计算方差和均值需要两步，先求得所有图片各通道的均值，然后再遍历一边数据集，求得各通道的方差，这样做会很耗时。

但如果把所有数据全部读进来再计算方差和均值，这种方法又很占内存，对配置要求较高，搞不好还会死机。

只需要遍历一边的方法：先看方差的公式推导
step 1：

![在这里插入图片描述](F:%5Cgithub%5Cgithubio%5Cstudynotes%5Cpython%5Crgb%E5%9B%BE%E7%89%87%E5%90%84%E9%80%9A%E9%81%93%E5%9D%87%E5%80%BC%E6%96%B9%E5%B7%AE.assets%5C20200404215451878.png)

step 2：

![在这里插入图片描述](F:%5Cgithub%5Cgithubio%5Cstudynotes%5Cpython%5Crgb%E5%9B%BE%E7%89%87%E5%90%84%E9%80%9A%E9%81%93%E5%9D%87%E5%80%BC%E6%96%B9%E5%B7%AE.assets%5C20200404215753628.png)step 3：

![在这里插入图片描述](F:%5Cgithub%5Cgithubio%5Cstudynotes%5Cpython%5Crgb%E5%9B%BE%E7%89%87%E5%90%84%E9%80%9A%E9%81%93%E5%9D%87%E5%80%BC%E6%96%B9%E5%B7%AE.assets%5C20200404220110434.png)

其中x为像素值，x’为均值，N为像素总个数，x’=sum(x)/N。

其实学过概率论与数理统计的同学，应该很容易发现这个就是V(x) = E(x2) - E(x)2的方差计算公式。

说明：
要求得方差和均值，只需要遍历一遍数据集：读取一张图片，保存当前图片的每个通道像素值的和以及像素值平方的和，利用得到的值再进一步求得数据集的均值和方差。

Python实现
（这里是计算均值和标准差的代码， 方差是标准差的平方）

```python
import os
import numpy as np
import cv2

files_dir = 'data/Images/'
files = os.listdir(files_dir)

R = 0.
G = 0.
B = 0.
R_2 = 0.
G_2 = 0.
B_2 = 0.
N = 0

for file in files:
    img = cv2.imread(files_dir+file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.array(img)
    h, w, c = img.shape
    N += h*w

    R_t = img[:, :, 0]
    R += np.sum(R_t)
    R_2 += np.sum(np.power(R_t, 2.0))

    G_t = img[:, :, 1]
    G += np.sum(G_t)
    G_2 += np.sum(np.power(G_t, 2.0))

    B_t = img[:, :, 2]
    B += np.sum(B_t)
    B_2 += np.sum(np.power(B_t, 2.0))

R_mean = R/N
G_mean = G/N
B_mean = B/N

R_std = np.sqrt(R_2/N - R_mean*R_mean)
G_std = np.sqrt(G_2/N - G_mean*G_mean)
B_std = np.sqrt(B_2/N - B_mean*B_mean)

print("R_mean: %f, G_mean: %f, B_mean: %f" % (R_mean, G_mean, B_mean))
print("R_std: %f, G_std: %f, B_std: %f" % (R_std, G_std, B_std))
```

