from enum import Enum, auto
from typing import TypeVar
from subscriptions import Subscriptions

# TODO Validate that sub subscriptions match subscriptions enum
# TODO Implement a generic Enum of the differnt sub subscriptions

# TODO Make these base subscription classes private/restricted and only accessible via SubSubscriptions
# TODO Give each subscription class a shared interface and/or abstract class

class DataWalletCodebase(Enum):
    ErrorLogs = auto()
    Other = auto() # TODO Add param to specify what Category (enum, string and id), with permissions taken into account
    # TODO For Other, add opt for who to contact/update about this

class DataWalletCodebasePersonal(Enum):
    ErrorLogs = auto()
    Other = auto() # TODO Add param to specify what Category (enum, string and id), with permissions taken into account
    # TODO For Other, add opt for who to contact/update about this

class SharedCodebase(Enum):
    ErrorLogs = auto()
    Other = auto() # TODO Add param to specify what Category (enum, string and id), with permissions taken into account
    # TODO For Other, add opt for who to contact/update about this

class DataWalletPersonal(Enum):
    ErrorLogs = auto()
    Email = auto()
    Other = auto() # TODO Add param to specify what Category (enum, string and id), with permissions taken into account

class Local(Enum):
    ByInternalRef = auto()
    ByExternalRef = auto()

TSUB = TypeVar('T', bound='SubSubscriptionsImpl')
ThatImplementsACertainInterfaceWithAtLeastBasicLogicCovered = TypeVar('T2', bound='...')

class Subscription:
    def __init__(self):
        self.sub: list[SubSubscriptionsImpl.SubSubscription] = []

    def subscribe(self, sub: TSUB):
        # TODO Notify of subscription
        if not isinstance(sub, (
            SubSubscriptionsImpl.DataWalletCodebase,
            SubSubscriptionsImpl.DataWalletCodebasePersonal,
            SubSubscriptionsImpl.SharedCodebase,
            SubSubscriptionsImpl.DataWalletPersonal,
            SubSubscriptionsImpl.Local,
        )):
            raise ValueError(f"Must be a valid subscription.")
        self.sub.append(sub)

    def subscribe(sub: ThatImplementsACertainInterfaceWithAtLeastBasicLogicCovered):
        raise Exception("TODO") # TODO

    def unsubscribe(sub: TSUB):
        raise Exception("TODO") # TODO

    def unsubscribe(sub: ThatImplementsACertainInterfaceWithAtLeastBasicLogicCovered):
        raise Exception("TODO") # TODO

    # TODO What does this do?...
    def __repr__(self):
        return f"Subscription({self.sub})"

class SubSubscriptionsImpl:
    class SubSubscription:
        pass

    class DataWalletCodebase(DataWalletCodebase, SubSubscription):
        pass

    class DataWalletCodebasePersonal(DataWalletCodebasePersonal, SubSubscription):
        pass

    class SharedCodebase(SharedCodebase, SubSubscription):
        pass
    
    class DataWalletPersonal(DataWalletPersonal, SubSubscription):
        pass

    class Local(Local, SubSubscription):
        pass

class Test:
    # TODO Implement unit and integration tests and a tailored testing framework solution
    # Test that only non custom was subscribed and unsubscribed to likewise with custom
    # Unit test (every function tested sperately/individually)
    # Utilize mocks
    # Find a framework/lib for my testing and perhaps create a tailored solution here

    def does_subscribe_non_custom():
        subscription = Subscription

    def does_subscribe_to_custom():
        subscription = Subscription
        
    def does_unsubscribe_non_custom():
        subscription = Subscription

    def does_unsubscribe_custom():
        subscription = Subscription