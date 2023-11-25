# ログ分析用Dockerfile
FROM python:3.8

# Pipenvのインストール
RUN pip install pipenv

# ワークディレクトリの設定
WORKDIR /log-analysis

# Pipfileのコピー
COPY log-analysis/Pipfile /log-analysis/Pipfile

# 依存関係のインストール
RUN pipenv install --deploy --ignore-pipfile

# 分析スクリプトのコピー
COPY log-analysis/analysis-scripts /log-analysis/analysis-scripts

# 分析スクリプトの実行
CMD pipenv run python /log-analysis/analysis-scripts/example-analysis-script.py
