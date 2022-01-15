#  Bitcoin Address  v0.1
#  Copyright (c) 2020 - https://github.com/fortesp/bitcoinaddress
#  This software is distributed under the terms of the MIT License.
#  See the file 'LICENSE' in the root directory of the present distribution,
#  or http://opensource.org/licenses/MIT.
import time

import quantumrandom

from bitcoinaddress import Address, Seed
from bitcoinaddress.key.key import Key


class Wallet:
    def __init__(self, hash_or_seed=None, testnet=False, entropy_seed=None):
        if hash_or_seed is None: hash_or_seed = Seed(entropy_seed=entropy_seed)
        self.key = Key.of(hash_or_seed)
        self.address = Address.of(self.key)
        self.testnet = testnet

    def __str__(self):
        return """%s\n%s""" % (self.key.__str__(self.testnet),
                               self.address.__str__(self.testnet))



