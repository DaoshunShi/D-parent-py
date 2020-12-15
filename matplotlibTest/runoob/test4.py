import numpy as np
from matplotlib import pyplot as plt
import matplotlib

# fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径

x = np.arange(1, 11)
y = 2 * x + 5
plt.rcParams['font.family']=['STFangsong']
plt.title("菜鸟教程 - 测试")

# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("x 轴")
plt.ylabel("y 轴")
plt.plot(x, y)
plt.show()
