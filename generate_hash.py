import bcrypt

HASHED = ''
if __name__ == "__main__":
    password = input("Create Admin Password: ")
    HASHED = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
