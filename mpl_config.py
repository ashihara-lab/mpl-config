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


# プリセット設定
PRESETS = {
    'paper': {
        'font.size': 10,
        'axes.labelsize': 11,
        'axes.titlesize': 12,
        'legend.fontsize': 10,
        'figure.figsize': [10, 5.625],  # 16:9比率
        'figure.dpi': 150,
        'savefig.dpi': 600,
        'axes.linewidth': 1.5,
        'lines.linewidth': 1.5,
    },
    
    'presentation': {
        'font.size': 14,
        'axes.labelsize': 16,
        'axes.titlesize': 18,
        'legend.fontsize': 12,
        'figure.figsize': [10, 5.625],  # 16:9比率
        'figure.dpi': 100,
        'savefig.dpi': 300,
        'axes.linewidth': 2.25,
        'lines.linewidth': 3.0,
    },
    
    'presentation_large': {
        'font.size': 20,
        'axes.labelsize': 24,
        'axes.titlesize': 28,
        'legend.fontsize': 18,
        'figure.figsize': [10, 5.625],  # 16:9比率
        'figure.dpi': 100,
        'savefig.dpi': 300,
        'axes.linewidth': 3.0,
        'lines.linewidth': 4.0,
    }
}


def optimize_math_rendering() -> None:
    """数式表示の改善設定を適用"""
    # Computer Modern フォント定数を使用
    mathtext.FontConstantsBase = mathtext.ComputerModernFontConstants
    
    # スペーシングの最適化
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
    **kwargs : dict
        追加のカスタマイズ設定
    """
    if preset_name not in PRESETS:
        available = ', '.join(PRESETS.keys())
        raise ValueError(f"不明なプリセット: {preset_name}. 利用可能: {available}")
    
    # プリセット設定を適用
    settings = PRESETS[preset_name].copy()
    settings.update(kwargs)
    
    for key, value in settings.items():
        plt.rcParams[key] = value
    
    # 共通設定
    _apply_common_settings()
    
    # 数式表示の最適化
    optimize_math_rendering()


def _apply_common_settings() -> None:
    """共通設定を適用"""
    # フォント設定
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans']
    
    # 軸とスパインの設定
    plt.rcParams['axes.spines.top'] = True
    plt.rcParams['axes.spines.right'] = True
    
    # 目盛設定
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['xtick.top'] = True
    plt.rcParams['ytick.right'] = True
    
    # 目盛のサイズと太さ
    plt.rcParams['xtick.major.size'] = 7.0
    plt.rcParams['ytick.major.size'] = 7.0
    plt.rcParams['xtick.minor.size'] = 4.0
    plt.rcParams['ytick.minor.size'] = 4.0
    plt.rcParams['xtick.major.width'] = 1.5
    plt.rcParams['ytick.major.width'] = 1.5
    plt.rcParams['xtick.minor.width'] = 1.0
    plt.rcParams['ytick.minor.width'] = 1.0
    
    # その他の設定
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['savefig.bbox'] = 'tight'
    plt.rcParams['savefig.transparent'] = True
    plt.rcParams['figure.facecolor'] = 'none'  # 透明背景
    plt.rcParams['axes.facecolor'] = 'none'


def set_figsize(width: float, height: float) -> None:
    """
    図のサイズを設定
    
    Parameters:
    -----------
    width : float
        図の幅（インチ）
    height : float
        図の高さ（インチ）
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
    """利用可能なプリセット一覧を返す"""
    return list(PRESETS.keys())


def reset() -> None:
    """デフォルト設定に戻す"""
    mpl.rcdefaults()


def enable_math_optimization() -> None:
    """数式表示の最適化を手動で有効化"""
    optimize_math_rendering()


# モジュールimport時に自動的にpresentationスタイルを適用
apply_style('presentation')


# 使用例
if __name__ == "__main__":
    print("利用可能なプリセット:")
    for preset in list_presets():
        print(f"  - {preset}")
    
    print("\n使用例:")
    print("  import mpl_config")
    print("  mpl_config.apply_style('paper')  # 論文用")
    print("  mpl_config.set_figsize(12, 6.75)  # サイズ変更")
    print("  with mpl_config.temp_style('paper'):")
    print("      plt.plot(x, y)  # 一時的に適用") 