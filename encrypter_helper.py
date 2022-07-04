# Standard packages
import pickle


# Pypi packages
from cryptography.fernet import Fernet


class LetsEncrypt:
    """Encrypter business logic
    """
    # encryping key
    _key: str = None

    def __init__(self):
        self._key = self._deserialize()

    # ***** parameter functions   *******
    def generate_key(self) -> None:
        self._key = self._generate_key()
        self._print_key()

    # persisting _key value into pickle file
    def serialize_key(self) -> None:
        if self._key:
            self._serialize(self._key)
            print(f"Key : {self._key}  serialized to encrypter.pickle file ")
        else:
            self._print_do_key_defined()

    # restoring _key value from pickle file
    def deserialize_key(self) -> None:
        self._key = self._deserialize()
        self._print_key()

    # key from parameter value to class property - no serializing to pickle
    def store_key(self, key: str) -> None:
        self._key = key

    # key from property
    def read_key(self):
        self._print_key()

    # encrypt string using key
    def encrypt(self, value_to_be_encryptred: str) -> None:
        if not self._key:
            self._print_do_key_defined()
            exit(1)
        try:
            encrypted_value = self._encrypt(value_to_be_encryptred, self._key)
            print(f"{value_to_be_encryptred} -> {encrypted_value}")
            self._print_key()
        except BaseException as error:
            print(f"Unexpected {error = }")

    # decrypt string using key
    def decrypt(self, encryptred_value: str) -> None:
        if not self._key:
            self._print_do_key_defined()
            exit(1)
        try:
            dencrypted_value = self._decrypt(encryptred_value, self._key)
            print(f"{encryptred_value} -> {dencrypted_value}")
            self._print_key()
        except BaseException as error:
            print(f"Unexpected {error = }")

    # ***** Helper functions ***************

    def _print_key(self) -> None:
        if self._key:
            print(f"Key : {self._key}")
        else:
            self._print_do_key_defined()

    def _print_do_key_defined(self) -> None:
        print("ERROR : No key defined")

    # key for encrypting/decrypting value
    def _generate_key(self) -> str:
        return self._bytes_to_string(Fernet.generate_key())

    def _string_to_bytes(self, st: str) -> bytes:
        return bytes(st, "ascii")

    def _bytes_to_string(self, b: bytes) -> str:
        return b.decode("ascii")

    # Encrypts string
    def _encrypt(self, to_be_encrypted: str, key: str) -> str:
        cipher_suite = Fernet(self._string_to_bytes(key))
        return self._bytes_to_string(
            cipher_suite.encrypt(self._string_to_bytes(to_be_encrypted))
        )

    # Decrypts string
    def _decrypt(self, encrypted: str, key: str) -> str:
        cipher_suite = Fernet(self._string_to_bytes(key))
        return self._bytes_to_string(
            cipher_suite.decrypt(self._string_to_bytes(encrypted))
        )

    def _serialize(self, key_to_be_saved: str) -> None:
        with open("encrypter.pickle", "wb") as handle:
            pickle.dump(key_to_be_saved, handle,
                        protocol=pickle.HIGHEST_PROTOCOL)

    def _deserialize(self) -> str:
        deserialized_key = None
        try:
            with open("encrypter.pickle", "rb") as handle:
                deserialized_key = pickle.load(handle)
        except:
            pass
        return deserialized_key
