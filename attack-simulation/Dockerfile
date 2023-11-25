# 攻撃シミュレーション用Dockerfile
FROM python:3.10

# Pipenvのインストール
RUN pip install pipenv

# ワークディレクトリの設定
WORKDIR /app

# Pipfileのコピー
COPY . /app

# 依存関係のインストール
RUN pipenv install --deploy --ignore-pipfile

# 攻撃スクリプトの実行
CMD pipenv run python ./attack-scripts/example-attack-script.py
