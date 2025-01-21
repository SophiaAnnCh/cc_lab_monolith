import json
from typing import List, Union
from products import get_product, Product
from cart import dao


class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> "Cart":
        contents = [get_product(item_id) for item_id in json.loads(data.get('contents', '[]'))]
        return Cart(data['id'], data['username'], contents, data['cost'])


def get_cart(username: str) -> Union[Cart, None]:
    cart_data = dao.get_cart(username)
    if not cart_data:
        return Cart(id=0, username=username, contents=[], cost=0.0)
    
    cart = Cart.load(cart_data)
    return cart


def add_to_cart(username: str, product_id: int) -> None:
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int) -> None:
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str) -> None:
    dao.delete_cart(username)
