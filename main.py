try:
    from actions import importer
    from actions import launcher
except ImportError as err:
    importer("boot")

if __name__ == '__main__':
    launcher()
