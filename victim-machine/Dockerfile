# 攻撃されるマシン用Dockerfile
FROM ubuntu:20.04

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y iputils-ping

# 永久に稼働させるためのコマンド
CMD tail -f /dev/null
