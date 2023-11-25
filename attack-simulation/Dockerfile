# 攻撃シミュレーション用Dockerfile
FROM python:3.8

# Pipenvのインストール
RUN pip install pipenv

# ワークディレクトリの設定
WORKDIR /attack-simulation

# Pipfileのコピー
COPY attack-simulation/Pipfile /attack-simulation/Pipfile

# 依存関係のインストール
RUN pipenv install --deploy --ignore-pipfile

# 攻撃スクリプトのコピー
COPY attack-simulation/attack-scripts /attack-simulation/attack-scripts

# 攻撃スクリプトの実行
CMD pipenv run python /attack-simulation/attack-scripts/example-attack-script.py
