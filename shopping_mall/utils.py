# 数据处理工具
def shop_info(status, assess):
    lists = ['购物车', '待付款', '待发货', '待收货', '待评价']
    result = [{'status': x, 'num': 0} for x in [1, 2, 3, 6]]
    for i in result:
        for j in status:
            if i['status'] == j['status']:
                i['num'] = j['num']
    result.append({'status': '待评价', 'num': assess})
    for i in range(len(lists)):
        result[i]['status'] = lists[i]
    return result


# 处理商品选择
def shop_category(opt):
    category_name = ['选择颜色', '选择尺码', '选择系列', '选择版本', '选择规格', '选择类别', '选择性别']
    lists = []
    result = []
    for i in range(len(opt)):
        if not lists:
            lists.append(opt[i])
        else:
            if lists[-1].get('type') == opt[i].get('type'):
                lists.append(opt[i])
                if i == len(opt) - 1:
                    result.append([{'title': category_name[lists[-1].get('type')]}, {'content': lists}])

            else:
                result.append([{'title': category_name[lists[-1].get('type')]}, {'content': lists}])
                lists = []
                lists.append(opt[i])
    return result


def data_conversion(data):
    result = []
    for i in data:
        i['show_image'] = eval(i.get('show_image'))
        result.append(i)
    return result
