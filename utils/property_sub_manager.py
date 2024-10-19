from dataclasses import dataclass
from listen import Listen
# TODO ~9/10priority Create a documentation and testing framework to hide
# and show comments on hover (later an option to to optionally show it in file though
# not writing file, similar to how Cline uses diff and some lines are added)
# TODO Add context for property (such as what from what class and what methods it is in
# and is begin called from) as well as authentication for permission based properties.
# Although first you may need to implement permissions manager

class PropertySubscriptionManager:
    """
    This allows any property to be subscribed to, and the subscribers will be
    notified whenever the property value changes.
    """
    
    @dataclass
    class Subscribers:
        property: Listen
        update_type: any # TODO Enum
        callback: any # TODO Callback
    
    @dataclass
    class _PropertySubManager:
        subscribe = {}
        unsubscrbe = {}
        notify = {}
        reserved = {}

    def __init__(self):
        self.subscribers: dict[str, PropertySubscriptionManager.Subscribers] = {}
        self.property_sub_manager = self._PropertySubManager()

    def request_set(self, property_name, new_value: str):
        # TODO Notify to whom ever registered for request
        # TODO If real time update is allowed or if deadlock would be in place before operation is complete (TODO but make sure that the deadlock only works by the receiving end).
        # if self.subscribers[property_name].update_type == "update in real time":
        if self.subscribers[property_name].callback:
            self.subscribers[property_name].callback(new_value)
        self.subscribers[property_name].property = new_value
        print(self.subscribers[property_name].property, "kk changed")
    
    def _get(self, property_name):
        return self.subscribers[property_name].property

    def request_view():
        # TODO Notify to whom ever registered for request
        allow = False
        if allow:
            return "value"
        else:
            return "Not allowed" # TODO Return enums with values caried in them

    def not_a_reserved_property_name(property_name, uuid):
        match property_name:
            # TODO Everything under property_sub_manager that is
            case "subscribe" "unsubscribe" "notify" "reserved":
                self.reserved[property_name][uuid]
                raise Exception(f"Reserved property of '{property_name}'") # TODO Custom logging and notification

    def subscribe(self, property: Listen, property_name: str, update_type, callback = None):
        """
        Adds a callback function to the list of subscribers for the given property name.
        Record the subscription attempt.
        """
        self.not_a_reserved_property_name(property_name)
        if property_name not in self.subscribers:
            self.subscribers[property_name] = {} # TODO

        self.subscribers[property_name] = PropertySubscriptionManager.Subscribers(
            property, update_type, callback
        )

    def unsubscribe(self, property_name, callback):
        """
        Removes a callback function from the list of subscribers for the given property name.
        Record the unsubscription attempt.
        """
        self.not_a_reserved_property_name(property_name)
        if property_name in self.subscribers:
            self.subscribers[property_name].remove(callback)
            if not self.subscribers[property_name]:
                del self.subscribers[property_name]

    def notify(self, property_name, value):
        """
        Calls all the callback functions subscribed to the given property name,
        passing the provided value as an argument.
        Record the notify attempt.
        """
        self.not_a_reserved_property_name(property_name)
        if property_name in self.subscribers:
            for callback in self.subscribers[property_name]:
                callback(value)
