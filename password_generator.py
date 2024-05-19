# Password generator

import random
import string

charecters = string.ascii_letters + string.digits + string.punctuation
password_length = 16 # set password length here
password = "".join(random.sample(charecters, password_length))
print(password)
