from utils.myllm import getLLM
from utils.user_interface import message

myLLM = getLLM()

print("hello, users")

ai_mssg = myLLM.invoke(message)
print(ai_mssg)
