import random
import secrets

number = random.SystemRandom().random()
print("secure number is ", number)

print("Secure byte token", secrets.token_bytes(16))