# ログ分析スクリプト
import pandas as pd
import matplotlib.pyplot as plt

def analyze_logs(log_file_path):
    # ログファイルの読み込み
    logs = pd.read_csv(log_file_path)

    # ログデータの分析
    # 例: DNSクエリ数の時間経過による変化
    query_counts = logs.groupby('timestamp')['query_name'].count()
    query_counts.plot(kind='line', title='DNS Query Counts Over Time')

    # 攻撃されるマシンからのクエリの分析
    # 例: 攻撃対象マシンからのクエリ数
    victim_queries = logs[logs['source_ip'] == 'victim-machine-ip']
    victim_query_counts = victim_queries.groupby('timestamp')['query_name'].count()
    victim_query_counts.plot(kind='line', title='Victim Machine DNS Queries Over Time')

    # グラフの表示
    plt.show()

# ログファイルのパス
log_file_path = '/log-files/dns-logs.csv'
analyze_logs(log_file_path)
