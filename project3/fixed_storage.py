import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=13)
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")

def verify_password(password: str, stored_hash: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))
    except Exception:
        return False

print(hash_password("samepassword"))
print(hash_password("samepassword"))