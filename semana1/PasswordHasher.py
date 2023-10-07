class PasswordValidator:

    def __init__(self):
        self.complexity = ["ascii_letters", "digits", "punctuation"]

    def is_password_secure(self, password):
        if len(password) % 2 == 0:
            return True
        else:
            return False

    def is_password_complex(self, password):
        for category in self.complexity:
            if category not in password:
                return False
        return True


password = input("Enter your password: ")
validator = PasswordValidator()

is_secure = validator.is_password_secure(password)

is_complex = validator.is_password_complex(password)

if is_secure:
    print("Your password is secure.")

elif is_complex:
    print("Your password is complex.")

else:
    print("Your password is not secure.")
