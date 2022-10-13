#!/usr/bin/python3
import inspect
import io
import sys
import cmd
import shutil
import os
import console


"""
 Create console
"""
console_obj = "HBNBCommand"
for name, obj in inspect.getmembers(console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_obj = obj

my_console = console_obj(stdout=io.StringIO(), stdin=io.StringIO())
my_console.use_rawinput = False


"""
 Exec command
"""
def exec_command(my_console, the_command, last_lines = 1):
    my_console.stdout = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = my_console.stdout
    my_console.onecmd(the_command)
    sys.stdout = real_stdout
    lines = my_console.stdout.getvalue().split("\n")
    return "\n".join(lines[(-1*(last_lines+1)):-1])


"""
 Tests
"""
result = exec_command(my_console, "all Amenity", 4)
if result is None or result == "":
    print("FAIL: No amenities retrieved")
if "my_id_0" not in result or "my_name_0" not in result :
    print("FAIL: Missing information 0")
if "my_id_1" not in result or "my_name_1" not in result :
    print("FAIL: Missing information 1")
if "my_id_2" not in result or "my_name_2" not in result :
    print("FAIL: Missing information 2")
if "my_id_3" not in result or "my_name_3" not in result :
    print("FAIL: Missing information 3")
    
print("OK", end="")

shutil.copy("tmp_console_main.py", "console.py")
