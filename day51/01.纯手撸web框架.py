import socket

"""
# 请求头
GET /favicon.ico HTTP/1.1
Host: 127.0.0.1:8080
Connection: keep-alive
sec-ch-ua-platform: "Windows"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0
sec-ch-ua: "Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"
sec-ch-ua-mobile: ?0
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: image
Referer: http://127.0.0.1:8080/index
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: csrftoken=LEhOMFQH58iH0xhqNDIkgjDW2UPueRUBYrP5c8XyOmpdeNSDIpccCQKOCuZKLDq6
"""

server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)

while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    # print(data)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    data = data.decode('utf-8')
    # 客户端请求发送过来的内容
    print(data)
    # 通过字符串处理，根据路径把对应的网页内容返回给客户端
    current_path = data.split('\r\n')[0].split(' ')[1]
    print(current_path)

    if current_path == '/index':
        with open(r'templates/01.纯手撸web框架.html',mode='rb') as f:
            conn.send(f.read())
    elif current_path == '/login':
        conn.send(b'login')
    else:
        conn.send(b'hello word!')
    conn.close()
