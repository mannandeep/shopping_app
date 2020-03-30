from .cart import Cart


def cart(request): #request object as a parameter
    return {'cart': Cart(request)} #dictionary of object