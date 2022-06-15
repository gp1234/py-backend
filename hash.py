import base64
import binascii
import hmac
import time
import os

from hashlib import sha512



def get_signature(message):
  secret = os.environ.get("SECRET_KEY")
  timestamp = str(int(time.time()))
  stamped_message = str(str(message) + '.' + timestamp).encode()
  secret_bin = binascii.unhexlify(secret)
  hash_websafe = base64.urlsafe_b64encode(hmac.new(secret_bin, stamped_message, sha512).digest())
  signature = stamped_message.decode('utf-8') + '.' + hash_websafe.decode('utf-8')

  return signature.rstrip('=')
