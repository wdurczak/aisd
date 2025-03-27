import random
from enum import Enum

class DataType(Enum):
    RANDOM = "losowe"
    ASCENDING = "rosnące"
    DESCENDING = "malejące"
    CONSTANT = "stałe"
    A_SHAPED = "a-kształtne"

def generate_data(n, data_type: DataType):
    if data_type== DataType.RANDOM:
        return [random.randint(0, 1000) for _ in range(n)]
    elif data_type ==DataType.ASCENDING:
        return list(range(n))
    elif data_type == DataType.DESCENDING:
        return list(range(n, 0, -1))
    elif data_type ==DataType.CONSTANT:
        return [100] * n
    elif data_type ==DataType.A_SHAPED:
        half = n// 2
        return list(range(1, half + 2)) + list(range(half, 0, -1))
