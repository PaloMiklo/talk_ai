import requests
from model.mistral import url, headers as heads, read_response, prepare_payload, ChatResponse

def send_message(msg: str) -> str:
    payload = prepare_payload(msg)
    response = requests.post(url, json=payload, headers=heads)
    if response.status_code == 200:
        chat_response = ChatResponse(**response.json())
        return read_response(chat_response)
    else:
        return "Request failed with status code: {}".format(response.status_code)