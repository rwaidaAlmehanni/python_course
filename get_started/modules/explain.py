# Modules are reusable libraries of code in Python. Python comes with many standard library modules.

# A module is imported using the import statement.

# >>> import time
# >>> print time.asctime()
# 'Fri Mar 30 12:59:21 2012'

# In this example, we’ve imported the time module and called the asctime function from that module, which returns current time as a string.

# There is also another way to use the import statement.

# >>> from time import asctime
# >>> asctime()
# 'Fri Mar 30 13:01:37 2012'

# Here were imported just the asctime function from the time module.

# The pydoc command provides help on any module or a function.

# $ pydoc time
# Help on module time:

# NAME
#     time - This module provides various functions to manipulate time values.
# ...

# $ pydoc time.asctime
# Help on built-in function asctime in time:

# time.asctime = asctime(...)
#     asctime([tuple]) -> string
# ...

# On Windows, the pydoc command is not available. The work-around is to use, the built-in help function.

# >>> help('time')
# Help on module time:

# NAME
#     time - This module provides various functions to manipulate time values.
# ...

