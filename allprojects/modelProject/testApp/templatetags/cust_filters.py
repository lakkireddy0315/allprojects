from django import template
register=template.Library()

@register.filter(name='truncate5')
def truncate5(value):
    result=value[0:5]
    return result

@register.filter(name='t_n')
def truncate_n(value,n):
    result=value[0:n]
    return 'durga' 

def first_eight_upper(value): 
    '''''This is my own filter''' 
    result=value[:8].upper() 
    return result 

register.filter('f8upper',first_eight_upper) 