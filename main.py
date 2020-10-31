from core import app
from middleware import handler


if __name__ == '__main__':
    app.run(handler())
    app.run()
    pass
