import uuid


def send_email_token(email):
    try:
        # Generate a UUID token
        email_token = str(uuid.uuid4())

        subject = 'Your account needs to be verified'
        message = f'Click on the link to verify http://127.0.0.1:8000/verify/{email_token}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        return False
        
    return True
