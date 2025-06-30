#!/usr/bin/env python3
"""
Master script to run all mpl_config usage examples
Batch execution of mpl_config library examples
"""

# %% [markdown]
# # 全例題の一括実行スクリプト
# 
# mpl_configの使用例を一括で実行するスクリプトです。
# 各セルを順番に実行すると、全ての例題が実行されます。

# %% ライブラリのインポートとセットアップ
import sys
import os
import subprocess

print("=== mpl_config Usage Examples Batch Execution ===\n")

# 出力ディレクトリを作成
output_dir = "examples/output"
os.makedirs(output_dir, exist_ok=True)

# %% 実行する例題リスト
examples = [
    ("simple_example.py", "Basic Usage Examples"),
    ("curve.py", "Curve Plot Examples"),
    ("scatter.py", "Scatter Plot Examples"),
    ("2dmap.py", "2D Map Examples"),
    ("math_demo.py", "Math Rendering Demo")
]

print("実行予定の例題:")
for i, (filename, description) in enumerate(examples, 1):
    print(f"{i}. {description} ({filename})")

# %% [markdown]
# ## 1. Basic Usage Examples の実行

# %% Simple Example の実行
print("1. Running Basic Usage Examples...")

try:
    result = subprocess.run(
        [sys.executable, "simple_example.py"],
        cwd="examples",
        capture_output=True,
        text=True,
        timeout=60
    )
    
    if result.returncode == 0:
        print("✓ Basic Usage Examples completed successfully\n")
    else:
        print(f"✗ Basic Usage Examples failed: {result.stderr}\n")
        
except subprocess.TimeoutExpired:
    print("✗ Basic Usage Examples timed out\n")
except Exception as e:
    print(f"✗ Basic Usage Examples error: {e}\n")

# %% [markdown]
# ## 2. Curve Plot Examples の実行

# %% Curve Examples の実行
print("2. Running Curve Plot Examples...")

try:
    result = subprocess.run(
        [sys.executable, "curve.py"],
        cwd="examples",
        capture_output=True,
        text=True,
        timeout=60
    )
    
    if result.returncode == 0:
        print("✓ Curve Plot Examples completed successfully\n")
    else:
        print(f"✗ Curve Plot Examples failed: {result.stderr}\n")
        
except subprocess.TimeoutExpired:
    print("✗ Curve Plot Examples timed out\n")
except Exception as e:
    print(f"✗ Curve Plot Examples error: {e}\n")

# %% [markdown]
# ## 3. Scatter Plot Examples の実行

# %% Scatter Examples の実行
print("3. Running Scatter Plot Examples...")

try:
    result = subprocess.run(
        [sys.executable, "scatter.py"],
        cwd="examples",
        capture_output=True,
        text=True,
        timeout=60
    )
    
    if result.returncode == 0:
        print("✓ Scatter Plot Examples completed successfully\n")
    else:
        print(f"✗ Scatter Plot Examples failed: {result.stderr}\n")
        
except subprocess.TimeoutExpired:
    print("✗ Scatter Plot Examples timed out\n")
except Exception as e:
    print(f"✗ Scatter Plot Examples error: {e}\n")

# %% [markdown]
# ## 4. 2D Map Examples の実行

# %% 2D Map Examples の実行
print("4. Running 2D Map Examples...")

try:
    result = subprocess.run(
        [sys.executable, "2dmap.py"],
        cwd="examples",
        capture_output=True,
        text=True,
        timeout=60
    )
    
    if result.returncode == 0:
        print("✓ 2D Map Examples completed successfully\n")
    else:
        print(f"✗ 2D Map Examples failed: {result.stderr}\n")
        
except subprocess.TimeoutExpired:
    print("✗ 2D Map Examples timed out\n")
except Exception as e:
    print(f"✗ 2D Map Examples error: {e}\n")

# %% [markdown]
# ## 5. Math Rendering Demo の実行

# %% Math Demo の実行
print("5. Running Math Rendering Demo...")

try:
    result = subprocess.run(
        [sys.executable, "math_demo.py"],
        cwd="examples",
        capture_output=True,
        text=True,
        timeout=60
    )
    
    if result.returncode == 0:
        print("✓ Math Rendering Demo completed successfully\n")
    else:
        print(f"✗ Math Rendering Demo failed: {result.stderr}\n")
        
except subprocess.TimeoutExpired:
    print("✗ Math Rendering Demo timed out\n")
except Exception as e:
    print(f"✗ Math Rendering Demo error: {e}\n")

# %% [markdown]
# ## 実行結果の確認

# %% 生成されたファイルの確認
print("=== Execution Complete ===")
print(f"Generated files saved in {output_dir} directory")

# Script execution location adaptive path
possible_paths = [
    "examples/output",     # When executed from root directory
    "output",              # When executed from examples directory
    "../examples/output"   # When executed from another location
]

output_path = None
for path in possible_paths:
    if os.path.exists(path) and os.path.isdir(path):
        output_path = path
        break

if output_path:
    files = sorted(os.listdir(output_path))
    if files:
        print("\nGenerated files:")
        for file in files:
            print(f"  - {file}")
        print(f"\nTotal: {len(files)} files generated")
    else:
        print("\nNo files were generated")
else:
    print("\nOutput directory not found")

# %% まとめ
print("\n=== Summary ===")
print("全ての例題の実行が完了しました。")
print("各例題でグラフが生成され、examples/output/ ディレクトリに保存されました。")
print("Jupyter環境では、各例題ファイルを個別に開いて実行することも可能です。") 