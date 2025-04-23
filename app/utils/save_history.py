import json


def save_chat_history(
    chat_history, user_id: str, conversation_id: str, path="chat_store.json"
):
    try:
        with open(path, encoding="utf-8") as f:
            store = json.load(f)
    except FileNotFoundError:
        store = {}

    if user_id not in store:
        store[user_id] = {}
    store[user_id][conversation_id] = [list(item) for item in chat_history]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False, indent=2)


def load_chat_history(user_id: str, conversation_id: str, path="chat_store.json"):
    try:
        with open(path, encoding="utf-8") as f:
            store = json.load(f)
        if user_id in store and conversation_id in store[user_id]:
            return [tuple(item) for item in store[user_id][conversation_id]]
    except FileNotFoundError:
        pass
    return []
