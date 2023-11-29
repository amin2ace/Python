import hashlib


class GetHash:
    def __init__(self, *data) -> None:
        self.data = data

    @staticmethod
    def get_hash_MD5(*data) -> tuple:
        data_list: list = [hashlib.md5(cell.encode()).hexdigest() for cell in data]
        return tuple(data_list)

    @staticmethod
    def get_hash_256(*data) -> tuple:
        data_list: list = [hashlib.sha256(cell.encode()).hexdigest() for cell in data]
        return tuple(data_list)

    @staticmethod
    def get_hash_512(*data) -> tuple:
        data_list: list = [hashlib.sha512(cell.encode()).hexdigest() for cell in data]
        return tuple(data_list)
