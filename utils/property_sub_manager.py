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

    def __init__(self):
        self.subscribers = {}

    def subscribe(self, property_name, callback):
        """
        Adds a callback function to the list of subscribers for the given property name.
        """
        if property_name not in self.subscribers:
            self.subscribers[property_name] = []
        self.subscribers[property_name].append(callback)

    def unsubscribe(self, property_name, callback):
        """Removes a callback function from the list of subscribers for the given property name."""
        if property_name in self.subscribers:
            self.subscribers[property_name].remove(callback)
            if not self.subscribers[property_name]:
                del self.subscribers[property_name]

    def notify(self, property_name, value):
        """
        Calls all the callback functions subscribed to the given property name,
        passing the provided value as an argument.
        """
        if property_name in self.subscribers:
            for callback in self.subscribers[property_name]:
                callback(value)
