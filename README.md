# mpl-config

シンプルなMatplotlib設定ライブラリ。論文・プレゼンテーション用のグラフ設定を簡単に適用できます。

## 特徴

- 📊 **3つのシンプルなプリセット**: paper, presentation, presentation_large
- 🎯 **自動適用**: importするだけでpresentationスタイルが適用
- 🔄 **一時スタイル**: コンテキストマネージャーで元の設定を保持
- 📐 **16:9比率**: スライドプレゼンテーションに最適化されたアスペクト比

## インストール

```bash
pip install matplotlib
```

## 使用方法

### 基本的な使い方

```python
import mpl_config  # 自動的にpresentationスタイルが適用される
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sample Plot')
plt.legend()
plt.grid(True)
plt.show()
```

### プリセット

| プリセット | フォントサイズ | 用途 |
|---|---|---|
| `paper` | 10 | 論文用（高解像度保存） |
| `presentation` | 14 | プレゼン用（デフォルト） |
| `presentation_large` | 20 | 大型会場・講堂用 |

```python
# 明示的にプリセットを指定
mpl_config.apply_style('paper')
mpl_config.apply_style('presentation_large')

# 図のサイズを個別調整（16:9比率を維持）
mpl_config.set_figsize(12, 6.75)
```

### 一時的なスタイル適用

```python
# 元の設定を保持したまま一時的に変更
with mpl_config.temp_style('paper'):
    plt.plot(x, y)
    plt.show()
# ここで元の設定に戻る
```

### その他の機能

```python
# プリセット一覧
print(mpl_config.list_presets())  # ['paper', 'presentation', 'presentation_large']

# 数式表示の最適化のみ適用
mpl_config.enable_math_optimization()

# デフォルト設定に戻す
mpl_config.reset()
```

## 数式表示の最適化

数式の上付き・下付き文字のスペーシングと配置を自動最適化します：

```python
import mpl_config
import matplotlib.pyplot as plt

plt.text(0.5, 0.5, r'$x^2 + y^2 = r^2$', fontsize=20)
plt.show()  # より美しく読みやすい数式表示
```

## ファイル構成

```
mpl-config/
├── mpl_config.py          # メインライブラリ（約200行）
└── README.md
```

## ライセンス

MIT License
