from enum import Enum, auto
from subscriptions import Subscriptions

# TODO Validate that sub subscriptions match subscriptions enum
# TODO Implement a generic Enum of the differnt sub subscriptions
class SubSubscriptions:

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

    subscription: Subscriptions