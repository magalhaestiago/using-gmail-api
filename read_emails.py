from simplegmail import Gmail
from simplegmail.query import construct_query

gmail = Gmail()

query_params = {
    "newer_than": (3, "day")
}

messages = gmail.get_messages(query=construct_query(query_params))

for message in messages:
    print("To: " + message.recipient)
    print("From: "+message.sender)
    print("Subject: " +message.subject)
    print("Date: " + message.date)
    print("Preview: "+ message.snippet)

    # print("Message body: " + message.plain)