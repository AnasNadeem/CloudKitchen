"""
    Problem Statement:
    There's a cloud kitchen where users gives order and you have to provide the expected time the food gets deliever [Consider Delievery time is 0].
    Notes:
    1. Limited stove in kitchen
    2. Every order item has a given prep time.
    3. Orders can be recieved anytime.
    Find the least time the order gets ready for users considering the above situation.
"""
class Kitchen:
    def __init__(self):
        # Later change self.stove to {"1":True, "2":False} something like this
        self.stove = [
            {
                "id":1,
                "name":"First stove",
                "status":False
            },
            {
                "id":2,
                "name":"Second stove",
                "status":False
            },
            {
                "id":3,
                "name":"Third stove",
                "status":False
            }
            ]
        self.items = [
                {
                    "id":1,
                    "name":"Biryani",
                    "p_time":35
                },
                {
                    "id":2,
                    "name":"Pizza",
                    "p_time":30
                },
                {
                    "id":3,
                    "name":"Fries",
                    "p_time":10
                },
                {
                    "id":4,
                    "name":"Lava cake",
                    "p_time":15
                }
            ]
        self.crnt_orders = []
        self.cooked_orders = []
        self.temp_order_dict = {}

    def rec_order(self, order_dict):
        """
        order_dict: {
            "user_id":<id>,
            "item":[order_id, order_id]
        }
        For ex {"user_id":1, "item":[1, 3]}: User 1 ordered [1, 3] i.e., Biryani and Fries .
        """
        # Insert the order in the crnt_orders
        self.crnt_orders.append(order_dict)
        # Assign the orders to the stove
        self.assign_order(order_dict=order_dict)
        print('Temp order dict', self.temp_order_dict)

    def assign_order(self, order_dict):
        # Check stove status whether if its assigned or available
        temp_order_item = []
        avail_stove, book_stove = self.stove_status()
        num = 0
        for stove in avail_stove:
            stove['order'] = order_dict['id']
            for item in order_dict['items'][num:]:
                stove['item'] = item
                # Updating the stove status 
                self.update_stove_status(stove_id=stove['id'], status=True)
                print(f"Order {order_dict['id']} with item {self.items[stove['item']]['name']} assigned to stove {stove['id']}")
            num+=1
        # Incase item is not assigned cause now the stove's all booked
        temp_order_item.append(order_dict['items'][num:])
        self.temp_order_dict[order_dict['id']]= temp_order_item
        self.stove_status()

    def update_order(self):
        pass

    def expected_time(self):
        pass

    def update_stove_status(self, stove_id, status):
        for stove in self.stove:
            if stove['id'] == stove_id:
                stove['status'] = status
        print('Stove dict', self.stove)
        print(f"Status changed of stove {stove_id} to {status}..")

    def stove_status(self):
        avail_stove = []
        book_stove = []
        for stove in self.stove:
            if stove["status"]==False:
                print(f"Stove {stove['id']} is available")
                avail_stove.append(stove)
            else:
                print(f"Stove {stove['id']} is booked")
                book_stove.append(stove)
        return avail_stove, book_stove


a = Kitchen()
order1 = {"id":1, "items":[1, 3]}
a.rec_order(order_dict=order1)