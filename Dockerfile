FROM python:3.12-slim

# 作業ディレクトリを設定
WORKDIR /workspace

# システムパッケージをインストール（matplotlib用）
RUN apt-get update && apt-get install -y \
    git \
    libfreetype6-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# 開発環境用のPython依存関係は postCreateCommand でインストール
# ファイルはマウントされるのでCOPYは不要

# デフォルトコマンド
CMD ["python"] 