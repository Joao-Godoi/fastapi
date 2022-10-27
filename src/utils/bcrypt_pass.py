from passlib.context import CryptContext


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def bcrypt_password(password):
    return password_context.hash(password)
