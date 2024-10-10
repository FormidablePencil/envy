# Since .bashrc has `alias py='~/envy/py/main.py` and since the command isn't run as a
# module such as in `python3 -m main`relative paths won't work nor does importing through
# `py` module doesn't work. Although its not applicable to the target files and directories
# specified as an argument since under the hood of the `py` command it just runs python3
# or pytest depending on the flags. But when modifying py you'll have be considerate of 
# any names of files that may conflict with other files and modules that are in envy/ 
# like for instance the py/util.py was originally py/utils.py but conflicted with a
# file/module that was in envy/