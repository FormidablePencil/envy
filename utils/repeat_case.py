from typing import TypedDict, Optional, Generic, TypeVar
from dataclasses import dataclass
from typing import Callable
from utils.validation.internal_state_management import InternalStateManagement

# TODO give a Enum constraint on generic T
# TODO Create higher level class to handle different types of eval since eval()
# can be unsafe in certain circumstances

@dataclass
class CaseCodePath:
    call: Callable[[any], any]
    case: str
    rerun = False
    # TODO Test exempt from rerun True and False variation and test exempt from rerun from all cases
    exempt_from_rerun_from_self_case = True # Exempt from run() if rerun=True on any case when rerunning run() again. Set to true by default to avoid running the same code path again unecessarily
    exempt_from_rerun_from_all_cases = False
    def __init__(
            self,
            call: Callable[[any], any],
            case: str,
            rerun = False,
            exempt_from_rerun_from_self_case = True, # TODO Find a non intrusive way to dynamically document things like this for instance
            exempt_from_rerun_from_all_cases = False,
        ):
        self.call = call
        self.case = case
        self.rerun = rerun
        self.exempt_from_rerun_from_self_case = exempt_from_rerun_from_self_case # Exempt from run() if rerun=True on any case when rerunning run() again. Set to true by default to avoid running the same code path again unecessarily
        self.exempt_from_rerun_from_all_cases = exempt_from_rerun_from_all_cases

class RepeatCase:
    case_code_paths: list[CaseCodePath] = []
    rerun_case: list[bool]
    internal_state_manager: InternalStateManagement

    def __init__(self, exempt_realtime_mod = False):
        self._exempt_realtime_mod = exempt_realtime_mod # exempt_from_modifying_cases_for_real_time TODO add comments to variables. Internal code via doc comments for variable documentation is useful but also non intrusive yet highly accessible documentation is neccessary too

    @property
    def exempt_realtime_mod(self):
        # TODO Save in db context from which it was called and increment call of context


        return self._exempt_realtime_mod

    @exempt_realtime_mod.setter
    def exempt_realtime_mod(self, value: bool):
        self._exempt_realtime_mod = value

    # Internal validation can be useful for real time testing rather than
    # a simulated environemnt to test against. TODO add a way to assign certain
    # things trivial documentation like for this instance.
    def internal_validation_of_case_exampt_internal_managment(self, case, is_exampt_from_rerun):
        if self.rerun_case[case] and is_exampt_from_rerun == False:
            # TODO Implement a robust Internal error manager that also keep track of where
            # it is being called from too and whether certain places do run validation and
            # in other places that explicately don't need to
            raise Exception("Internal error. Never should have occured.")
    
    def internal_validation_of_exempt_realtime_mod_updated():

    def append(
            self,
            call: Callable[[any], any],
            case: str,
            rerun = False,
            exempt_in_rereun = True,
        ) -> None:
        self.case_code_paths.append(CaseCodePath(call, case, rerun, exempt_in_rereun))

    # Will modify cases that are exempt_from_rerun_from_self_case=True or exempt_from_rerun_from_all_cases=True but will be reset back at the end
    # If you desire to opt out from modifying cases then set opt_out_case_mod=True, keeping track of what to opt out from rerun is internally handled
    # TODO Add this comment to class and variable opt_out_case_mod=True
    def run(self) -> None:
        """
        Executes the appropriate case code path based on the evaluated conditions.
        If a case code path requires a rerun the rerun value is then set to false.
        """
        for case_code_path in self.case_code_paths:
            if case_code_path.case:
                case_code_path.call()
                # TODO Create a validator of cases to not be duplicate and an option to allow
                # TODO Implement a validator for only allowing 1 of 2 types of rerun exemptions
                # TODO self.rerun_case=True and is_exampt_from_rerun=False should never be
                if not self.rerun_case[case_code_path.case]:
                    is_exempt_from_rerun = case_code_path.exempt_from_rerun_from_self_case or case_code_path.exempt_from_rerun_from_all_cases 
                    if is_exempt_from_rerun:
                        # Will keep track of rerun case internally and by default will 
                        # override cases in realtime. set exempt_realtime_mod=True to 
                        # opt out. User will have to solely rely on internal case rerun 
                        # exemptions without being able to conditionally update case from 
                        # passed in code callbacks for a given case. TODO move this comment
                        # to somewhere where it makes more sense and just reference this point
                        # to it once proper code documenttion with advanced and robust database
                        # storing and retrieval for code is implemented
                        if not self.exempt_realtime_mod:
                            case_code_path.case = True
                            self.rerun_case[case_code_path.case] = True
                        elif self.exempt_realtime_mod: # TODO Document that exempt_realtime_mod was called twice (if statement prior to this one) and for what reasons/context. Update: Partually implemented.
                            self.rerun_case[case_code_path.case] = True
                        else
                        raise Exception("self.rerun_case has never been updated")
                elif case_code_path.rerun and self.rerun_case[case_code_path.case] == False:
                    if case_code_path.exempt_from_rerun_from_all_cases:
                    if case_code_path.exempt_from_rerun_from_self_case:
                        self.rerun_case[case_code_path.case]

                    case_code_path.rerun = False
                    case_code_path.rerun = False
                    self.run()
                else
                    raise Exception("Internal code path error.")
                self.internal_validation_of_case_exampt_internal_managment(case_code_path.case, is_exempt_from_rerun)
        self.reset_cases_rerun_exempted()
    
    def reset_cases_rerun_exempted():


class Test:
    # TODO Make this a test and find a pytest library to allow tests in the same file
    # as the business logic that won't go to production
    def test_does_modify_conditions_from_passed_code_for_case():
        def change_condition_1():
            nonlocal condition_1
            condition_1 = False

        condition_1 = True
        condition_2 = True

        rc = RepeatCase()
        rc.append(lambda: print("Case 1 executed"), condition_1)
        rc.append(change_condition_1, condition_2)
        rc.run()

        assert condition_1 == False
        assert condition_2 == True

    # TODO Find a library to give tests more context with descriptions at least
    def test_repeating_code_paths_that_change_previous_condition_and_when_rerun_the_change_to_condition_is_applied_also_code_cases_dont_rerun_unnecessarily_multiple_times():
        rc = RepeatCase()
        condition_1 = False
        condition_2 = False
        condition_3 = True
        reset = False

        test_has_run_run_1_and_2_conditions_count = 0
        test_has_run_reset_conditions_count = 0

        def run_1_and_2_conditions():
            nonlocal condition_1
            nonlocal condition_2
            nonlocal condition_3
            nonlocal reset
            condition_1 = True
            condition_2 = True
            condition_3 = False
            reset = True
            # TODO Implement unit test by dependency injecting this function instead
            # and validating that it was called given the right cirumstance that is
            nonlocal test_has_run_run_1_and_2_conditions_count
            test_has_run_run_1_and_2_conditions_count += 1
            print("k2k")

        def reset_conditions():
            nonlocal condition_1
            nonlocal condition_2
            nonlocal condition_3
            nonlocal reset
            condition_1 = False
            condition_2 = False
            condition_3 = True
            reset = False
            # TODO Implement unit test by dependency injecting this function instead
            # and validating that it was called given the right cirumstance that is
            nonlocal test_has_run_reset_conditions_count
            test_has_run_reset_conditions_count += 1
            print("k k")

        rc.append(lambda: print("Case 1 executed"), condition_1)
        rc.append(lambda: print("Case 2 executed"), condition_2)
        rc.append(run_1_and_2_conditions, condition_3, rerun=True) # TODO When a conditional 
        # mod is presented then save conditional state and when revert_condition(commit: int)
        # is called then revert back to commit before the change occured.
        # If there are multiple mod conditions then state will be commited and can be reverted
        # to with <commit> in revert_condition(commit: int). Currently a reset condition with
        # reset logic has to be provided just as every other condition via .append()
        rc.append(reset_conditions, case=True)
        rc.run()

        assert test_has_run_run_1_and_2_conditions_count == 1
        assert test_has_run_reset_conditions_count == 1

if __name__ == "__main__":
    Test.test_repeating_code_paths_that_change_previous_condition_and_when_rerun_the_change_to_condition_is_applied_also_code_cases_dont_rerun_unnecessarily_multiple_times()
    # Test.test_does_modify_conditions_from_passed_code_for_case()
