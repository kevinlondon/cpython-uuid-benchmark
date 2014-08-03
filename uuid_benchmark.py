import uuid
import time
import sys
from binascii import unhexlify


N = int(sys.argv[1])


class UpdatedUUID(uuid.UUID):
    @property
    def bytes(self):
        return unhexlify(self.hex)  


def benchmark(uuid_object):
    t = time.time()
    for x in xrange(N):
        uuid_object.bytes

    print('%.3f microseconds' % ((time.time() - t) * 1000000.0 / N))


original_uuid = uuid.uuid4()
updated_uuid = UpdatedUUID(hex=original_uuid.hex)
benchmark(original_uuid)
benchmark(updated_uuid)
