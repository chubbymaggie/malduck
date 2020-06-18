# Copyright (C) 2018 Jurriaan Bremer.
# This file is part of Roach - https://github.com/jbremer/roach.
# See the file 'docs/LICENSE.txt' for copying permission.

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class DES3(object):
    modes = {
        "cbc": lambda iv: modes.CBC(iv),
    }

    def __init__(self, key, iv=None, mode="cbc"):
        self.des3 = Cipher(
            algorithms.TripleDES(key), self.modes[mode](iv),
            backend=default_backend()
        )

    def decrypt(self, data):
        decryptor = self.des3.decryptor()
        return decryptor.update(data) + decryptor.finalize()

    def encrypt(self, data):
        encryptor = self.des3.encryptor()
        return encryptor.update(data) + encryptor.finalize()
