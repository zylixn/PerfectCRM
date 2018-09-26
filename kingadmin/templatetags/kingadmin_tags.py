from django.template import Library
from django.utils.safestring import mark_safe
import datetime

register = Library()
@register.simple_tag
def build_table_row(obj,admin_class):
    """生成一条记录的HTML element"""
    ele = ''
    for column_name in admin_class.list_display:
        column_obj = admin_class.model._meta.get_field(column_name)
        # 通过反射获取数据,两个参数,一个是object,一个是列名
        # column_data = getattr(obj,column_name)
        if column_obj.choices:
            column_data = getattr(obj,'get_%s_display'%column_name)()
        else:
            column_data = getattr(obj,column_name)
        td_ele = "<td>%s</td>"%column_data
        ele += td_ele

    return mark_safe(ele)

@register.simple_tag
def build_filter_ele(filter_column,admin_class):
    #filter_ele = "<select name='%s'>"%filter_column
    column_obj = admin_class.model._meta.get_field(filter_column)
    try:
        filter_ele = "<select name='%s'>" % filter_column
        for choice in column_obj.get_choices():
            selected = ''
            if filter_column in admin_class.filter_conditions:
                filter_data = admin_class.filter_conditions.get(filter_column)
                if str(choice[0]) == filter_data:
                    selected = "selected"
            option = "<option value='%s' %s>%s</option>"%(choice[0],selected,choice[1])
            filter_ele += option

    except AttributeError as e:
        #get_internal_type():获取字段属性
        #因为时间的过滤方式是固定的（今天，过去七天，一个月.....），而不是从后台获取的
        filter_ele = "<select name='%s__gte'>" % filter_column
        if column_obj.get_internal_type() in ('DateField','DateTimeField'):
            time_obj = datetime.datetime.now()
            time_list = [
                ['','--------'],
                [time_obj,'Today'],
                    [time_obj - datetime.timedelta(7),'七天内'],
                [time_obj.replace(day=1),'本月'],
                [time_obj - datetime.timedelta(90),'三个月内'],
                [time_obj.replace(month=1,day=1),'YearToDay(YTD)'],     #本年
                ['','ALL'],
            ]

            for i in time_list:
                selected = ''
                time_to_str = '' if not i[0] else "%s-%s-%s"%(i[0].year,i[0].month,i[0].day)
                if "%s__gte"%filter_column in admin_class.filter_conditions:
                    if time_to_str == admin_class.filter_conditions.get("%s__gte"%filter_column):
                        selected = "selected"
                option = "<option value='%s' %s>%s</option>" %(time_to_str,selected,i[1])
                filter_ele += option

    filter_ele += "</select>"

    return mark_safe(filter_ele)



