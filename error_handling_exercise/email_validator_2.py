EMAIL_SYMBOL = '@'
domains = (".com", ".bg", ".org", ".net")


class NameTooShortError(Exception):
    """
    Raises:
        NameTooShortError: If address name less than 4 characters
    """
    def __init__(self):
        self.message = "Name must be more than 4 characters"

    def __str__(self):
        return self.message


class MustContainAtSymbolError(Exception):
    """
    Raises:
        MustContainAtSymbolError: If address not contains @
    """
    def __init__(self):
        self.message = "Email must contains @"

    def __str__(self):
        return self.message


class InvalidDomainError(Exception):
    """
    Raises:
        InvalidDomainError: Only the following domains are allowed: .com, .bg, .org, .net
    """
    def __init__(self):
        self.message = "Domain must be one of the following: .com, .bg, .org, .net"

    def __str__(self):
        return self.message


while True:
    user_input = input()
    if user_input == "End":
        break
    if EMAIL_SYMBOL in user_input[:5]:
        raise NameTooShortError
    if EMAIL_SYMBOL not in user_input:
        raise MustContainAtSymbolError
    for domain in domains:
        if domain in user_input:
            break
    else:
        raise InvalidDomainError
    print("Email is valid")
