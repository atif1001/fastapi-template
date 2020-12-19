import click
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = click.prompt('Please enter password to hash', type=str)
print(f'Your password hash is: {pwd_context.hash(password)}')
