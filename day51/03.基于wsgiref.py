from wsgiref.simple_server import make_server
from urls import urls
from views import *

def run(env,response):
    """
    env是请求相关的数据
    response是响应相关的数据
    """
    # print(env)
    response('200 OK',[])
    current_path = env.get('PATH_INFO')
    # print(current_path)
    # if current_path == '/index':
    #     return [b'index']
    # elif current_path == '/login':
    #     return [b'login']
    # 定义一个存储函数名的标志位
    func = None
    for url in urls:
        # 判断当前url在不在元组内
        if url[0] == current_path:
            # 只要匹配上了  就把url后缀对应的函数名赋值给func
            func = url[1]
            # 一旦匹配上 应该立刻退出for循环 节省资源
            break
    # 对变量func做判断
    if func:
        res = func(env)
    else:
        res = errors(env)
    return [res.encode('utf-8')]


if __name__ == '__main__':
    server = make_server('127.0.0.1',8080,run)
    # 实时监测127.0.0.1:8080地址 一旦有客户端来连接 会自动加括号调用run方法
    server.serve_forever()  # 启动服务端