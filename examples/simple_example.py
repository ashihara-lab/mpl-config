#!/usr/bin/env python3
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

# 出力ディレクトリを作成
os.makedirs('examples/output', exist_ok=True)

# %% [markdown]
# ## 1. 基本的な使用例 - paper プリセット

# %% 基本例：paperプリセット
# サンプルデータの作成
x = np.linspace(0, 10, 100)
y = np.sin(x)

# paperプリセットを適用
mpl_config.apply_style('paper')

# グラフの作成
plt.figure()
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Example Graph for Paper')
plt.legend()
plt.grid(True)

# 保存
plt.savefig('examples/output/simple_paper.png')
plt.show()

print("Paper graph saved: examples/output/simple_paper.png")

# %% [markdown]
# ## 2. プリセット比較例
# 
# paper, presentation, default の3つのプリセットを比較します。

# %% プリセット比較
# サンプルデータ
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
presets = ['paper', 'presentation', 'default']

for i, preset in enumerate(presets):
    with mpl_config.temp_style(preset):
        ax = axes[i]
        ax.plot(x, y1, label='sin(x)')
        ax.plot(x, y2, label='cos(x)')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'{preset} Preset')
        ax.legend()
        ax.grid(True)

plt.tight_layout()
plt.savefig('examples/output/simple_comparison.png', dpi=300)
plt.show()

print("Preset comparison saved: examples/output/simple_comparison.png")

# %% [markdown]
# ## 3. 利用可能なプリセット一覧

# %% プリセット一覧表示
print("利用可能なプリセット:")
for preset in mpl_config.list_presets():
    print(f"  - {preset}")

# %% [markdown]
# ## 4. 個別スタイル試行
# 
# 各プリセットを個別に試してみましょう。

# %% presentationプリセット
mpl_config.apply_style('presentation')

x = np.linspace(0, 8, 80)
y = np.exp(-x/4) * np.sin(2*x)

plt.figure()
plt.plot(x, y, linewidth=3, label='exp(-x/4)×sin(2x)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Presentation Style Example')
plt.legend()
plt.grid(True)
plt.show()

# %% defaultプリセット
mpl_config.apply_style('default')

x = np.linspace(-5, 5, 100)
y = x**2 * np.exp(-x**2/5)

plt.figure()
plt.plot(x, y, color='green', label='x²×exp(-x²/5)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Default Style Example')
plt.legend()
plt.grid(True)
plt.show()

# %% [markdown]
# ## 5. カスタマイズ例

# %% カスタマイズ例
# paperプリセットをベースにカスタマイズ
mpl_config.apply_style('paper')

# 追加のカスタマイズ
plt.rcParams['figure.figsize'] = [8, 6]
plt.rcParams['lines.linewidth'] = 2.5
plt.rcParams['grid.linewidth'] = 0.8

x = np.linspace(0, 2*np.pi, 200)
y1 = np.sin(x)
y2 = np.sin(2*x) * 0.5
y3 = np.sin(3*x) * 0.3

plt.figure()
plt.plot(x, y1, label='sin(x)', alpha=0.8)
plt.plot(x, y2, label='0.5×sin(2x)', alpha=0.8)
plt.plot(x, y3, label='0.3×sin(3x)', alpha=0.8)
plt.xlabel('Angle (rad)')
plt.ylabel('Amplitude')
plt.title('Customized Paper Style')
plt.legend()
plt.grid(True)
plt.show()

print("\n完了！結果は examples/output/ ディレクトリで確認できます。") 