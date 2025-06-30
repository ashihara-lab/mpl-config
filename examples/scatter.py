#!/usr/bin/env python3
"""
Scatter plot examples
Comparison of mpl_config presets for academic and presentation use
"""

# %% [markdown]
# # 散布図プロット例
#
# mpl_configの各プリセットを使った散布図の例を示します。
# クラスター解析、相関分析、エラーバー付きプロットなど。

# %% ライブラリのインポートとセットアップ
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Import mpl_config from parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mpl_config

# 出力ディレクトリを作成
os.makedirs('examples/output', exist_ok=True)

figsize = (10, 8)

# %% サンプルデータの生成
np.random.seed(42)
n_points = 200

# 3つのクラスターデータ
cluster1_x = np.random.normal(2, 0.8, n_points//3)
cluster1_y = np.random.normal(2, 0.8, n_points//3)

cluster2_x = np.random.normal(6, 1.0, n_points//3)
cluster2_y = np.random.normal(6, 1.0, n_points//3)

cluster3_x = np.random.normal(4, 1.2, n_points//3)
cluster3_y = np.random.normal(1, 0.6, n_points//3)

# 相関データ
x_corr = np.random.normal(0, 1, 100)
y_corr = 0.8 * x_corr + np.random.normal(0, 0.3, 100)

print("サンプルデータ（クラスター、相関）を生成しました")

# %% [markdown]
# ## 1. Paper プリセット - 4つのサブプロット

# %% Paper プリセットでの散布図
mpl_config.apply_style('paper')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=figsize)

# 1. クラスター散布図
ax1.scatter(cluster1_x, cluster1_y, alpha=0.7, label='Cluster 1', s=50)
ax1.scatter(cluster2_x, cluster2_y, alpha=0.7, label='Cluster 2', s=50)
ax1.scatter(cluster3_x, cluster3_y, alpha=0.7, label='Cluster 3', s=50)
ax1.set_xlabel('X Coordinate')
ax1.set_ylabel('Y Coordinate')
ax1.set_title('Cluster Analysis')
ax1.legend()
ax1.grid(True, alpha=plt.rcParams['grid.alpha'])

# 2. 相関散布図
ax2.scatter(x_corr, y_corr, alpha=0.6, s=30, color='red')
# 回帰直線を追加
z = np.polyfit(x_corr, y_corr, 1)
p = np.poly1d(z)
x_line = np.linspace(x_corr.min(), x_corr.max(), 100)
ax2.plot(x_line, p(x_line), "r--", alpha=0.8, linewidth=2)
ax2.set_xlabel('Variable X')
ax2.set_ylabel('Variable Y')
ax2.set_title('Correlation (r≈0.8)')
ax2.grid(True, alpha=plt.rcParams['grid.alpha'])

# 3. 可変サイズ散布図
sizes = np.random.uniform(20, 200, len(cluster1_x))
ax3.scatter(cluster1_x, cluster1_y, s=sizes, alpha=0.6, c=sizes, cmap='viridis')
ax3.set_xlabel('X Coordinate')
ax3.set_ylabel('Y Coordinate')
ax3.set_title('Variable Size Scatter Plot')
ax3.grid(True, alpha=plt.rcParams['grid.alpha'])

# 4. エラーバー付き散布図
x_err = np.linspace(1, 10, 10)
y_err = 2 * x_err + np.random.normal(0, 1, 10)
xerr = np.random.uniform(0.1, 0.3, 10)
yerr = np.random.uniform(0.5, 1.5, 10)

ax4.errorbar(x_err, y_err, xerr=xerr, yerr=yerr, 
             fmt='o', markersize=6, capsize=5, alpha=0.8)
ax4.set_xlabel('Measured X')
ax4.set_ylabel('Measured Y')
ax4.set_title('Scatter Plot with Error Bars')
ax4.grid(True, alpha=plt.rcParams['grid.alpha'])

plt.tight_layout()
plt.savefig('examples/output/scatter_paper.png', dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("Paper preset 散布図を保存しました: examples/output/scatter_paper.png")

# %% [markdown]
# ## 2. Presentation プリセット

# %% Presentation プリセットでの散布図
mpl_config.apply_style('presentation')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=figsize)

# 同じ内容をプレゼンテーション用スタイルで描画
ax1.scatter(cluster1_x, cluster1_y, alpha=0.7, label='Cluster 1', s=50)
ax1.scatter(cluster2_x, cluster2_y, alpha=0.7, label='Cluster 2', s=50)
ax1.scatter(cluster3_x, cluster3_y, alpha=0.7, label='Cluster 3', s=50)
ax1.set_xlabel('X Coordinate')
ax1.set_ylabel('Y Coordinate')
ax1.set_title('Cluster Analysis')
ax1.legend()
ax1.grid(True, alpha=plt.rcParams['grid.alpha'])

ax2.scatter(x_corr, y_corr, alpha=0.6, s=30, color='red')
ax2.plot(x_line, p(x_line), "r--", alpha=0.8, linewidth=2)
ax2.set_xlabel('Variable X')
ax2.set_ylabel('Variable Y')
ax2.set_title('Correlation (r≈0.8)')
ax2.grid(True, alpha=plt.rcParams['grid.alpha'])

ax3.scatter(cluster1_x, cluster1_y, s=sizes, alpha=0.6, c=sizes, cmap='viridis')
ax3.set_xlabel('X Coordinate')
ax3.set_ylabel('Y Coordinate')
ax3.set_title('Variable Size Scatter Plot')
ax3.grid(True, alpha=plt.rcParams['grid.alpha'])

ax4.errorbar(x_err, y_err, xerr=xerr, yerr=yerr, 
             fmt='o', markersize=6, capsize=5, alpha=0.8)
ax4.set_xlabel('Measured X')
ax4.set_ylabel('Measured Y')
ax4.set_title('Scatter Plot with Error Bars')
ax4.grid(True, alpha=plt.rcParams['grid.alpha'])

plt.tight_layout()
plt.savefig('examples/output/scatter_presentation.png', dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("Presentation preset 散布図を保存しました: examples/output/scatter_presentation.png")

# %% [markdown]
# ## 3. Default プリセット

# %% Default プリセットでの散布図
mpl_config.apply_style('default')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=figsize)

ax1.scatter(cluster1_x, cluster1_y, alpha=0.7, label='Cluster 1', s=50)
ax1.scatter(cluster2_x, cluster2_y, alpha=0.7, label='Cluster 2', s=50)
ax1.scatter(cluster3_x, cluster3_y, alpha=0.7, label='Cluster 3', s=50)
ax1.set_xlabel('X Coordinate')
ax1.set_ylabel('Y Coordinate')
ax1.set_title('Cluster Analysis')
ax1.legend()
ax1.grid(True, alpha=plt.rcParams['grid.alpha'])

ax2.scatter(x_corr, y_corr, alpha=0.6, s=30, color='red')
ax2.plot(x_line, p(x_line), "r--", alpha=0.8, linewidth=2)
ax2.set_xlabel('Variable X')
ax2.set_ylabel('Variable Y')
ax2.set_title('Correlation (r≈0.8)')
ax2.grid(True, alpha=plt.rcParams['grid.alpha'])

ax3.scatter(cluster1_x, cluster1_y, s=sizes, alpha=0.6, c=sizes, cmap='viridis')
ax3.set_xlabel('X Coordinate')
ax3.set_ylabel('Y Coordinate')
ax3.set_title('Variable Size Scatter Plot')
ax3.grid(True, alpha=plt.rcParams['grid.alpha'])

ax4.errorbar(x_err, y_err, xerr=xerr, yerr=yerr, 
             fmt='o', markersize=6, capsize=5, alpha=0.8)
ax4.set_xlabel('Measured X')
ax4.set_ylabel('Measured Y')
ax4.set_title('Scatter Plot with Error Bars')
ax4.grid(True, alpha=plt.rcParams['grid.alpha'])

plt.tight_layout()
plt.savefig('examples/output/scatter_default.png', dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("Default preset 散布図を保存しました: examples/output/scatter_default.png")

# %% [markdown]
# ## 5. カスタマイズ例

# %% カスタマイズ例
# paperプリセットをベースにカスタマイズ
mpl_config.apply_style('paper')

# 追加のカスタマイズ
plt.rcParams['figure.figsize'] = [4, 3]
plt.rcParams['lines.markersize'] = 4
plt.rcParams['legend.frameon'] = True

fig, ax = plt.subplots()
ax.scatter(x_corr, y_corr, alpha=0.6, s=30, color='darkblue', 
           edgecolors='black', linewidth=0.5)

ax.set_xlabel('Variable X')
ax.set_ylabel('Variable Y')
ax.set_title('Customization Example (Paper-based)')
ax.grid(True, alpha=plt.rcParams['grid.alpha'])

plt.tight_layout()
plt.savefig('examples/output/scatter_custom.png', 
            dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("カスタマイズ例を保存しました: examples/output/scatter_custom.png")
