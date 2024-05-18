import json


def load_product_list():
    """
    получаем список json.
    :return:
    """
    with open('products.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
    return products


def get_name_category(product_list):
    """
    получаем наименование категории.
    :param product_list:
    :return:
    """
    category_name = product_list['name']
    return category_name


def get_category_description(product_list):
    """
    получаем описание категории.
    :param product_list:
    :return:
    """
    description_categories = product_list["description"]
    return description_categories


def get_category_products(product_list):
    """
    получаем категории.
    :param product_list:
    :return:
    """
    category_products = product_list['products']
    return category_products


def get_products_name(product_list):
    """
    получаем наименование продукта для класса Products.
    :param product_list:
    :return:
    """
    product_name = product_list["products"][0]['name']
    return product_name


def get_products_description(product_list):
    """
    получаем описание продукта.
    :param product_list:
    :return:
    """
    product_description = product_list["products"][0]['description']
    return product_description


def get_products_price(product_list):
    """
    получаем цену продукта.
    :param product_list:
    :return:
    """
    price = product_list["products"][0]['price']
    return price


def get_quantity(product_list):
    """
    получчаем количество на складе.
    :param product_list:
    :return:
    """
    quantity_in_stock = product_list["products"][0]['quantity']
    return quantity_in_stock
