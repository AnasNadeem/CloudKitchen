# Cloud Kitchen prep time
class CloudKitchen:
    def __init__(self):
        self.stoves = {
            '1':{
            'item':None,
            'available':True
            },
            '2':{
            'item':None,
            'available':True
            },
            '3':{
            'item':None,
            'available':True
            },
        }
        self.menu_items = {
            '1':{
            'name':'Biryani',
            'prep_time': 40
            },
            '2':{
            'name':'Pizza',
            'prep_time': 30
            },
            '3':{
            'name':'Burger',
            'prep_time': 15
            },
            '4':{
            'name':'Momos',
            'prep_time': 10
            }
        }
        self.order_on_stove = []
        self.order_queue = []
        self.user_order_completed = {}
        self.user_order_on_stove = {}
        # {
        #     '<user:id>':{
        #         'item1':'item:expected_time',
        #         'item2':'item:expected_time',
        #     },
        #     '<user:id>':{
        #         'item1':'item:expected_time',
        #     },
        # }
        self.user_order_queue = {}
        # {
        #     '<user:id>':{
        #         'item1':'item:prep_time',
        #         'item2':'item:prep_time',
        #     },
        #     '<user:id>':{
        #         'item1':'item:prep_time',
        #         'item2':'item:prep_time',
        #         'item3':'item:prep_time',
        #     },
        # }
        self.user_original_order = {}

    def check_availablity(self):
        """Will check the stove availablity"""
        avail_stove = []
        booked_stove = []
        for stove_id, stove_value in self.stoves.items():
            if self.stoves[stove_id]["available"]:
                print(f"Stove {stove_id} is available")
                avail_stove.append(stove_id)
            else:
                print(f"Stove {stove_id} is booked")
                booked_stove.append(stove_id)
        return avail_stove, booked_stove

    def new_orders(self, order):
        """Receive new orders from Users"""
        avail_stove, booked_stove = self.check_availablity()
        for item in order:
            # TODO- Assigning the item with max time first into queue
            self.order_queue.append(item)
            
        for stove_id in avail_stove:
            if len(self.order_queue)<1:
                break
            self.update_order_stove(stove_id)


    def update_order_stove(self, stove_id):
        """Will update the order_queue_list, order_on_stove_list and stove  
        availability dict."""
        # Update the stove with the first item in order_queue
        first_item_in_order_queue = self.order_queue[0]
        self.stoves[stove_id]['item'] = first_item_in_order_queue
        # Updating stove availability
        self.stoves[stove_id]['available'] = False
        # append in order_on_stove
        self.order_on_stove.append(first_item_in_order_queue)
        # remove from order_queue
        self.order_queue.remove(first_item_in_order_queue)

    def order_prep_end_time(self):
        pass

if __name__=="__main__":
    a = CloudKitchen()
    # order = [1, 3]
    # Order will be a dict containg user_id as a key and order items as a value that will be a  list 
    order= {'1':[1,2]}
    a.new_orders(order)
    a.new_orders([4,2])
    a.new_orders([3])
  
  
  