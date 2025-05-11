#download external ibraries
install bs4
!pip install requests
!pip install python-dotenv
!pip install --upgrade openai



# import libraries
import os
import openai
import requests
from bs4 import BeautifulSoup
import IPython.display
from dotenv import load_dotenv


# set up the API key
load_dotenv()
api_key=os.getenv('OPENAI_API_KEY')
if not api_key:
    print('that is not the API key or there is no API key')
# sending a sample request
# turning api key into an openai key
openai.api_key = api_key
# asking user input
message=input('enter a website to analyze:')
# using try function for troubleshoot
try:
    #send request to openai
    response=openai.ChatCompletion.create(
    model="gpt-4o-mini", 
    messages = [{'role':'user','content': message}])
# print response
    print(response.choices[0].message.content)
except openai.error.OpenAIError as e:
    print(f"OpenAI API Error: {e}")

except Exception as e:
    print("Unexpected Error: {e}")
    