# ログ分析用Dockerfile
FROM python:3.10

# Pipenvのインストール
RUN pip install pipenv

# ワークディレクトリの設定
WORKDIR /app

COPY . /app

# 依存関係のインストール
RUN pipenv install --deploy --ignore-pipfile

# 分析スクリプトの実行
CMD pipenv run python ./analysis-scripts/example-analysis-script.py
