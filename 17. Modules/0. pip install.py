#pip install email-validator
#can be installed from pycharm also file -> settings -> project -> python interpreter



from email_validator import validate_email, EmailNotValidError

print(validate_email("ines.iv.ivanova@gmail.com"))