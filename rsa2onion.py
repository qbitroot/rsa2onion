import argparse

from base64 import b32encode
from hashlib import sha1, sha3_256
from Crypto.PublicKey import RSA, ECC

def onion_address_v2(priv_key_file):
	with open(priv_key_file) as f:
		private_key = RSA.import_key(f.read())
	public_key = private_key.publickey().exportKey('DER')[22:]
	m = sha1()
	m.update(public_key)
	sha_hash = m.digest()
	half = sha_hash[:10]
	return b32encode(half).lower()

def onion_address_v3(priv_key_file):
	with open(priv_key_file) as f:
		priv_key = ECC.import_key(f.read())

	public_key = priv_key.public_key().export_key(format='raw')
	version = b"\x03"
	checksum = sha3_256(b".onion checksum" + public_key + version).digest()[:2]
	onion_address = b32encode(public_key + checksum + version).lower()
	return onion_address

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('file', type=str, help='private key file')
	parser.add_argument('-v', '--version', type=int, help='onion service address version, 2 or 3.')

	args = parser.parse_args()
	if args.version is None:
		args.version = 2
	if args.version == 3:
		print(onion_address_v3(args.file).decode() + '.onion')
	elif args.version == 2:
		print(onion_address_v2(args.file).decode() + '.onion')
	else:
		parser.print_help()
