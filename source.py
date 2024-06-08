import json
from ibm_watson import AssistantV2, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from const import VERSION, API_KEY, ASSISTANT_URL, ASSISTANT_INSTANCE_URL, ASSISTANT_ID, LIVE_ENVIRONMENT_ID

authenticator = IAMAuthenticator(API_KEY)

assistant = AssistantV2(
    version=VERSION,
    authenticator=authenticator,
    service_name="Demo Bot"
)

assistant.set_service_url(ASSISTANT_URL)

response = assistant.create_session(
    assistant_id=LIVE_ENVIRONMENT_ID
).get_result()

session_id = response["session_id"]

print(f"Assistant is ready for chatting: {session_id=}. Enter your first message.")

while True:
    try:
        msg = input("U: ")
    except KeyboardInterrupt:
        break

    response = assistant.message(
        assistant_id=LIVE_ENVIRONMENT_ID,
        session_id=session_id,
        input={
            'message_type': 'text',
            'text': msg
        }
    ).get_result()

    print(f"A: {response['output']['generic'][0]['text']}")
    # print(json.dumps(response, indent=2))
