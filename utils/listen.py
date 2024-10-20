import inspect
from typing import Union
from enum import Enum, auto
import pytest # TODO How to exclude pytest and its related tests from prod
from utils.suit_test_helpers import description, tsprint
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# TODO Test LockInListener feature as well as its' history of stack trace (alt)
# TODO Implement subscribing to various sources; databases, datawallet, codebases even if history is kept track locally
# TODO Implement private tracking where history isn't tracked locally but by whom ever subscribed to to keep history at privately.
# TODO Following the last point, implement contextually secure data. (Still a little hazy about this idea)

# TODOs To work going forward
# TODO Implementing py command for testing and running purposes
# TODO Implement value listeners to be adopted by every value in any codebase
# TODO Implement a subscription source for listener and vise-versa where a data source can request for or subscribe to data optionally providing in what context (determined by ai intention and context detection. There is no other way to implement context based authentication so a degree of uncertainty will be there but the potential gain is promising)

class Listen:
    class TrackOrCount(Enum):
        Count = auto()
        Track = auto()
        Nothing = auto()
    
    class Listener(Enum):
        Call = auto()
        InvokedCall = auto()
        Set = auto()
        InvokedSet = auto()

    call: Union[list[list[inspect.FrameInfo]], int, None] = list[list[inspect.FrameInfo]]
    set: Union[list[list[inspect.FrameInfo]], int, None] = list[list[inspect.FrameInfo]]
    call_type = TrackOrCount.Track
    set_type = TrackOrCount.Track
    # TODO History of changes (if option specified)
    # TODO Invoked call and set
    # TODO Only update the history of changes with inspect.stack only
    # upon lock.

    def __init__(
            self,
            value, 
            call = TrackOrCount.Track, 
            set = TrackOrCount.Track, 
        ):
        self._value = value
        self.call_type = call
        self.set_type = set

        if call == self.TrackOrCount.Nothing:
            self.call = None
        if set == self.TrackOrCount.Nothing:
            self.set = None
        if call == self.TrackOrCount.Count:
            self.call = 0
        if set == self.TrackOrCount.Count:
            self.set = 0
        if call == self.TrackOrCount.Track:
            self.call: list[inspect.FrameInfo] = []
        if set == self.TrackOrCount.Track:
            self.set: list[inspect.FrameInfo] = []

    def is_instantiated_or_populated(self, listen_target_type: list[inspect.FrameInfo]):
        if (isinstance(listen_target_type, list) or (isinstance(listen_target_type, list) and all(
            isinstance(frame, inspect.FrameInfo) for item in listen_target_type for frame in item)) or (
             isinstance(listen_target_type, list) and len(listen_target_type) == 0)):
             return True
        else:
            return False

    # region lock in type of listener
    
    class LockInListener:
        class Shareable:
            def __init__(self, listener: Listen.Listener, stack: inspect.FrameInfo):
                self.listener = listener
                self.stack = stack

            def append(self, new_listener: Listen.Listener):
                self.listener = new_listener

        @dataclass
        class SetStackTrace(Shareable):
            pass

        @dataclass
        class GetStackTrace(Shareable):
            pass
        
        def __init__(self):
            self.stack_trace = {
                'set': self.SetStackTrace(Listen.Listener.Set, inspect.stack()),
                'get': self.GetStackTrace(Listen.Listener.Call, inspect.stack())
            }
            self._lock_in_listener = None
            self.lock_in_listener_stack_trace = []

        @property
        def lock_in_listener(self):
            return self._lock_in_listener

        @lock_in_listener.setter
        def lock_in_listener(self, new_listener: Listen.Listener):
            if self._lock_in_listener == new_listener:
                raise Exception("Tried to change lock_in_listener with it being the same.")
            self.lock_in_listener_stack_trace.append(self.Shareable(new_listener, inspect.stack()))
            self._lock_in_listener = new_listener

        def lock_in_listener_bypass(self, new_listener: Listen.Listener):
            # No validation unlike lock_in_listener
            self.lock_in_listener_stack_trace.append(self.Shareable(new_listener, inspect.stack()))
            self._lock_in_listener = new_listener

        @property
        def listener(self) -> Union[list[list[inspect.FrameInfo]], int, None]:
            if self.lock_in_listener == Listen.Listener.Call:
                self.stack_trace['get'].append(Listen.Listener.Call)
                return self.call
            elif self.lock_in_listener == Listen.Listener.Set:
                self.stack_trace['set'].append(Listen.Listener.Set)
                return self.set
            else:
                raise Exception("Invalid listener type")
    # endregion

    @property
    def value(self):
        if self.call is None and self.call_type is self.TrackOrCount.Nothing:
            pass
        elif isinstance(self.call, int) and self.call_type is self.TrackOrCount.Count:
            self.call += 1
        elif self.is_instantiated_or_populated(self.call) and self.call_type is self.TrackOrCount.Track:
            """Either empty list or a populated one"""
            stack = inspect.stack()
            self.call.append(stack)
        else:
            logger.error("Unknown internal error in value getter.")
            raise ValueError("Unknown internal error in value getter.")
        return self._value

    @value.setter
    def value(self, new_value):
        if self.set is None and self.set_type is self.TrackOrCount.Nothing:
            pass
        elif isinstance(self.set, int) and self.set_type is self.TrackOrCount.Count:
            self.set += 1
        elif self.is_instantiated_or_populated(self.set) and self.set_type is self.TrackOrCount.Track:
            stack = inspect.stack()
            self.set.append(stack)
        else:
            logger.error("Unknown internal error in value setter.")
            raise ValueError("Unknown internal error in value setter.")
        self._value = new_value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Listen(value={self.value!r})"

    def __eq__(self, other):
        """Override equality operator."""
        if isinstance(other, (str, int, bool)):
            return self._value == other
        return False

    def __len__(self):
        return len(str(self.value))

    def __getitem__(self, index):
        # TODO Give more context of this type of lookup
        return self.value[index]
 

class TestListen:
    # Example:
    # @pytest.fixture
    # def setup(self):
    #     listen = Listen("Hi! Before update.")
    #     tsprint("Setting up listen")
        
    #     yield (listen)
        
    #     tsprint("Tearing down listen")


    # TODO Refactor out reusable code, Make sure the results of the refactored code outputs
    # the same results as prior to refactoring.
    def test_listen_call_None(self):
        listen = Listen("Hi! Before update.", call=Listen.TrackOrCount.Nothing)
        assert listen.call is None, "Call is not set to None when explicitly set to that."
        tsprint(listen, "Call 1")
        if listen:
            tsprint(f'{listen} From if statement. Call 2.')
        else:
            raise Exception("Listen has no value.")
        assert listen.call is None, "Call is not set to None when explicitly set to that after some changed."
    def test_listen_set_None(self):
        listen = Listen("Hi! Before update.", set=Listen.TrackOrCount.Nothing)
        assert listen.set is None, "Set is not set to None when explicitly set to that."
        tsprint(listen, "Set 1")
        if listen:
            tsprint(f'{listen} From if statement. Set 2.')
        else:
            raise Exception("Listen has no value.")
        assert listen.set is None, "Set is not set to None when explicitly set to that after some changed."

    def test_listen_call_Count(self):
        listen = Listen("Hi! Before update.", call=Listen.TrackOrCount.Count)
        assert isinstance(listen.call, int), "Not instance of int"
        tsprint(listen, "Call 1")
        if listen: # Call 2
            tsprint(f'{listen} From if statement. Call 3.')
        else:
            raise Exception("Listen has no value.")
        assert isinstance(listen.call, int), "Not instance of int after some changing."
        assert listen.call is 3, f"Listen has been viewed 3 times but count is {listen.call}"
    def test_listen_set_Count(self):
        listen = Listen("Hi! Before update.", set=Listen.TrackOrCount.Count)
        assert isinstance(listen.set, int), "Not instance of int"
        listen.value = "Hi! After update 1."
        tsprint(listen, "Set 1")
        if listen:
            listen.value = "Hi! After update 2."
        else:
            raise Exception("Listen has no value.")
        assert isinstance(listen.set, int), "Not instance of int after some changing."
        assert listen.set is 2, f"Listen has been set 2 times but count is {listen.set}"

    def test_listen_call_Track(self):
        listen = Listen("Hi! Before update.", call=Listen.TrackOrCount.Track)
        assert isinstance(listen.call, list)
        assert len(listen.call) is 0
        tsprint(listen, "Call 1")
        tsprint(len(listen), "Call 2")
        if listen: # Call 3
            tsprint(f'{listen} From if statement. Call 4')
        else:
            raise Exception(f"Listen has no value. Value: '{listen}'")
        assert isinstance(listen.call, list) and all( # Call 5
            isinstance(frame, inspect.FrameInfo) for item in listen.call for frame in item), "Call not instance of list[inspect.FrameInfo] after some changing."
        assert len(listen.call) is 4, f"Listen has been viewed/called 5 times but stack len is {len(listen.call)}"
    def test_listen_set_Track(self):
        listen = Listen("Hi! Before update.", set=Listen.TrackOrCount.Track)
        assert isinstance(listen.set, list)
        assert len(listen.set) is 0
        listen.value = "Hi! After update 1."
        assert len(listen.set) is 1
        tsprint("Set 1")
        if listen:
            listen.value = "Hi! After update 2."
            assert len(listen.set) is 2
            tsprint("setting the same thing to itself")
            listen.value = "Hi! After update 2."
            assert len(listen.set) is 3
        else:
            raise Exception(f"Listen has no value. Value: '{listen}'")
        assert isinstance(listen.set, list) and all(
            isinstance(frame, inspect.FrameInfo) for item in listen.set for frame in item), "Set not instance of list[inspect.FrameInfo] after some changing."
        assert len(listen.set) is 3, f"Listen has been set 3 times but stack len is {len(listen.set)}"
    
    def test_listen_stack_saved(self):
        description("Testing listen.call is instance of list and inner item is instance of inspect.FrameInfo")
        listen = Listen("Hi! Before update.", call=Listen.TrackOrCount.Track)
        tsprint(listen, "Call 1")
        assert len(listen.call) == 1, f"Only once was listen viewed/called but we get '{len(listen.call)}' calls"
        assert isinstance(listen.call, list) and all(
            isinstance(frame, inspect.FrameInfo) for item in listen.call for frame in item), "Call not instance of list[inspect.FrameInfo] after some changing."
