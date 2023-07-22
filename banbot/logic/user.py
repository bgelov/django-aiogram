from banbot.models import User

def add_user(chat_id, first_name, last_name, username):
    user = User.objects.update_or_create(
        chat_id=chat_id,
        first_name=first_name,
        last_name=last_name,
        username=username,
    )
    user.save()
    return True
