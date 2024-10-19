import inspect
from utils.listen import Listen
from utils.suit_test_helpers import description, tsprint
from enum import Enum, auto
import pytest
from pytest import FixtureRequest
from dataclasses import dataclass

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
    def setup_listen_of_type(self, request: FixtureRequest):
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
    def test_listen_None2(self, setup_listen_of_type):
        listen, param = setup_listen_of_type
        self.listen_None_CP(param.type, listen)

    def listen_None_CP(self, type: ListenCP.Type, listen: Listen):
        self.type_of_both_not_allowed(type)
        # Set to target and validate target of type int
        if type == ListenCP.Type.call:
            listen_target_type = listen.call
        elif type == ListenCP.Type.set:
            listen_target_type = listen.set
        else:
            Exception("Make sure type_of_both_not_allowed is in place")
        assert listen_target_type is None, f"{'Call' if type == ListenCP.Type.call else 'Set'} is not set to None when explicitly setting Listen.TrackOrCount.Nothing."

        # Action
        if type == ListenCP.Type.call:
            tsprint(listen, "Call 1")
        elif type == ListenCP.Type.set:
            listen.value = "Hi! After update 1."
        else:
            Exception("Make sure type_of_both_not_allowed is in place")

        # Validate previous action was successful
        if type == ListenCP.Type.call:
            tsprint(listen, "Call 1")
        elif type == ListenCP.Type.set:
            listen.value = "Hi! After update 1."
            tsprint("Set 1")
        else:
            Exception("Make sure type_of_both_not_allowed is in place")

        # Validate changes of when listen is called/viewed/evaluated in an if statement
        if listen:
            if type == ListenCP.Type.call:
                tsprint(f'{listen} From if statement. Call 2.')
            elif type == ListenCP.Type.set:
                tsprint(f"Listen has value of: '{listen}'")
            else:
                Exception("Make sure type_of_both_not_allowed is in place")
        else:
            raise Exception("Listen has no value.")
        
        # Validate there were no significant changes
        assert listen_target_type is None, f"{'Call' if type == ListenCP.Type.call else 'Set'} is not set to None when explicitly setting Listen.TrackOrCount to '{type}' after some changed."

    default_listen_Count_args = [
        ListenParams(type = ListenCP.Type.call, call = Listen.TrackOrCount.Count, set = Listen.TrackOrCount.Nothing),
        ListenParams(type = ListenCP.Type.set, call = Listen.TrackOrCount.Nothing, set = Listen.TrackOrCount.Count),
    ]
    @pytest.mark.parametrize('setup_listen_of_type', default_listen_Count_args, indirect=True)
    def test_listen_Count2(self, setup_listen_of_type):
        listen, param = setup_listen_of_type
        self.listen_Count_CP(param.type, listen)

    def listen_Count_CP(self, type: ListenCP.Type, listen: Listen):
        self.type_of_both_not_allowed(type)

        # Set to target and validate target of type int
        if type == ListenCP.Type.call:
            listen_target_type = listen.call
        elif type == ListenCP.Type.set:
            listen_target_type = listen.set
        else:
            raise Exception("Make sure type_of_both_not_allowed is in place since it sould have caught the type error.")
        print(listen_target_type, "instance")
        assert isinstance(listen_target_type, int), f"{'Call' if type == ListenCP.Type.call else 'Set'} is not instance of int when explicitly setting Listen.TrackOrCount to '{type}'"

        # Make changes
        tsprint(listen, "Call 1")
        listen.value = "Hi! After update. 1"
        if listen: # Call 2
            if type == ListenCP.Type.call:
                tsprint(f'{listen} From if statement. Call 3.')
            elif type == ListenCP.Type.set:
                listen.value = "Hi! After update. 2" # TODO Create an auto incrementor for updating values
            else:
                raise Exception("Make sure type_of_both_not_allowed is in place since it sould have caught the type error.")
        else:
            raise Exception("Listen has no value.")

        # Validate those changes
        assert isinstance(listen_target_type, int), f"{'Call' if type == ListenCP.Type.call else 'Set'} is not instance of int when explicitly setting Listen.TrackOrCount to '{type}'"
        if type == ListenCP.Type.call or type == ListenCP.Type.set:
            assert listen_target_type == 2 if type == ListenCP.Type.call else 3, f"Listen has been viewed 3 times but count is {listen.call}"
        else:
            raise Exception("Make sure type_of_both_not_allowed is in place since it sould have caught the type error.")
        # Set 

    def test_listen_call_Track2(self):
        self.listen_Track(ListenCP.Type.call)
    def test_listen_set_Track2(self):
        self.listen_Track(ListenCP.Type.set)

    # TODO Track3, abstract out different methods of validation

    def listen_Track(self, type: ListenCP.Type):
        self.type_of_both_not_allowed(type)
        listen = self.setup_listen_of_type(type, call = Listen.TrackOrCount.Track, set = Listen.TrackOrCount.Track)

        # Set to target
        if type == ListenCP.Type.call:
            listen_target_type = listen.call
        elif type == ListenCP.Type.set:
            listen_target_type = listen.set
        else:
            raise Exception("Make sure type_of_both_not_allowed is in place since it sould have caught the type error.")

        assert isinstance(listen_target_type, list) and len(listen_target_type) is 0, f"listen.{'call' if type == ListenCP.Type.call else 'set'} not properly instantiated to empty list"

        # Make changes
        if type == ListenCP.Type.call:
            tsprint(listen_target_type, "listen.call invoked 1.")
        if type == ListenCP.Type.set:
            listen_target_type = "Hi! After update 1."
            tsprint("Set 1")
            assert len(listen_target_type) is 1
        if listen:
            if type == ListenCP.Type.call:
                tsprint(listen, "Call 1")
                tsprint(len(listen), "Call 2")
                if listen: # Call 3
                    tsprint(f'{listen}. Once invoked from if statement. And once invoked from here. 4')
            if type == ListenCP.Type.set:
                listen.value = "Hi! After update 2."
                assert len(listen_target_type) is 2
                tsprint("Setting the same thing to itself")
                listen.value = "Hi! After update 2."
                assert len(listen_target_type) is 3, "Setting the same thing to itself should have invoked set regardless."
                listen.value = "Hi! After update 4. For validation 2 birds with 1 stone."
        else:
            raise Exception(f"Listen has no value. Value: '{listen}'")

        # Validate target of those changes of type being the correct list of items (inspect.stack) TODO dynamic comments. Perhaps just introduce description that only runs in dev, test but not in prod
        assert isinstance(listen_target_type, list) and len(listen_target_type) > 0 and all(
            isinstance(frame, inspect.FrameInfo) for item in listen_target_type for frame in item), "Call not instance of list[inspect.FrameInfo] after some changing."
        assert len(listen_target_type) is 4, f"Listen.{'call' if type == ListenCP.Type.call else 'set'} has been invoked 4 times but stack len is {len(listen_target_type)}"

    # endregion Refactored code

    # region Unrefactored code
 
    def test_listen_call_None(self):
        listen = self.setup_listen_of_type(type = ListenCP.Type.call, call = Listen.TrackOrCount.Nothing)
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
        listen.value = "Hi! After update 1."
        tsprint("Set 1")
        if listen:
            tsprint(f'{listen} From if statement. Set 1.')
        else:
            raise Exception("Listen has no value.")
        assert listen.set is None, "Set is not set to None when explicitly set to that after some changed."

    def test_listen_call_Count(self):
        listen = Listen("Hi! Before update.", call=Listen.TrackOrCount.Count)
        assert isinstance(listen.call, int), "Not instance of int when explicitly setting Listen.TrackOrCount.Count"
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

    # endregion Unrefactored code


class checkpoint(dict):
    default_listen_None_args = TestListen.default_listen_None_args
    listen_None_CP = TestListen.listen_None_CP
    default_listen_Count_args = TestListen.default_listen_Count_args
    listen_Count_CP = TestListen.listen_Count_CP