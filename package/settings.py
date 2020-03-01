import os
from dotenv import load_dotenv

env_path = '../.env'
load_dotenv(dotenv_path=env_path)

# OR, the same with increased verbosity
load_dotenv(verbose=True)
DEBUG = os.getenv("DEBUG")
