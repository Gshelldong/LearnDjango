from  django import template
register = template.Library()

@register.filter(name='plugin')
def plugin(a,b):
    # 做一个简易加法版本
    return a + b


# 自定义标签
# 支持传多个值
@register.simple_tag(name='jason')
def xxx(a,b,c,year):
	return '%s?%s|%s{%s'%(a,b,c,year)


@register.inclusion_tag('bigplus.html')
def bigplus(n):
	l = []
	for i in range(n):
		l.append('第%s项'%i)
	return {'l':l}