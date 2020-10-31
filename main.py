try:
    from actions import msg
    from actions import launcher
except ImportError as err:
    print(msg["boot"])
    exit(1)

if __name__ == '__main__':
    launcher()
