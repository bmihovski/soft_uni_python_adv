class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name: str):
        return len(name) >= self.min_length

    def __validate_mail(self, mail: str):
        return mail in self.mails

    def __validate_domain(self, domain: str):
        return domain in self.domains

    def validate(self, email: str):
        email_name, mail_and_domain = email.split("@")
        email_mail, email_domain = mail_and_domain.split(".")
        return self.__validate_name(email_name) and self.__validate_mail(email_mail) \
               and self.__validate_domain(email_domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator: EmailValidator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
