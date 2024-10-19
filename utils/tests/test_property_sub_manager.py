import pytest
from unittest.mock import Mock
from utils.property_sub_manager import PropertySubscriptionManager, Listen

class TestPropertySubscriptionManager:
    # TODO TODO Uncomment these tests and get them to work

    def setup_method(self):
        self.sub_manager = PropertySubscriptionManager()

    # def test_subscribe_and_notify(self):
    #     mock_callback = Mock()
    #     self.sub_manager.subscribe('test_property', mock_callback)
    #     self.sub_manager.notify('test_property', 'new_value')
    #     mock_callback.assert_called_once_with('new_value')

    # def test_unsubscribe(self):
    #     mock_callback = Mock()
    #     self.sub_manager.subscribe('test_property', mock_callback)
    #     self.sub_manager.unsubscribe('test_property', mock_callback)
    #     self.sub_manager.notify('test_property', 'new_value')
    #     mock_callback.assert_not_called()

    # def test_subscribe_with_invalid_property(self):
    #     mock_callback = Mock()
    #     with pytest.raises(ValueError):
    #         self.sub_manager.subscribe(None, mock_callback)

    # def test_unsubscribe_with_invalid_property(self):
    #     mock_callback = Mock()
    #     with pytest.raises(ValueError):
    #         self.sub_manager.unsubscribe(None, mock_callback)

    # def test_notify_with_invalid_property(self):
    #     with pytest.raises(ValueError):
    #         self.sub_manager.notify(None, 'new_value')


    def test_listen(self):
        my_value1z = Listen("My data before update")
        my_value_after_update = "My data after update"
        print(my_value1z, "my_value1z")

        assert my_value1z == "My data before update"
        my_value1z = my_value_after_update
        assert my_value1z is not "My data before update"
        assert my_value1z is my_value_after_update

    def test_sub_update(self):
        qmy_prev_val = "My data before update"
        my_value = Listen("My data before update")
        qmy_value_after_update = "My data after update"

        # print("k dude")
        # prev_update_value = "fuck"
        # value = prev_update_value

        # def generic_callback(update_to):
        #     nonlocal value
        #     value = update_to

        self.sub_manager.subscribe(
            my_value,
            "fk",
            "update in real time",
            # "update in real time" or f"update but only after some process is finished. So deadlock in the mean time or disallowed until.",
            # set_value_request, 
            # callback_for_when_value_is_requested_to_view
        )
        qres = self.sub_manager._get("fk")
        assert qres is my_value

        qval_to_update_to = "fkly"
        self.sub_manager.request_set("fk", qval_to_update_to)

        assert my_value is not qmy_prev_val
        assert qval_to_update_to is not qmy_value_after_update
        assert my_value is qval_to_update_to
        assert qval_to_update_to is "fkly"

if __name__ == "__main__":
    print("fuck python")
    test = TestPropertySubscriptionManager()
    test.test_sub_update()
    print("fuck python")