# import ipdb

class Coffee:
    def __init__(self, name):
        self.name = name

    @property #getter
    def name(self):
        return self._name
    
    @name.setter #setter
    def name(self, value):
        if isinstance(value, str) and 2 < len(value):
            if not hasattr(self, '_name'):
                self._name = value
            else: 
                raise Exception("name is already set and can't be changed")
        else: 
            raise TypeError("name must be type 'string' and be at least 3 characters long.")
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in Order.all if order.coffee == self]))
    
    def num_orders(self):
        return sum([1 for order in Order.all if order.coffee == self])
    
    def average_price(self):
        total_prices = [order.price for order in Order.all if order.coffee == self]
        if total_prices: 
            return sum(total_prices) / len(total_prices)
        else: 
            return 0

class Customer:
    def __init__(self, name):
        self.name = name

    @property #getter
    def name(self):
        return self._name
    
    @name.setter #setter
    def name(self, value):
        if isinstance(value, str) and 0 < len(value) < 16:
            self._name = value
        else: 
            raise TypeError("name must be type 'string' and be between 1 and 15 characters long.")
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in Order.all if order.customer == self]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all = [] 
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.__class__.all.append(self)

    @ property #getter
    def customer(self):
        return self._customer

    @customer.setter #setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else: 
            raise TypeError("customer must be type 'Customer'.")


    @ property #getter
    def coffee(self):
        return self._coffee

    @coffee.setter #setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
        else: 
            raise TypeError("coffee must be type 'Coffee'.")


    @ property #getter
    def price(self):
        return self._price

    @price.setter #setter
    def price(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            if not hasattr(self, '_price'):
                self._price = value
            else: 
                raise Exception("price is already set and can't be changed")
        else: 
            raise TypeError("price must be type 'float' and must be a number between 1.0 and 10.0, inclusive.")




# n1 = Coffee("Drip")
# n2 = Coffee("Americano")

# c1 = Customer("Steven")
# c2 = Customer("Rachel")

# o1 = Order(n1, c1 , 1.1)
# o2 = Order(n2, c2, 9.9)

# ipdb.set_trace()