import matplotlib.pyplot as plt
import numpy as np

# 数据
data = {
    "Dataset": ["amazon0601", "web-Google", "cit-Patents", "soc-Epinions1", "email-Eu-core", "soc-Slashdot0811", "wiki-Vote", "as-skitter"],
    "Edges": [3387388, 5105039, 16518948, 508837, 25571, 905468, 103689, 11095298],
    "DegreeDiscountIC": [0.1844, 0.4967, 2.7362, 0.0492, 0.0052, 0.0686, 0.0140, 1.4084],
    "DegreeDiscountLT": [0.3163, 0.6597, 3.3176, 0.0638, 0.0051, 0.0839, 0.0169, 1.8668]
}

# 绘图
x = np.arange(len(data["Dataset"]))
width = 0.35  # 柱宽

fig, ax1 = plt.subplots(figsize=(12, 6))

# 边的数量（柱状图）
bar1 = ax1.bar(x - width/2, data["Edges"], width, label="Edges", color="skyblue")
ax1.set_ylabel("Number of Edges")
ax1.set_xlabel("Dataset")
ax1.set_title("Running Time")
ax1.set_xticks(x)
ax1.set_xticklabels(data["Dataset"], rotation=45)
ax1.legend(loc="upper left")

# 添加次坐标轴用于运行时间
ax2 = ax1.twinx()

# IC 和 LT 模型运行时间（折线图）
line1 = ax2.plot(x, data["IC Time (s)"], label="IC Time (s)", marker="o", color="green")
line2 = ax2.plot(x, data["LT Time (s)"], label="LT Time (s)", marker="s", color="orange")
ax2.set_ylabel("Running Time (s)")
ax2.legend(loc="upper right")

# 显示图例和网格
fig.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
