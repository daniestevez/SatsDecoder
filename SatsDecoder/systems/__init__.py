#  Copyright (c) 2024. Alexander Baskikh
#
#  MIT License (MIT), http://opensource.org/licenses/MIT
#  Full license can be found in the LICENSE-MIT file
#
#  SPDX-License-Identifier: MIT

import sys

from SatsDecoder.systems.ax25 import *
from SatsDecoder.systems.csp import *
from SatsDecoder.systems.geoscan import *
from SatsDecoder.systems.greencube import *
from SatsDecoder.systems.lucky7 import *
from SatsDecoder.systems.roseycubesat import *
from SatsDecoder.systems.sharjahsat import *
from SatsDecoder.systems.sonate2 import *
# from SatsDecoder.systems.starlink_vhf import *
from SatsDecoder.systems.usp import *
from SatsDecoder.systems.wtc_simba import *
from SatsDecoder.systems.raw import *

PROTOCOLS = {}
for i in (
        'geoscan',
        'greencube',
        'usp',
        'ax25',
        'csp',
        'lucky7',
        'roseycubesat',
        'sharjahsat',
        'sonate2',
        # 'starlink_vhf',
        'wtc_simba',
        'raw',
        ):
    m = getattr(sys.modules['SatsDecoder.systems'], i)
    for n in dir(m):
        if n.endswith('Protocol'):
            PROTOCOLS[m.proto_name] = getattr(m, n)
            break
