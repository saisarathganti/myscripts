# Password generator

import random
import string
import sys

charecters = string.ascii_letters + string.digits + string.punctuation
password_length = int(sys.argv[1]) if sys.argv[1] else 16
password = "".join(random.sample(charecters, password_length))
print(password)
