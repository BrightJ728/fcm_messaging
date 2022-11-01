import firebase_admin

from firebase_admin import credentials, messaging
cred = credentials.Certificate('service-account.json')
firebase_admin.initialize_app(cred)

def sendPush(registration_token):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title="Hello",
            body="bright Message"
        ),
        data=None,
        tokens=[registration_token],
    )

    response = messaging.send_multicast(message)
    # Response is a message ID string.
    return response

def subscribe_topic(token:str,topic:str):
    # These registration tokens come from the client FCM SDKs.
    registration_tokens = token    
    response = messaging.subscribe_to_topic(registration_tokens, topic)
    return response 

def unsubscribe_topic(token:str,topic:str):
    # These registration tokens come from the client FCM SDKs.
    registration_tokens = [token]
    response = messaging.unsubscribe_from_topic(registration_tokens, topic)
    return response 

def  send_messages_single_devices( registration_token:str):
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token=registration_token,
    )
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)

def send_messages_multiple_devices(registration_tokens:list):
    # Create a list containing up to 500 registration tokens.
# These registration tokens come from the client FCM SDKs.


    message = messaging.MulticastMessage(
        data={'score': '850', 'time': '2:45'},
        tokens=registration_tokens,
    )
    response = messaging.send_multicast(message)

    print('{0} messages were sent successfully'.format(response.success_count))

def send_batch_of_messages(messages:list,registration_token:list):
    # Create a list containing up to 500 messages.
    messages = [
        messaging.Message(
            notification=messaging.Notification('Price drop', '5% off all electronics'),
            token=registration_token,
        ),
        # ...
        messaging.Message(
            notification=messaging.Notification('Price drop', '2% off all books'),
            topic='readers-club',
        ),
    ]

    response = messaging.send_all(messages)
    # See the BatchResponse reference documentation
    # for the contents of response.
    print('{0} messages were sent successfully'.format(response.success_count))


def send_topic():
    topic = 'news'
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        topic=topic,
    )

    # Send a message to the devices subscribed to the provided topic.
    response = messaging.send(message)
    # Response is a message ID string.
    
    print('Successfully sent message:', response)
    return response

