from sys import argv

from qr_mark.qr_cli import QrCLI

if __name__ == '__main__':
    try:
        QrCLI.main(argv)
    # TODO: add custom exceptions
    except Exception as e:
        print("an error has occurred")
        print(e)
        exit(1)