def get_customer_baskets(email, shopping_baskets):
    return [basket for basket in shopping_baskets if email == basket["email"]]


def get_all_customers(shopping_baskets):
    return sorted(set([basket["email"] for basket in shopping_baskets]))


def get_required_stock(shopping_baskets):
    required_stock = []
    paid_stock = [
        {"name": item["name"], "quantity": item["quantity"]}
        for basket in shopping_baskets
        for item in basket["items"]
        if basket["status"] == "PAID"
    ]

    for stock in paid_stock:
        if stock not in required_stock:
            required_stock.append(stock)
        elif stock in required_stock:
            required_stock[required_stock.index(stock)]["quantity"] += stock["quantity"]

    return required_stock


def get_total_spent(email, shopping_baskets):
    bought_items = [
        item
        for basket in get_customer_baskets(email, shopping_baskets)
        for item in basket["items"]
        if basket["status"] in ("PAID", "DELIVERED")
    ]

    return sum(item["price"] * item["quantity"] for item in bought_items)


def get_top_customers(shopping_baskets):
    customer_purchases = {}

    for customer in get_all_customers(shopping_baskets):
        customer_purchases[customer] = get_total_spent(customer, shopping_baskets)

    sorted_customer_purchases = dict(
        sorted(customer_purchases.items(), key=lambda item: item[1], reverse=True)
    )

    return [
        {"email": customer, "total": sorted_customer_purchases[customer]}
        for customer in sorted_customer_purchases
    ]


def get_customers_with_open_baskets(shopping_baskets):
    return sorted(
        set(
            basket["email"] for basket in shopping_baskets if basket["status"] == "OPEN"
        )
    )
