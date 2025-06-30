#!/usr/bin/env python3
"""
2D map (heatmap) examples
Comparison of mpl_config presets for academic and presentation use
"""

# %% [markdown]
# # 2Dマップ（ヒートマップ）例
# 
# mpl_configの各プリセットを使った2Dマップの例を示します。
# コンターマップ、温度分布、相関行列、ベクトル場など。

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

# %% サンプルデータの生成
# 2D ガウシアンデータ
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 複数のガウシアンピーク
Z1 = np.exp(-((X-1)**2 + (Y-1)**2) / 2)
Z2 = 0.5 * np.exp(-((X+2)**2 + (Y-2)**2) / 4)
Z3 = 0.3 * np.exp(-((X-2)**2 + (Y+1)**2) / 1)
Z = Z1 + Z2 + Z3

# 温度分布のようなデータ
temp_data = (20 + 10 * np.sin(X/2) * np.cos(Y/2) + 
             5 * np.random.normal(0, 0.1, X.shape))

# 相関行列データ
np.random.seed(42)
corr_matrix = np.random.randn(10, 10)
corr_matrix = np.corrcoef(corr_matrix)

print("サンプルデータ（2Dガウシアン、温度分布、相関行列）を生成しました")

# %% [markdown]
# ## 1. Paper プリセット - 複合2Dマップ

# %% Paper プリセットでの2Dマップ
mpl_config.apply_style('paper')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

# 1. コンターマップ
contour = ax1.contourf(X, Y, Z, levels=20, cmap='viridis')
ax1.contour(X, Y, Z, levels=20, colors='black', 
            alpha=0.3, linewidths=0.5)
fig.colorbar(contour, ax=ax1, shrink=0.8)
ax1.set_xlabel('X Coordinate')
ax1.set_ylabel('Y Coordinate')
ax1.set_title('Contour Map')

# 2. ヒートマップ
heatmap = ax2.imshow(temp_data, extent=[-5, 5, -5, 5], origin='lower', 
                     cmap='RdYlBu_r', aspect='auto')
fig.colorbar(heatmap, ax=ax2, shrink=0.8, label='Temperature (°C)')
ax2.set_xlabel('X Coordinate')
ax2.set_ylabel('Y Coordinate')
ax2.set_title('Temperature Distribution')

# 3. 相関行列
im = ax3.imshow(corr_matrix, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
fig.colorbar(im, ax=ax3, shrink=0.8, label='Correlation')
ax3.set_xlabel('Variable Number')
ax3.set_ylabel('Variable Number')
ax3.set_title('Correlation Matrix')

# ティックを設定
ticks = np.arange(0, 10, 2)
ax3.set_xticks(ticks)
ax3.set_yticks(ticks)

# 4. 3D表面投影
surface = ax4.contourf(X, Y, Z, levels=30, cmap='plasma')
fig.colorbar(surface, ax=ax4, shrink=0.8)
ax4.set_xlabel('X Coordinate')
ax4.set_ylabel('Y Coordinate')
ax4.set_title('3D Surface Projection')

plt.tight_layout()
plt.savefig('examples/output/2dmap_paper.png', dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("Paper preset 2Dマップを保存しました: examples/output/2dmap_paper.png")

# %% [markdown]
# ## 2. Presentation プリセット

# %% Presentation プリセットでの2Dマップ
mpl_config.apply_style('presentation')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

# 同じ内容をプレゼンテーション用スタイルで描画
contour = ax1.contourf(X, Y, Z, levels=20, cmap='viridis')
ax1.contour(X, Y, Z, levels=20, colors='black', 
            alpha=0.3, linewidths=0.5)
fig.colorbar(contour, ax=ax1, shrink=0.8)
ax1.set_xlabel('X Coordinate')
ax1.set_ylabel('Y Coordinate')
ax1.set_title('Contour Map')

heatmap = ax2.imshow(temp_data, extent=[-5, 5, -5, 5], origin='lower', 
                     cmap='RdYlBu_r', aspect='auto')
fig.colorbar(heatmap, ax=ax2, shrink=0.8, label='Temperature (°C)')
ax2.set_xlabel('X Coordinate')
ax2.set_ylabel('Y Coordinate')
ax2.set_title('Temperature Distribution')

im = ax3.imshow(corr_matrix, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
fig.colorbar(im, ax=ax3, shrink=0.8, label='Correlation')
ax3.set_xlabel('Variable Number')
ax3.set_ylabel('Variable Number')
ax3.set_title('Correlation Matrix')
ax3.set_xticks(ticks)
ax3.set_yticks(ticks)

surface = ax4.contourf(X, Y, Z, levels=30, cmap='plasma')
fig.colorbar(surface, ax=ax4, shrink=0.8)
ax4.set_xlabel('X Coordinate')
ax4.set_ylabel('Y Coordinate')
ax4.set_title('3D Surface Projection')

plt.tight_layout()
plt.savefig('examples/output/2dmap_presentation.png', dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("Presentation preset 2Dマップを保存しました: examples/output/2dmap_presentation.png")

# %% [markdown]
# ## 3. Default プリセット

# %% Default プリセットでの2Dマップ
mpl_config.apply_style('default')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

contour = ax1.contourf(X, Y, Z, levels=20, cmap='viridis')
ax1.contour(X, Y, Z, levels=20, colors='black', 
            alpha=0.3, linewidths=0.5)
fig.colorbar(contour, ax=ax1, shrink=0.8)
ax1.set_xlabel('X Coordinate')
ax1.set_ylabel('Y Coordinate')
ax1.set_title('Contour Map')

heatmap = ax2.imshow(temp_data, extent=[-5, 5, -5, 5], origin='lower', 
                     cmap='RdYlBu_r', aspect='auto')
fig.colorbar(heatmap, ax=ax2, shrink=0.8, label='Temperature (°C)')
ax2.set_xlabel('X Coordinate')
ax2.set_ylabel('Y Coordinate')
ax2.set_title('Temperature Distribution')

im = ax3.imshow(corr_matrix, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
fig.colorbar(im, ax=ax3, shrink=0.8, label='Correlation')
ax3.set_xlabel('Variable Number')
ax3.set_ylabel('Variable Number')
ax3.set_title('Correlation Matrix')
ax3.set_xticks(ticks)
ax3.set_yticks(ticks)

surface = ax4.contourf(X, Y, Z, levels=30, cmap='plasma')
fig.colorbar(surface, ax=ax4, shrink=0.8)
ax4.set_xlabel('X Coordinate')
ax4.set_ylabel('Y Coordinate')
ax4.set_title('3D Surface Projection')

plt.tight_layout()
plt.savefig('examples/output/2dmap_default.png', dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("Default preset 2Dマップを保存しました: examples/output/2dmap_default.png")

# %% [markdown]
# ## 4. カラーマップ比較

# %% カスタムカラーマップ例
mpl_config.apply_style('paper')

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 異なるカラーマップで表示
colormaps = ['viridis', 'plasma', 'coolwarm', 'seismic']
titles = ['Viridis', 'Plasma', 'Coolwarm', 'Seismic']

for i, (cmap, title) in enumerate(zip(colormaps, titles)):
    ax = axes[i // 2, i % 2]
    im = ax.contourf(X, Y, Z, levels=20, cmap=cmap)
    ax.contour(X, Y, Z, levels=20, colors='black', 
               alpha=0.2, linewidths=0.3)
    fig.colorbar(im, ax=ax, shrink=0.6)
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title(f'{title} Colormap')

plt.tight_layout()
plt.savefig('examples/output/2dmap_colormap_comparison.png', 
            dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("カラーマップ比較を保存しました: examples/output/2dmap_colormap_comparison.png")

# %% [markdown]
# ## 5. 高度な2Dプロット

# %% 高度な2Dプロット例
mpl_config.apply_style('presentation')

# より複雑なデータを生成
x_adv = np.linspace(-3, 3, 200)
y_adv = np.linspace(-3, 3, 200)
X_adv, Y_adv = np.meshgrid(x_adv, y_adv)

# 複雑な関数
Z_adv = np.sin(X_adv**2 + Y_adv**2) * np.exp(-(X_adv**2 + Y_adv**2)/4)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# 1. 詳細なコンター
levels = np.linspace(Z_adv.min(), Z_adv.max(), 50)
contour = ax1.contourf(X_adv, Y_adv, Z_adv, levels=levels, cmap='RdYlBu_r')
ax1.contour(X_adv, Y_adv, Z_adv, levels=20, colors='black', 
            alpha=0.3, linewidths=0.5)
fig.colorbar(contour, ax=ax1, shrink=0.8)
ax1.set_xlabel('X Coordinate')
ax1.set_ylabel('Y Coordinate')
ax1.set_title('Detailed Contour')

# 2. ベクトル場の可視化
u = -np.sin(Y_adv)
v = np.cos(X_adv)
skip = 10  # ベクトル削間
ax2.quiver(X_adv[::skip, ::skip], Y_adv[::skip, ::skip], 
           u[::skip, ::skip], v[::skip, ::skip], 
           alpha=0.7, scale=20)
ax2.contour(X_adv, Y_adv, Z_adv, levels=10, alpha=0.3)
ax2.set_xlabel('X Coordinate')
ax2.set_ylabel('Y Coordinate')
ax2.set_title('Vector Field')
ax2.set_aspect('equal')

# 3. ストリームライン
ax3.streamplot(X_adv, Y_adv, u, v, density=2, color='blue')
ax3.contour(X_adv, Y_adv, Z_adv, levels=10, alpha=0.3)
ax3.set_xlabel('X Coordinate')
ax3.set_ylabel('Y Coordinate')
ax3.set_title('Streamlines')

# 4. コンター + 散布図
ax4.contourf(X_adv, Y_adv, Z_adv, levels=30, cmap='viridis', alpha=0.7)
# ランダムポイントを追加
np.random.seed(42)
n_points = 50
x_points = np.random.uniform(-3, 3, n_points)
y_points = np.random.uniform(-3, 3, n_points)
ax4.scatter(x_points, y_points, c='red', s=30, alpha=0.8, 
            edgecolors='black', linewidth=0.5)
ax4.set_xlabel('X Coordinate')
ax4.set_ylabel('Y Coordinate')
ax4.set_title('Contour + Scatter Plot')

plt.tight_layout()
plt.savefig('examples/output/2dmap_advanced.png', 
            dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("高度な2Dプロットを保存しました: examples/output/2dmap_advanced.png")

# %% [markdown]
# ## 6. 一時的なスタイル変更のデモ

# %% 一時的なスタイル変更例
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# デフォルト設定
mpl_config.apply_style('default')

# 最初：デフォルト
axes[0].contourf(X, Y, Z, levels=20, cmap='viridis')
axes[0].set_title('Default Setting')
axes[0].set_xlabel('X Coordinate')
axes[0].set_ylabel('Y Coordinate')

# 2番目：一時的にpaper設定
with mpl_config.temp_style('paper'):
    axes[1].contourf(X, Y, Z, levels=20, cmap='viridis')
    axes[1].set_title('Paper Setting (Temporary)')
    axes[1].set_xlabel('X Coordinate')
    axes[1].set_ylabel('Y Coordinate')

# 3番目：デフォルトに戻る
axes[2].contourf(X, Y, Z, levels=20, cmap='viridis')
axes[2].set_title('Default Setting (Restored)')
axes[2].set_xlabel('X Coordinate')
axes[2].set_ylabel('Y Coordinate')

plt.tight_layout()
plt.savefig('examples/output/2dmap_temp_style_demo.png', dpi=300)
plt.show()

print("一時的なスタイル変更デモを保存しました: examples/output/2dmap_temp_style_demo.png") 