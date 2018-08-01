import importlib.util
import sys

import signal
from contextlib import contextmanager
import random

class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

spec = importlib.util.spec_from_file_location("module.name", sys.argv[1])
submitted_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(submitted_module)

if not hasattr(submitted_module, 'add'):
    print(0)
    exit(0)

# tests_input = [(1, 2), (3, 4)]
# expected_outputs = [3, 7]

# score = 0

# for i in range(len(tests_input)):
#     test = tests_input[i]
#     expected_output = expected_outputs[i]
#     try:
#         with time_limit(10):
#             submitted_output = submitted_module.add(test[0], test[1])
#             score += int(submitted_output == expected_output)
#     except TimeoutException as e:
#         continue

# print(score)

score = 0
for i in range(10):
    test = (random.randint(-1000, 1000), random.randint(-1000, 1000))
    expected_output = test[0] + test[1]
    try:
        with time_limit(10):
            submitted_output = submitted_module.add(test[0], test[1])
            score += int(submitted_output == expected_output)
    except TimeoutException as e:
        continue

print(score)