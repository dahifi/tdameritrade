from .Utils import *


class Token:
    def __init__(self, access_token, refresh_token, token_type, expires_in, scope, refresh_token_expires_in):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.scope = scope
        self.refresh_token_expires_in = refresh_token_expires_in

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        access_token = from_str(obj.get("access_token"))
        refresh_token = from_str(obj.get("refresh_token"))
        token_type = from_str(obj.get("token_type"))
        expires_in = from_int(obj.get("expires_in"))
        scope = from_str(obj.get("scope"))
        refresh_token_expires_in = from_int(obj.get("refresh_token_expires_in"))
        return Token(access_token, refresh_token, token_type, expires_in, scope, refresh_token_expires_in)

    def to_dict(self):
        result = {}
        result["access_token"] = from_str(self.access_token)
        result["refresh_token"] = from_str(self.refresh_token)
        result["token_type"] = from_str(self.token_type)
        result["expires_in"] = from_int(self.expires_in)
        result["scope"] = from_str(self.scope)
        result["refresh_token_expires_in"] = from_int(self.refresh_token_expires_in)
        return result


def token_from_dict(s):
    return Token.from_dict(s)


def token_to_dict(x):
    return to_class(Token, x)