

def cart_contents(request):

    cart_items = []
    product_count = 0
    total_cost = 0

    context = {
        'cart_items': cart_items,
        'product_count': product_count,
        'total_cost': total_cost
    }

    return context
