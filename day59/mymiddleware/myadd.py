from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class MyAdd(MiddlewareMixin):
    def process_request(self,request):
        print('我是第一个中间件里面的process_request方法')

    def process_response(self,request,response):
        print('我是第一个中间件的process_reponse方法')
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print(view_func)
        print(view_args)
        print(view_kwargs)
        print('我是第一个中间件里面的process_view方法')

    def process_exception(self, request, exception):
        print('我是第一个中间件里面的process_exception')

    def process_template_response(self, request, response):
        print('我是第一个中间件里面的process_template_response')
        return response


class MyAdd1(MiddlewareMixin):
    def process_request(self, request):
        print('我是第2个中间件里面的process_request方法')

    def process_response(self, request, response):
        print('我是第2个中间件的process_reponse方法')
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print(view_func)
        print(view_args)
        print(view_kwargs)
        print('我是第二个中间件里面的process_view方法')

    def process_exception(self, request, exception):
        print('我是第二个中间件里面的process_exception')

    def process_template_response(self, request, response):
        print('我是第二个中间件里面的process_template_response')
        return response


class MyAdd2(MiddlewareMixin):
    def process_request(self, request):
        print('我是第3个中间件里面的process_request方法')

    def process_response(self, request, response):
        print('我是第3个中间件的process_reponse方法')
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print(view_func)
        print(view_args)
        print(view_kwargs)
        print('我是第三个中间件里面的process_view方法')

    def process_exception(self, request, exception):
        print('我是第三个中间件里面的process_exception')

    def process_template_response(self, request, response):
        print('我是第三个中间件里面的process_template_response')
        return response
