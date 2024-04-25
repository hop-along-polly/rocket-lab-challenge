import os
from dotenv import load_dotenv

__config = None

# Env Vars should overwrite values in .env which should overwrite defaults
class Config:

  def __init__(self, **kwargs):
    self._mongodb_user = kwargs.get('MONGODB_USER', 'rocket-lab')
    self._mongodb_password = kwargs.get('MONGODB_PASSWORD', 'rocket-lab-pw')
    self._mongodb_host = kwargs.get('MONGODB_HOST', 'localhost')
    self._mongodb_port = kwargs.get('MONGODB_PORT', '27017')

  @property
  def mongodb_uri(self):
    user = self._mongodb_user
    password = self._mongodb_password
    host = self._mongodb_host
    port = self._mongodb_port
    uri = f'mongodb://{user}:{password}@{host}:{port}/rocket-lab?authSource=admin'
    return uri


def get_config():
  global __config
  if not __config:
    load_dotenv() # Doesn't overwrite existing env vars
    __config = Config(**os.environ)

  return __config
