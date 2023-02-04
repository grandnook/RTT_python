# Measuring RTT

This is a simple program to measure RTT between server and client using socket communication implemented with python.

# Implementation details
## Default configurations
- UDP
- Hostname: `localhost`
- IP address: `0.0.0.0` or `127.0.0.1`
- Port number: `12345`
- buffer size: `512`

## Methods mainly used
- `sock.sendto()`
- `sock.recvfrom()`

## Japanese
pythonで実装したソケット通信を利用して，サーバ・クライアント間のRTTの計測を行う簡単なプログラム．


