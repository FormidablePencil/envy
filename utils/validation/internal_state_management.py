from enum import Enum, auto
from subscriptions.subscriptions import Subscriptions
from subscriptions.sub_subscriptions import SubSubscriptions



class InternalStateManagement:
    subscriptions: Subscriptions
    enum: [Class1, Class2] # TODO Either implement some generic for the sub subscriptions or handle this in some other way than using 'any'

    def __init__(self):
        self.subscriptions = Subscriptions.DataWalletCodebase
        self.sub_subscriptions = SubSubscriptions.DataWalletCodebase

    data: list[any]
    state: list[any]

    # TODO Depending on certian criteria certain methods can't be called no more
    # So perhaps implement abstract/interface for this

    def __init__(self, subscribe: ):
            

    def subscribe():

    def local():

    def validate_call():
        # TODO 1. Call by reference (opt permission based), relative to in context (permission based) and index (permssion based)
    
    # Will always be accessible by reference so long as reference is kept. TODO It might
    # be necessary to implement by internal reference to item or reference to external
    # state/data
    def 
