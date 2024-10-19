from dataclasses import dataclass
from utils.property_sub_manager import PropertySubscriptionManager

class Object:
    @dataclass
    class Subscribers:
        property: any
        update_type: any
        callback: any
    
    @dataclass
    class _PropertySubManager:
        subscribe = {}
        unsubscrbe = {}
        notify = {}
        reserved = {}

    def __init__(self):
        self.subscribers: dict[str, PropertySubscriptionManager.Subscribers] = {}
        self.property_sub_manager = self._PropertySubManager()

    def subscribe(self, property, property_name, update_type, callback = None):
        self.subscribers[property_name] = Object.Subscribers(
            property, update_type, callback
        )
                
        print(self.subscribers[property_name].property, "(self.subscribers[property_name].property)")
    
    def _get(self, property_name):
        return self.subscribers[property_name].property

# TODO Include this in full code coverage too
class TestObject:
    def sub_and_get(self):
        object = Object()
        property = "kk little man"
        property_name = "my prop"

        object.subscribe(property, property_name, "")
        object._get(property_name)

def main():
    test_object = TestObject()
    test_object.sub_and_get()

if __name__ == "__main__":
    main()