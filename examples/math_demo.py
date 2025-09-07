#!/usr/bin/env python3
"""
数式表示改善のデモ
mpl_configの数式最適化機能の効果を確認
"""

# %% [markdown]
# # 数式表示例
# 
# 数式の上付き・下付き文字の位置を調整します。

# %% ライブラリのインポートとセットアップ
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Import mpl_config from parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mpl_config

# %% [markdown]
# ## 1. 数式表示の例

# %%
mpl_config.apply_style('paper')  # 数式最適化も自動適用

fig, ax = plt.subplots(figsize=(10, 8))

# 複雑な数式のサンプル
equations = [
    r'$E = mc^2$',
    r'$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$',
    r'$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$',
    r'$\sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k} = (x+y)^n$',
    r'$\frac{d}{dx}\left[\int_a^x f(t)dt\right] = f(x)$',
    r'$\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e$',
    r'$\mathbf{F} = m\mathbf{a} = m\frac{d^2\mathbf{r}}{dt^2}$',
    r'$\Psi(x,t) = \sum_n c_n \psi_n(x) e^{-iE_n t/\hbar}$'
]

# 数式を配置
for i, eq in enumerate(equations):
    y_pos = 0.9 - i * 0.1
    ax.text(0.1, y_pos, eq, fontsize=14, transform=ax.transAxes)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Complex Mathematical Expressions\n' +
             '(with optimized spacing and positioning)', 
             fontsize=16, pad=20)

plt.tight_layout()

plt.show()

# %% [markdown]
# ## 2. 論文でよく使われる数式

# %% 数式例
mpl_config.apply_style('paper')

# 数式を含む実際のグラフ例
t = np.linspace(0, 4*np.pi, 1000)
omega = 2  # 角周波数
damping = 0.1  # 減衰係数

# 減衰調和振動子
y_damped = np.exp(-damping * t) * np.cos(omega * t)

plt.figure(figsize=(10, 6))
plt.plot(t, y_damped, 'b-', linewidth=2, label=r'$y(t) = e^{-\gamma t} \cos(\omega t)$')
plt.plot(t, np.exp(-damping * t), 'r--', alpha=0.7, label=r'$e^{-\gamma t}$ (envelope)')
plt.plot(t, -np.exp(-damping * t), 'r--', alpha=0.7)

plt.xlabel(r'Time $t$ (s)')
plt.ylabel(r'$y(t)$')
plt.title(r'Damped Harmonic Oscillator: $\frac{d^2y}{dt^2} + 2\gamma\frac{dy}{dt} + \omega^2 y = 0$')
plt.legend()
plt.grid(True, alpha=0.3)

# パラメータを注釈で追加
plt.text(0.5, 0.8, r'$\omega = 2$ rad/s, $\gamma = 0.1$ s$^{-1}$', transform=plt.gca().transAxes, 
         bbox=dict(boxstyle="round,pad=0.3", facecolor="none", edgecolor="none", alpha=0.7))


plt.tight_layout()
plt.show()

# %% [markdown]
# ## 3. 統計・数学の数式

# %% 統計・数学の数式例
mpl_config.apply_style('presentation')

# 正規分布のデータ
x = np.linspace(-4, 4, 1000)
mu = 0
sigma = 1
y = (1/(sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=3)
plt.fill_between(x, y, alpha=0.3)

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'Normal Distribution: $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$')

# 統計量を表示
plt.text(0.05, 0.8, r'$\mu = 0$ (mean)', transform=plt.gca().transAxes, fontsize=14)
plt.text(0.05, 0.7, r'$\sigma = 1$ (standard deviation)', transform=plt.gca().transAxes, fontsize=14)
plt.text(0.05, 0.6, r'$\int_{-\infty}^{\infty} f(x) dx = 1$', transform=plt.gca().transAxes, fontsize=14)

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

