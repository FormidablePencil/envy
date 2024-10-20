import inspect
from utils.listen import Listen
from utils.suit_test_helpers import description, tsprint
from enum import Enum, auto
import pytest
from pytest import FixtureRequest
from dataclasses import dataclass
from typing import Union, Generator

# TODO Maybe rename this since tests will be also used as checkpoints

class ListenCP:
    class Type(Enum):
        call = auto(),
        set = auto(),
        both = auto()

class TestListen:

    @dataclass
    class ListenParams:
        type: ListenCP.Type
        call: Listen.TrackOrCount = Listen.TrackOrCount.Track
        set: Listen.TrackOrCount = Listen.TrackOrCount.Track

    listen_initial_content = "Hi! Before update."
    
    # region Refactored code

    def type_of_both_not_allowed(self, type: ListenCP.Type):
        if type == ListenCP.Type.both:
            Exception("Even though Type.both is used some place else it can't be used in 'type'")
        elif type == ListenCP.Type.call or type == ListenCP.Type.set:
            pass
        else:
            raise Exception("Didn't account for other types.") # TODO Create a function for getting the reset of the types that were't covered in a similar fashion as repeat_case.py

    @pytest.fixture
    def setup_listen_of_type(self, request: FixtureRequest) -> Generator[tuple[Listen, ListenParams], None, None]:
        param: TestListen.ListenParams = request.param

        if param.type == ListenCP.Type.call:
            listen = Listen(value = self.listen_initial_content, call = param.call)
        elif param.type == ListenCP.Type.set:
            listen = Listen(value = self.listen_initial_content, set = param.set)
        elif param.type == ListenCP.Type.both:
            listen = Listen(value = self.listen_initial_content, call = param.call, set = param.set)

        yield listen, param
        tsprint("Tearing down Listen")

    default_listen_None_args = [
        ListenParams(type = ListenCP.Type.call, call = Listen.TrackOrCount.Nothing, set = Listen.TrackOrCount.Nothing),
        ListenParams(type = ListenCP.Type.set, call = Listen.TrackOrCount.Nothing, set = Listen.TrackOrCount.Nothing),
    ]

    @pytest.mark.parametrize('setup_listen_of_type', default_listen_None_args, indirect=True)
    def test_listen_None2(self, setup_listen_of_type: tuple[Listen, ListenParams]):
        listen, param = setup_listen_of_type
        self.listen_None_CP(param.type, listen)

    def listen_None_CP(self, type: ListenCP.Type, listen: Listen):
        self.type_of_both_not_allowed(type)

        # Setting for dynamic validation
        if type == ListenCP.Type.call:
            listen.lock_in_listener = Listen.Listener.Call
        elif type == ListenCP.Type.set:
            listen.lock_in_listener = Listen.Listener.Set
        else:
            raise Exception("Make sure type_of_both_not_allowed is in place since it sould have caught the type error.")

        # Validate listen of type None
        assert listen.listener is None, f"{type} is not set to None when explicitly setting '{type}' = Listen.TrackOrCount.Nothing."

        # Action
        if type == ListenCP.Type.call:
            tsprint(listen, "Call 1")
        elif type == ListenCP.Type.set:
            listen.value = "Hi! After update 1."
        else:
            Exception("Make sure type_of_both_not_allowed is in place") # TODO Reusing the same pattern and can be refactored even further out with util helper to set up else upon instantiation and setting it to the same exception.

        # Validate 2 birds with one stone (type.call and type.set) previous action was successful
        assert listen.listener is None

        # Action call in if statement and validate
        if listen:
            if type == ListenCP.Type.call:
                assert len(listen.listener) is 2
            elif type == ListenCP.Type.set:
                pass
            else:
                Exception("Make sure type_of_both_not_allowed is in place")
        else:
            raise Exception("Listen has no value.")
        
        # Validate there were no significant changes
        assert listen.listener is None, f"{type} is not set to None when explicitly setting Listen.TrackOrCount to '{type}' after some changed."

    default_listen_Count_args = [
        ListenParams(type = ListenCP.Type.call, call = Listen.TrackOrCount.Count, set = Listen.TrackOrCount.Nothing),
        ListenParams(type = ListenCP.Type.set, call = Listen.TrackOrCount.Nothing, set = Listen.TrackOrCount.Count),
    ]
    @pytest.mark.parametrize('setup_listen_of_type', default_listen_Count_args, indirect=True)
    def test_listen_Count2(self, setup_listen_of_type: tuple[Listen, ListenParams]):
        listen, param = setup_listen_of_type
        self.listen_Count_CP(param.type, listen)

    def listen_Count_CP(self, type: ListenCP.Type, listen: Listen):
        self.type_of_both_not_allowed(type)

        # Setting for dynamic validation
        if type == ListenCP.Type.call:
            listen.lock_in_listener = Listen.Listener.Call
            tsprint(listen, "Call 1")
            assert listen.call is 1
            assert listen.listener is 1
        elif type == ListenCP.Type.set:
            listen.lock_in_listener = Listen.Listener.Set
            listen.value = "made change"
            assert listen.set is 1
            assert listen.listener is 1
        else:
            raise Exception("Make sure type_of_both_not_allowed is in place since it sould have caught the type error.")

        # validate target of type int
        assert isinstance(listen.listener, int), f"'{type}' is not instance of int when explicitly setting Listen.TrackOrCount to '{type}'"

        # Make changes
        tsprint(listen, "Call 2")
        listen.value = "Hi! After update. 1" # TODO Create an auto incrementor for updating values

        # Validate call stack was recorded when changes were made
        if listen: # Call 3
            if type == ListenCP.Type.call:
                tsprint(f'{listen} From if statement and one Call here which makes it 3.')
                assert listen.listener is 4
            elif type == ListenCP.Type.set:
                assert listen.listener is 2
            else:
                raise Exception("Make sure type_of_both_not_allowed is in place since it sould have caught the type error.")
        else:
            raise Exception("Listen has no value.")

        # Validate those changes
        assert isinstance(listen.listener, int), f"'{type}' is not instance of int when explicitly setting Listen.TrackOrCount to '{type}'"
        if type == ListenCP.Type.call:
            assert listen.listener == 4 if type == ListenCP.Type.call else 2, f"Listen has been '{type}' {4 if type == ListenCP.Type.call else 2} times but count is {listen.listener}"
        elif type == ListenCP.Type.set:
            assert listen.listener == 2 if type == ListenCP.Type.set else 4, f"Listen has been '{type}' {2 if type == ListenCP.Type.set else 4} times but count is {listen.listener}"
        else:
            raise Exception("Make sure type_of_both_not_allowed is in place since it sould have caught the type error.") 

    default_listen_Track_args = [
        ListenParams(type = ListenCP.Type.call, call = Listen.TrackOrCount.Track, set = Listen.TrackOrCount.Nothing),
        ListenParams(type = ListenCP.Type.set, call = Listen.TrackOrCount.Nothing, set = Listen.TrackOrCount.Track),
    ]
    @pytest.mark.parametrize('setup_listen_of_type', default_listen_Track_args, indirect=True)
    def test_listen_Track2(self, setup_listen_of_type: tuple[Listen, ListenParams]):
        listen, param = setup_listen_of_type
        self.listen_Track_CP(param.type, listen)

    # TODO Track3, abstract out different methods of validation

    def listen_Track_CP(self, type: ListenCP.Type, listen: Listen):
        self.type_of_both_not_allowed(type)

        # Setting for dynamic validation
        if type == ListenCP.Type.call:
            listen.lock_in_listener = Listen.Listener.Call
        elif type == ListenCP.Type.set:
            listen.lock_in_listener = Listen.Listener.Set
        else:
            raise Exception("Make sure type_of_both_not_allowed is in place since it sould have caught the type error.")

        print("statement")
        print(type, "type")
        print(listen.listener, "leng")
        print(len(listen.listener), "leng")
        assert isinstance(listen.listener, list) and len(listen.listener) is 0, f"listen.'{type}' not properly instantiated to empty list"

        # Make changes and validate
        if type == ListenCP.Type.call:
            tsprint(listen, "listen.call invoked 1.")
            assert len(listen.listener) is 1
        elif type == ListenCP.Type.set:
            listen.value = "Hi! After update 1."
            tsprint("Set invoked 1")
            assert len(listen.listener) is 1

        if listen: # Call 2
            if type == ListenCP.Type.call:
                tsprint(listen, 'Once invoked from if statement. And once invoked from here. 3')
                assert len(listen.listener) is 3
            if type == ListenCP.Type.set:
                listen.value = "Hi! After update 2."
                assert len(listen.listener) is 2
                tsprint("Setting the same thing to itself")
                listen.value = "Hi! After update 3."
                assert len(listen.listener) is 3, "Setting the same thing to itself should have invoked set regardless."
        else:
            raise Exception(f"Listen has no value. Value: '{listen}'")

        # Validate target of those changes of type being the correct list of items (inspect.stack) TODO dynamic comments. Perhaps just introduce description that only runs in dev, test but not in prod
        assert isinstance(listen.listener, list) and len(listen.listener) > 0 and all(
            isinstance(frame, inspect.FrameInfo) for item in listen.listener for frame in item), f"'{type}' not instance of list[inspect.FrameInfo] after some changing."

        assert len(listen.listener) == 3 if type == ListenCP.Type.call else 3, f"Listen has been '{type}' {3 if type == ListenCP.Type.call else 3} times but count is {len(listen.listener)}"
        # assert listen.listener == 2 if type == ListenCP.Type.set else 4, f"Listen has been '{type}' {2 if type == ListenCP.Type.set else 4} times but count is {listen.listener}"

    # endregion Refactored code

    # region Unrefactored code
 
    default_listen_Nothing_args = [
        ListenParams(type = ListenCP.Type.call, call = Listen.TrackOrCount.Nothing, set = Listen.TrackOrCount.Count),
        ListenParams(type = ListenCP.Type.set, call = Listen.TrackOrCount.Track, set = Listen.TrackOrCount.Nothing),
    ]
    @pytest.mark.parametrize('setup_listen_of_type', default_listen_Nothing_args, indirect=True)
    def test_listen_None(self, setup_listen_of_type: tuple[Listen, ListenParams]):
        listen, param = setup_listen_of_type
        self.listen_None_CP(param.type, listen)

    def listen_None_CP(self, type: ListenCP.Type, listen: ListenParams):
        # Setting for dynamic validation
        if type == ListenCP.Type.call:
            listen.lock_in_listener = Listen.Listener.Call
        elif type == ListenCP.Type.set:
            listen.lock_in_listener = Listen.Listener.Set
        else:
            raise Exception("Make sure type_of_both_not_allowed is in place since it sould have caught the type error.")

        if listen: # Call 1 TODO Ability to leave notes to values. Here I could specify that 'call' in if statment is handled here too
            if type == ListenCP.Type.call:
                tsprint(listen.listener, 'From if statement. Call 2.')
                assert listen.listener is None
            if type == ListenCP.Type.set:
                listen.value = "New value update 1."
                assert listen.listener is None
        else:
            raise Exception("Listen has no value.")

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

    # endregion Unrefactored code


class checkpoint(dict):
    default_listen_None_args = TestListen.default_listen_None_args
    listen_None_CP = TestListen.listen_None_CP
    default_listen_Count_args = TestListen.default_listen_Count_args
    listen_Count_CP = TestListen.listen_Count_CP