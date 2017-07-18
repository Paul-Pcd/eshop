from django.core.paginator import Paginator, InvalidPage, PageNotAnInteger
from .my_logger import logger


def get_page(order_info, current_page, num):
    """
    :param self: 
    :param order_info: 需要分页的数据 
    :param current_page:  当前的页码 从前端获取
    :param num: 每页显示多少条数据
    :return: 当前页对象 , 总共有多少也 一个列表
    """
    paginator = Paginator(order_info, num)
    try:
        current_page_order_inf0 = paginator.page(int(current_page))
    except (InvalidPage, PageNotAnInteger) as err:
        logger.error(err)
        current_page_order_inf0 = paginator.page(1)
    page_range = paginator.page_range
    return current_page_order_inf0, page_range
