#  Bitcoin Address  v0.1
#  Copyright (c) 2020 - https://github.com/fortesp/bitcoinaddress
#  This software is distributed under the terms of the MIT License.
#  See the file 'LICENSE' in the root directory of the present distribution,
#  or http://opensource.org/licenses/MIT.

import os
import time
from random import randrange


class Seed:

    def __init__(self, entropy=None, entropy_seed=None):
        # print('Внутри сида', entropy_seed)
        self.entropy_seed = entropy_seed
        self.entropy = entropy
        if self.entropy is None:
            self.generate()

    def generate(self):
        self.entropy = self.random()

    @staticmethod
    def of(entropy=None):
        return Seed(entropy)

    def random(self):
        # from bitcoin project
        if self.entropy_seed:
            return str(os.urandom(32).hex()) + str(randrange(2 ** 256)) + str(int(time.time() * 1000000))
        else:
            return str(os.urandom(32).hex()) + str(randrange(2 ** 256)) + str(int(time.time() * 1000000))

    def __str__(self):
        return self.entropy
