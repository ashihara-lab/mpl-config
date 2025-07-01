#!/usr/bin/env python3
"""
2D map (heatmap) examples
Comparison of mpl_config presets for academic and presentation use
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Import mpl_config from parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mpl_config

# %% [markdown]
# # 2Dマップ（ヒートマップ）例
# 
# mpl_configの各プリセットを使った2Dマップの例を示します。
# コンターマップ、温度分布、相関行列、ベクトル場など。

# %% ライブラリのインポートとセットアップ

# 出力ディレクトリを作成
os.makedirs('output', exist_ok=True)

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
plt.savefig('output/2dmap_paper.png', dpi=plt.rcParams['savefig.dpi'])
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
plt.savefig('output/2dmap_presentation.png',
            dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("Presentation preset 2Dマップを保存しました: "
      "examples/output/2dmap_presentation.png")


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
plt.savefig('output/2dmap_advanced.png', 
            dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("高度な2Dプロットを保存しました: examples/output/2dmap_advanced.png")

# %% [markdown]
# ## 6. 一時的スタイル変更のデモ

# %% 一時的スタイル変更: Paper スタイル
# ベースラインとしてpresentationスタイルを適用
mpl_config.apply_style('presentation')

# 同じデータセットを使用
simple_x = np.linspace(0, 10, 100)
simple_y = np.sin(simple_x) * np.exp(-simple_x/5)
simple_z = np.cos(simple_x) * np.exp(-simple_x/3)

# Paper スタイルで一時的に描画
with mpl_config.temp_style('paper'):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # 左側: 線グラフ
    ax1.plot(simple_x, simple_y, label='sin(x)·exp(-x/5)', linewidth=2)
    ax1.plot(simple_x, simple_z, label='cos(x)·exp(-x/3)', linewidth=2)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_title('Line Plot (Paper Style)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 右側: ヒートマップ
    small_temp = temp_data[::5, ::5]  # データを間引き
    im = ax2.imshow(small_temp, cmap='RdYlBu_r', aspect='auto')
    ax2.set_xlabel('X Index')
    ax2.set_ylabel('Y Index')
    ax2.set_title('Heatmap (Paper Style)')
    fig.colorbar(im, ax=ax2, shrink=0.8)
    
    plt.tight_layout()
    plt.savefig('output/temp_style_paper.png', 
                dpi=plt.rcParams['savefig.dpi'])
    plt.show()

print("Paper一時スタイルの図を保存しました: "
      "examples/output/temp_style_paper.png")

# %% 一時的スタイル変更: Presentation Large スタイル
# presentation_largeスタイルで同じデータを描画
with mpl_config.temp_style('presentation_large'):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # 左側: 線グラフ
    ax1.plot(simple_x, simple_y, label='sin(x)·exp(-x/5)', linewidth=3)
    ax1.plot(simple_x, simple_z, label='cos(x)·exp(-x/3)', linewidth=3)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_title('Line Plot (Large Style)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 右側: ヒートマップ
    im = ax2.imshow(small_temp, cmap='RdYlBu_r', aspect='auto')
    ax2.set_xlabel('X Index')
    ax2.set_ylabel('Y Index')
    ax2.set_title('Heatmap (Large Style)')
    fig.colorbar(im, ax=ax2, shrink=0.8)
    
    plt.tight_layout()
    plt.savefig('output/temp_style_large.png', 
                dpi=plt.rcParams['savefig.dpi'])
    plt.show()

print("Large一時スタイルの図を保存しました: "
      "examples/output/temp_style_large.png")

# %% スタイル復帰確認
# 元のpresentationスタイルに戻っていることを確認
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(simple_x, simple_y, label='sin(x)·exp(-x/5)', linewidth=2)
ax.plot(simple_x, simple_z, label='cos(x)·exp(-x/3)', linewidth=2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Style Restoration Check (Presentation Style)')
ax.legend()
ax.grid(True, alpha=0.3)

# 現在のスタイル設定を表示
current_fontsize = plt.rcParams['font.size']
current_linewidth = plt.rcParams['lines.linewidth']
text_content = (f'Font Size: {current_fontsize}\n'
                f'Line Width: {current_linewidth}')
ax.text(0.7, 0.95, text_content, transform=ax.transAxes,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig('output/temp_style_restored.png', 
            dpi=plt.rcParams['savefig.dpi'])
plt.show()

print("スタイル復帰確認の図を保存しました: "
      "output/temp_style_restored.png")
print(f"現在のスタイル設定 - フォントサイズ: {plt.rcParams['font.size']}, "
      f"線幅: {plt.rcParams['lines.linewidth']}")

# %% [markdown]
# ## 一時的スタイル変更の説明
# 
# `mpl_config.temp_style()`コンテキストマネージャーを使用すると：
# 
# 1. **一時適用**: `with`ブロック内でのみスタイルが変更される
# 2. **自動復帰**: ブロックを抜けると元のスタイルに自動的に戻る
# 3. **図の独立性**: 各figureは独立してスタイルが適用される
# 4. **設定保持**: ベースのスタイル設定は保持される
# 
# この機能により、同じスクリプト内で複数のスタイルを使い分けることができます。

