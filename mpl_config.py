#!/usr/bin/env python3
"""
シンプルなMatplotlib設定ライブラリ
論文・プレゼン用のグラフ設定を簡単に変更
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import _mathtext as mathtext
from contextlib import contextmanager
from typing import List


# プリセット設定（必要最小限）
PRESETS = {
    'paper': {
        'font.size': 10,
        'axes.labelsize': 11,
        'axes.titlesize': 12,
        'legend.fontsize': 10,
        'figure.figsize': [10, 5.625],  # 16:9 ratio (統一)
        'figure.dpi': 150,
        'savefig.dpi': 600,
        'axes.linewidth': 1.5,  # 1.0 → 1.5 (1.5倍)
        'lines.linewidth': 1.5,
    },
    
    'presentation': {
        'font.size': 14,
        'axes.labelsize': 16,
        'axes.titlesize': 18,
        'legend.fontsize': 12,
        'figure.figsize': [10, 5.625],  # 16:9 ratio (統一)
        'figure.dpi': 100,
        'savefig.dpi': 300,
        'axes.linewidth': 2.25,  # 1.5 → 2.25 (1.5倍)
        'lines.linewidth': 3.0,
    },
    
    'presentation_large': {
        'font.size': 20,
        'axes.labelsize': 24,
        'axes.titlesize': 28,
        'legend.fontsize': 18,
        'figure.figsize': [10, 5.625],  # 16:9 ratio (統一)
        'figure.dpi': 100,
        'savefig.dpi': 300,
        'axes.linewidth': 3.0,  # 2.0 → 3.0 (1.5倍)
        'lines.linewidth': 4.0,
    }
}


def optimize_math_rendering() -> None:
    """
    数式表示の改善設定を適用
    
    数式の上付き文字・下付き文字の配置やスペーシングを最適化し、
    より美しい数式表示を実現します。
    
    主な改善点:
    - script_space: 数式要素間のスペースを縮小 (0.075 → 0.01)
    - sup1: 上付き文字の位置を下げる (0.45 → 0.3)
    - delta: ギリシャ文字周辺のスペースを縮小 (0.075 → 0.01)
    
    Note:
    -----
    この設定は論文やプレゼンテーションでの数式表示品質を向上させます。
    特に複雑な数式や上付き・下付き文字が多い場合に効果的です。
    """
    # Computer Modern フォント定数を使用
    mathtext.FontConstantsBase = mathtext.ComputerModernFontConstants
    
    # スペーシングの最適化
    # デフォルト: 0.075
    mathtext.FontConstantsBase.script_space = 0.01
    mathtext.FontConstantsBase.delta = 0.01             # デフォルト: 0.075
    
    # 上付き文字の位置調整（より自然な位置に）
    mathtext.FontConstantsBase.sup1 = 0.3               # デフォルト: 0.45
    
    # 以下はデフォルト値のまま（必要に応じてコメントアウトを外して調整可能）
    # mathtext.FontConstantsBase.subdrop = 0.2          # 下付き文字のドロップ量
    # mathtext.FontConstantsBase.sub1 = 0.2             # 下付き文字位置1
    # mathtext.FontConstantsBase.sub2 = 0.3             # 下付き文字位置2
    # mathtext.FontConstantsBase.delta_slanted = 0.3    # 斜体文字のスペース
    # mathtext.FontConstantsBase.delta_integral = 0.3   # 積分記号のスペース


def apply_style(preset_name: str = 'presentation', **kwargs) -> None:
    """
    スタイルプリセットを適用
    
    Parameters:
    -----------
    preset_name : str
        'paper', 'presentation', 'presentation_large'のいずれか
        デフォルトは'presentation'
    **kwargs : dict
        追加のカスタマイズ設定
        
    Note:
    -----
    全プリセットでfigsize=[10, 5.625]（16:9比率）に統一されています。
    スライドプレゼンテーションに最適化されたアスペクト比です。
    図のサイズを変更したい場合は、set_figsize()を使用してください。
    """
    if preset_name not in PRESETS:
        available = ', '.join(PRESETS.keys())
        raise ValueError(f"不明なプリセット: {preset_name}. 利用可能: {available}")
    
    # プリセット設定を適用
    settings = PRESETS[preset_name].copy()
    settings.update(kwargs)
    
    # matplotlib設定を更新
    for key, value in settings.items():
        plt.rcParams[key] = value
    
    # 共通設定
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans',
                                       'Liberation Sans']
    plt.rcParams['axes.spines.top'] = True
    plt.rcParams['axes.spines.right'] = True
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['xtick.top'] = True
    plt.rcParams['ytick.right'] = True
    # 目盛の長さを2倍に設定
    plt.rcParams['xtick.major.size'] = 7.0  # デフォルト: 3.5
    plt.rcParams['ytick.major.size'] = 7.0  # デフォルト: 3.5
    plt.rcParams['xtick.minor.size'] = 4.0  # デフォルト: 2.0
    plt.rcParams['ytick.minor.size'] = 4.0  # デフォルト: 2.0
    # 目盛線の太さを設定
    plt.rcParams['xtick.major.width'] = 1.5  # デフォルト: 0.8
    plt.rcParams['ytick.major.width'] = 1.5  # デフォルト: 0.8
    plt.rcParams['xtick.minor.width'] = 1.0  # デフォルト: 0.6
    plt.rcParams['ytick.minor.width'] = 1.0  # デフォルト: 0.6
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['savefig.bbox'] = 'tight'
    plt.rcParams['savefig.transparent'] = True
    # 背景透明化設定
    plt.rcParams['figure.facecolor'] = 'none'  # 図の背景を透明に
    plt.rcParams['axes.facecolor'] = 'none'    # 軸の背景を透明に
    
    # 数式表示の最適化を適用
    optimize_math_rendering()


def set_figsize(width: float, height: float) -> None:
    """
    図のサイズを設定
    
    Parameters:
    -----------
    width : float
        図の幅（インチ）
    height : float
        図の高さ（インチ）
        
    Example:
    --------
    # プレゼンテーション用フォントで大きな図を作成
    mpl_config.apply_style('presentation')
    mpl_config.set_figsize(12, 8)
    """
    plt.rcParams['figure.figsize'] = [width, height]


@contextmanager
def temp_style(preset_name: str, **kwargs):
    """
    一時的にスタイルを適用するコンテキストマネージャー
    
    Example:
    --------
    with temp_style('presentation'):
        plt.plot(x, y)
        plt.show()
    """
    original = plt.rcParams.copy()
    try:
        apply_style(preset_name, **kwargs)
        yield
    finally:
        plt.rcParams.update(original)


def list_presets() -> List[str]:
    """利用可能なプリセット一覧"""
    return list(PRESETS.keys())


def reset() -> None:
    """デフォルト設定に戻す"""
    mpl.rcdefaults()


def enable_math_optimization() -> None:
    """
    数式表示の最適化を手動で有効化
    
    apply_style()を使わずに数式表示だけを改善したい場合に使用
    """
    optimize_math_rendering()


# モジュールimport時に自動的にpresentationスタイルを適用
apply_style('presentation')


# 使用例
if __name__ == "__main__":
    print("利用可能なプリセット:")
    for preset in list_presets():
        print(f"  - {preset}")
    
    print("\n使用例:")
    print("  import mpl_config  # 自動的にpresentationスタイルが適用されます")
    print("  # 全プリセットで16:9比率（スライド用）に最適化")
    print("  # または明示的に:")
    print("  mpl_config.apply_style()  # デフォルトでpresentation")
    print("  mpl_config.apply_style('paper')  # 論文用")
    print("  # 一時的に適用:")
    print("  with mpl_config.temp_style('paper'):")
    print("      plt.plot(x, y)")
    print("  # 図のサイズを個別に調整:")
    print("  mpl_config.set_figsize(12, 6.75)  # 16:9比率を維持")
    print("  # 数式表示のみ最適化:")
    print("  mpl_config.enable_math_optimization()") 