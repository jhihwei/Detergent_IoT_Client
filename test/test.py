from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='../test/.env')
print(str(os.getenv('CLIENT_ID')))