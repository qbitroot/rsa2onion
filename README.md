# ⚙️ rsa2onion
Convert RSA private keys to .onion domains.

## Purpose?

When you place your private key to file named `private_key` at Tor hidden service directory, hostname is generated based on that key (or random if not set). This tool allows you to convert RSA private key to onion domain without necessity to paste key to file and restarting Tor hidden service to see what onion domain stands for that key.

## Usage

`python3 rsa2onion.py /path/to/private_key.pem`

File `private_key.pem` has to be in following format (PEM):

```
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC/3ancqN/SRYOEMKsgbIULDwTq543T6RQpWXKSFM5ako034fkE
/TcyLNk6oUt+QauRXOVTokuC2iLuk65vlLYC+UcSSmGxjbg2uCNyRAGM2idMkhuu
Nfr4ieDRKIzUh53DcTQEQpXF3A4nnZWHTYPKDgw6bNsOYCYGVkNSspv0NwIEAQAA
AwKBgFtM7ZcySlDyRytYiQXWJPTKM2geCjCZqpdEDif6l5/O6n8t340+SKEcsEno
FEO9XrM3xDSxJLlEAWko2atbHwKCMnbnsWf3Bb9Y46AeqNycd3qk2tClrX8pfpqx
Kf3+nXaw+YkSPTEexDOvOyam4C1C89AjF3+hAaWYcNepfPt7AkEA6jT6gLcXyk+W
muwxgyd59b/veFOF4pgR+OH5zmOD6/hVL36BP/pGiBGU3A7BU4UOMgxG8g2QA8E0
l2EhHM92wwJBANG4FRCX9TYVvy7JoDdAGhrUS6PZcOqcSckzy7uF9MkDTLazJte1
imWyqfyK0HkMKMcwbiBHi5nYFuTV0u7LvX0CQHyqthfSJ8aR8KP/Oj4FqUt1YEXh
rvc/v3E+AZltOiVh+OCvg18saBM+FzWnv9CT5WQeuoXrTgnXiqAW7z0nINkCQF/1
+OhpPp8QUuTq5vnu8GuNYf5Zlep6kNSTDCTCsVBPi/jAZd5udfdmXqslt4Wp7kQv
LSt4z+ISzc8TbXrZ+WMCQQCUGJf/zn6lzzru9jBWxjPzfUkUnWSh6dYlkruKzOJ8
G9SygLMEnE/C9GsYfpMnBp0NPf+Gk3a1IHIy/NhETlW1
-----END RSA PRIVATE KEY-----
```
Example output:

`a6w2bp7sz5wzvp52.onion`

## Installation
Firstly, install Python 3 and python3-pip. Then git clone this repo and `cd` to it:

`git clone https://github.com/qbitroot/rsa2onion && cd rsa2onion`

And install requiremenets from file:

`sudo pip3 install -r requirements.txt`

## How it works

1. Generate public key based on private key.
2. Convert it to DER format (for some reason I had to crop DER key to start from 22nd byte).
3. Calculate SHA-1 hash of that value (byte digest, not hex digest).
4. Crop to first half of hash.
5. Encode it to Base32.
6. Add .onion to end.
7. Done!

![Illustration](algorithm.png)

## TODO
Add support of V3 onion addresses (and check is it already done?).
