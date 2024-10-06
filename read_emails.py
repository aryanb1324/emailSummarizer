# import your json with your google api key into your project
# rename the file to "client_secret.json"

#import gmail (have to pip install simple_gmail)
from simple_gmail import Gmail
# puts a filter on the emails
from simplegmail.query import construct_query

# add OpenAI import
import openai

# initialize OpenAI API
openai.api_key = 'your-openai-api-key-here'

# call it
gmail = Gmail()
# in terminal, run:
# python read_emails.py

# google should open and ask for permission


# get query params
query_params = {
    "newer_than": (2, "year"),
    "unread": True,
}

messages = gmail.get_sent_messages(query=construct_query(query_params))

# function to summarize text using OpenAI
def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes emails."},
            {"role": "user", "content": f"Please summarize the following email:\n\n{text}"}
        ]
    )
    return response.choices[0].message['content']

# modified loop to include summarization
for message in messages:
    print(f"Subject: {message.subject}")
    print(f"Sender: {message.sender}")
    print(f"Date: {message.date}")
    print(f"Snippet: {message.snippet}")
    
    # Summarize the email body
    summary = summarize_text(message.plain_body)
    print(f"Summary: {summary}")
    print("-" * 50)

#now run this same file again
