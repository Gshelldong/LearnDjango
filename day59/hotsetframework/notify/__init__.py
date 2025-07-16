import importlib
import settings


def send_all(content):
    for path_str in settings.MIDDLEWARES:
        module_path,class_name = path_str.rsplit('.',maxsplit=1)  # 2.从右边开始 按照点切一个 ['notify.email','Email']
        module = importlib.import_module(module_path)  # from notity import msg,email,wechat
        cls = getattr(module,class_name)  # 利用反射 一切皆对象的思想 从文件中获取属性或者方法 cls = 一个个的类名
        obj = cls()  # 类实例化生成对象
        obj.send(content)  # 对象调方法
