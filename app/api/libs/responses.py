
def error_response(type, message):
    body = {
        'error': {
            'error_type': type,
            'error_message': message
            }
        }
    return body
