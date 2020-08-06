from base64 import b64decode, b32encode, b16decode
from hashlib import sha1
from Crypto.PublicKey import RSA
from sys import argv

private_key = open(argv[1], 'rb').read().strip()

if private_key.startswith(b'-----'):
	private_key = b"".join(private_key.split(b'\n')[1:-1]).strip()

der = b64decode(private_key)
key = RSA.importKey(der)
private_key = RSA.construct((key.n, key.e, key.d, key.p, key.q))

public_key = private_key.publickey().exportKey('DER')[22:]
m = sha1()
m.update(public_key)
sha_hash = m.digest()
half = sha_hash[:10]
print(b32encode(half).decode().lower()+'.onion')
