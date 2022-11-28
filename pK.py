import functions as f
import grabAbi as grab
from dotenv import load_dotenv
import os
from web3 import Web3

load_dotenv()
p = os.environ.get("privateKey") 
