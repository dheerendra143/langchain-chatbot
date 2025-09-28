from langchain_ollama.src.modules.users.services.create_user import create_users_service


def create_users_ctrl(user_payload):
    response = create_users_service(user_payload)
    return response


