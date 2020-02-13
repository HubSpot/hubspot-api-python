import time
from flask import session


def save_tokens(tokens_response):
    tokens = {
        'access_token': tokens_response.access_token,
        'refresh_token': tokens_response.refresh_token,
        'expires_in': tokens_response.expires_in,
        'expires_at': time.time() + tokens_response.expires_in * 0.95
    }
    session['tokens'] = tokens

    return tokens
