import matplotlib.pyplot as plt
import numpy as np

# 数据
k_values = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
ic_times = [0.4165, 0.4186, 0.4527, 0.4532, 0.4671, 0.4832, 0.4869, 0.5203, 0.5467, 0.5389]
lt_times = [0.6010, 0.6410, 0.6503, 0.6768, 0.7269, 0.6979, 0.7137, 0.8428, 0.7300, 0.7485]

# 绘制图形
plt.figure(figsize=(10, 6))
plt.plot(k_values, ic_times, label="IC Model Time (s)", marker="o")
plt.plot(k_values, lt_times, label="LT Model Time (s)", marker="s")

# 图表设置
plt.title("Running Time Comparison Across k Values")
plt.xlabel("k (Number of Seeds)")
plt.ylabel("Running Time (s)")
plt.legend()
plt.grid(alpha=0.5, linestyle="--")
plt.xticks(k_values)
plt.show()
