"""
Simple usage examples for mpl_config
Basic examples for getting started
"""

# %% [markdown]
# # mpl_config シンプル使用例
# 
# このファイルは mpl_config ライブラリの基本的な使用方法を示します。
# 各セルを順番に実行してください。

# %% ライブラリのインポート
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Import mpl_config from parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mpl_config

# %% [markdown]
# ## 1. 個別のプリセットの使用例

# %% 
# paperプリセット

x = np.linspace(0, 10, 100)
y = np.sin(x)

# paperプリセットを適用
mpl_config.apply_style('paper')

# グラフの作成
plt.figure()
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Paper Style Example')
plt.legend()
# plt.grid(True)

# %% 
# presentationプリセット
mpl_config.apply_style('presentation')


plt.figure()
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Presentation Style Example')
plt.legend()
# plt.grid(True)
plt.show()

# %% 
# presentation_largeプリセット
mpl_config.apply_style('presentation_large')

plt.figure()
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Presentation_large Style Example')
plt.legend()
# plt.grid(True)
plt.show()

# %% [markdown]
# ## 3. カスタマイズ例

# %%
# paperプリセットをベースにカスタマイズ
mpl_config.apply_style('paper')

# 追加のカスタマイズ
plt.rcParams['figure.figsize'] = [8, 6]
plt.rcParams['lines.linewidth'] = 2.5
plt.rcParams['grid.linewidth'] = 0.8

plt.figure()
plt.plot(x, y, label='sin(x)', alpha=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Customized Paper Style')
plt.legend()
# plt.grid(True)
plt.show()