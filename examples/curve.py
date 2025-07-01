#!/usr/bin/env python3
"""
Curve plot examples
Comparison of mpl_config presets for academic and presentation use
"""

# ライブラリのインポート
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Import mpl_config from parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mpl_config  # noqa: E402

# %% [markdown]
# # 曲線プロット例
# 
# mpl_configの各プリセットを使った曲線プロットの例を示します。
# 減衰振動などの科学グラフの描画に適用できます。

# %% セットアップ
# 出力ディレクトリを作成
os.makedirs('output', exist_ok=True)

# %% サンプルデータの生成
# 減衰振動のサンプルデータ
x = np.linspace(0, 10, 100)
y1 = np.sin(x) * np.exp(-x/5)           # sin(x)×exp(-x/5)
y2 = np.cos(x) * np.exp(-x/5)           # cos(x)×exp(-x/5)
y3 = np.sin(2*x) * np.exp(-x/8)         # sin(2x)×exp(-x/8)

print("サンプルデータ（減衰振動）を生成しました")


# %% [markdown]
# ## 1. Paper プリセット

# %% Paper プリセットでの曲線プロット
mpl_config.apply_style('paper')

fig, ax = plt.subplots(figsize=plt.rcParams['figure.figsize'])

# 複数の曲線をプロット
ax.plot(x, y1, label='sin(x)×exp(-x/5)', 
        linewidth=plt.rcParams['lines.linewidth'])
ax.plot(x, y2, label='cos(x)×exp(-x/5)', 
        linewidth=plt.rcParams['lines.linewidth'])
ax.plot(x, y3, label='sin(2x)×exp(-x/8)', 
        linewidth=plt.rcParams['lines.linewidth'], linestyle='--')

# グラフ設定
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Damped Oscillation Comparison (paper preset)')
ax.legend()
ax.grid(True, alpha=plt.rcParams['grid.alpha'])

# 軸範囲の設定
ax.set_xlim(0, 10)
ax.set_ylim(-0.8, 0.8)

plt.tight_layout()
plt.savefig('output/curve_paper.png', dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("Paper preset グラフを保存しました: output/curve_paper.png")

# %% [markdown]
# ## 2. Presentation プリセット

# %% Presentation プリセットでの曲線プロット
mpl_config.apply_style('presentation')

fig, ax = plt.subplots(figsize=plt.rcParams['figure.figsize'])

ax.plot(x, y1, label='sin(x)×exp(-x/5)', 
        linewidth=plt.rcParams['lines.linewidth'])
ax.plot(x, y2, label='cos(x)×exp(-x/5)', 
        linewidth=plt.rcParams['lines.linewidth'])
ax.plot(x, y3, label='sin(2x)×exp(-x/8)', 
        linewidth=plt.rcParams['lines.linewidth'], linestyle='--')

ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Damped Oscillation Comparison (presentation preset)')
ax.legend()
ax.grid(True, alpha=plt.rcParams['grid.alpha'])

ax.set_xlim(0, 10)
ax.set_ylim(-0.8, 0.8)

plt.tight_layout()
plt.savefig('output/curve_presentation.png', 
            dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("Presentation preset グラフを保存しました: output/curve_presentation.png")

# %% [markdown]
# ## 2. Presentation_large プリセット

# %% Presentation_large プリセットでの曲線プロット
mpl_config.apply_style('presentation_large')

fig, ax = plt.subplots(figsize=plt.rcParams['figure.figsize'])

ax.plot(x, y1, label='sin(x)×exp(-x/5)', 
        linewidth=plt.rcParams['lines.linewidth'])
ax.plot(x, y2, label='cos(x)×exp(-x/5)', 
        linewidth=plt.rcParams['lines.linewidth'])
ax.plot(x, y3, label='sin(2x)×exp(-x/8)', 
        linewidth=plt.rcParams['lines.linewidth'], linestyle='--')

ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Damped Oscillation Comparison (presentation_large preset)')
ax.legend()
ax.grid(True, alpha=plt.rcParams['grid.alpha'])

ax.set_xlim(0, 10)
ax.set_ylim(-0.8, 0.8)

plt.tight_layout()
plt.savefig('output/curve_presentation_large.png', 
            dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("Presentation_large preset グラフを保存しました: output/curve_presentation_large.png")

# %% [markdown]
# ## 5. より複雑な曲線例

# %% 複雑な曲線の例
mpl_config.apply_style('presentation')

# より複雑なデータを生成
t = np.linspace(0, 15, 200)
signal1 = np.sin(t) * np.exp(-t/8) + 0.3 * np.sin(3*t) * np.exp(-t/10)
signal2 = np.cos(t/2) * np.exp(-t/12) * np.sin(t/3)
signal3 = np.sin(t/1.5) * np.exp(-t/6) * (1 + 0.2 * np.sin(2*t))

plt.figure(figsize=(10, 6))
plt.plot(t, signal1, label='Mixed Signal 1', alpha=0.8)
plt.plot(t, signal2, label='Modulated Signal', alpha=0.8)
plt.plot(t, signal3, label='Complex Oscillation', alpha=0.8)

plt.xlabel('Time (s)')
plt.ylabel('Signal Amplitude')
plt.title('Complex Signal Analysis')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('output/curve_complex.png', dpi=300)
plt.show()

print("複雑な曲線例を保存しました: output/curve_complex.png") 