#解けなかった
#!/bin/sh

#POST /vote HTTP/1.1
#Host: 34.170.146.252:58224
#Content-Length: 10
#Accept-Language: ja
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36
#Content-Type: application/x-www-form-urlencoded
#Accept: */*
#Origin: http://34.170.146.252:58224
#Referer: http://34.170.146.252:58224/
#Accept-Encoding: gzip, deflate, br
#Connection: keep-alive
#
#animal=dog

# 送信先のURL
url="http://34.170.146.252:58224/vote"

# POSTデータ
data="animal=dog"

# curlコマンドでPOSTリクエストを送信
curl -X POST "$url" \
     -H "Host: 34.170.146.252:58224" \
     -H "Content-Length: 10" \
     -H "Accept-Language: ja" \
     -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -H "Accept: */*" \
     -H "Origin: http://34.170.146.252:58224" \
     -H "Referer: http://34.170.146.252:58224/" \
     -H "Accept-Encoding: gzip, deflate, br" \
     -H "Connection: keep-alive" \
     --data "$data"