


class Category:
    category_name: str

    description_category: str

    category_products: list

    category_count = 0

    product_count = 0

    def __init__(self, category_name, description_category, category_products):

        self.category_name = category_name

        self.description_category = description_category

        self.__category_products = category_products

        Category.category_count += 1

        Category.product_count += len(self.__category_products)

    def __repr__(self):

        return (f"Имя категории - {self.category_name}; "

                f"Описание категории - {self.description_category}; Список продуктов - {self.__category_products}\n")

    def __len__(self):

        len_products = 0

        for i in self.__category_products:
            len_products += i.quantity_in_stock

        return len_products

    def __str__(self):

        return f'{self.category_name},  количество продуктов: {self.__len__()} шт.\n'

