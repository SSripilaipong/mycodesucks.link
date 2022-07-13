from lambler.http import HttpApi

handler = HttpApi()


@handler.get("")
def homepage():
    pass
