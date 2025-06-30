#!/usr/bin/env python3
"""
シンプルなmatplotlib設定ライブラリのテスト
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_config


def test_basic_functionality():
    """基本機能のテスト"""
    print("=== 基本機能テスト ===")
    
    # 利用可能なプリセット表示
    presets = mpl_config.list_presets()
    print(f"利用可能なプリセット: {presets}")
    assert len(presets) == 3
    assert 'paper' in presets
    assert 'presentation' in presets
    assert 'default' in presets
    
    print("✓ プリセット一覧の取得が正常に動作しています")


def test_style_application():
    """スタイル適用のテスト"""
    print("\n=== スタイル適用テスト ===")
    
    # テストデータ
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    
    # 各プリセットでテストプロット
    for preset in mpl_config.list_presets():
        mpl_config.apply_style(preset)
        
        fig, ax = plt.subplots()
        ax.plot(x, y, label=f'{preset} style')
        ax.set_xlabel('x')
        ax.set_ylabel('sin(x)')
        ax.set_title(f'Test: {preset}')
        ax.legend()
        ax.grid(True)
        
        plt.tight_layout()
        plt.savefig(f'test_{preset}.png', dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"✓ {preset} スタイルの適用とプロット保存が完了しました")


def test_temp_style():
    """一時スタイル適用のテスト"""
    print("\n=== 一時スタイル適用テスト ===")
    
    x = np.linspace(0, 5, 30)
    y = np.cos(x)
    
    # 一時スタイルのテスト
    with mpl_config.temp_style('presentation'):
        fig, ax = plt.subplots()
        ax.plot(x, y, label='cos(x)')
        ax.set_xlabel('x')
        ax.set_ylabel('cos(x)')
        ax.set_title('Temporary Style Test')
        ax.legend()
        ax.grid(True)
        plt.tight_layout()
        plt.savefig('test_temp_style.png', bbox_inches='tight')
        plt.close()
    
    print("✓ 一時スタイル適用のテストが完了しました")


if __name__ == "__main__":
    print("matplotlib設定ライブラリ（シンプル版）のテストを開始します...\n")
    
    try:
        test_basic_functionality()
        test_style_application()
        test_temp_style()
        
        print("\n🎉 すべてのテストが正常に完了しました！")
        print("生成されたファイル:")
        for preset in mpl_config.list_presets():
            print(f"  - test_{preset}.png")
        print("  - test_temp_style.png")
        
    except Exception as e:
        print(f"\n❌ テスト中にエラーが発生しました: {e}")
        import traceback
        traceback.print_exc() 