from .models import Member

import requests

def complex_hash(key, table_size = 20):
  hash_value = 0
  prime = 31
  for i, char in enumerate(key):
    hash_value += ord(char) * (prime ** i)
  return hash_value % table_size