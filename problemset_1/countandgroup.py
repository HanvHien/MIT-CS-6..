
def item_order(order):

    count_Salad = 0
    count_Water = 0
    count_Hamburger = 0

    count_Salad = order.count('salad')
    count_Water = order.count('water')
    count_Hamburger = order.count('hamburger')

    return 'salad:{:} hamburger:{:} water:{:}'.format(count_Salad, count_Hamburger, count_Water)
