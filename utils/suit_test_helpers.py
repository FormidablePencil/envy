from colorama import Fore, Back, Style, init

def description(description):
    print(Fore.CYAN + 
        f"""
==  =========     ===========    =========
{description}
===   ================     =========    =====
""" + Fore.WHITE)

def tsprint(print_statement, *args, **kwargs):
    test = True
    if test:
        print(print_statement)
        for arg in args:
            print(arg)
        for key, value in kwargs.items():
            print(f"{key}: {value}")
# Usage
# tsprint("This is a print statement", "Argument 1", "Argument 2", key1="Value 1", key2="Value 2")
