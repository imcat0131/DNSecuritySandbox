# DNSサーバー用Dockerfile
FROM ubuntu:20.04

# BINDのインストール
RUN apt-get update && apt-get install -y bind9

# 設定ファイルのコピー
COPY named.conf /etc/bind/

# ポート53（DNS）を開放
EXPOSE 53/udp
EXPOSE 53/tcp

# BINDサービスを起動
CMD ["named", "-g"]
