import os
import re
import subprocess

test_files: list[str] = []

with os.scandir("../") as it:
    for entry in it:
        match = re.fullmatch(r"\w*.py", entry.name)
        if match is None:
            continue
        py_file = match.group(0)
        test_files.append(py_file)

os.chdir("../")
for test_file in test_files:
    proc = subprocess.run(["pytest", test_file])
    data = proc.stdout
    result = proc.returncode
    print(f"execute file: {test_file}")
    print(f"exit code: {result}")
    print("**************")
    if result != 0:
        exit(result)

exit(0)
