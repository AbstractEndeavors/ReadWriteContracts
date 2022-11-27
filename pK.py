import functions as f
from dotenv import load_dotenv
import os
def getKey(x):
	load_dotenv()
	if f.exists(x) == False:
		f.pen('privateKey = '+str(input('please enter your private key')),x+'.env')
	load_dotenv(str(f.reader(x+'.env')))
	return os.environ.get("privateKey")

