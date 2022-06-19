import hashlib

class HashHandler:

    def __init__(self):
        self.hmac_hash_digest_algorithm = 'sha256'
        self.hmac_hash_iterations = 100000
        self.key_length = 128

    def hash_password_to_hex_string(self, password: str):

        hashed_password = hashlib.pbkdf2_hmac(
            hash_name=self.hmac_hash_digest_algorithm,  # The hash digest algorithm for HMAC
            password=password.encode('utf-8'),  # Convert the password to bytes
            salt="salt".encode('utf-8'),  # Convert the password to bytes
            iterations=self.hmac_hash_iterations,  # It is recommended to use at least 100,000 iterations of SHA-256
            dklen=self.key_length  # Get a 128 byte key
        )

        encoded_password = hashed_password.hex()

        return encoded_password