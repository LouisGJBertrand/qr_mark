from qr_mark.qr_settings import QrSettings
from qr_mark.qr_pipeline import QrPipeline

class QrCLI:
    @staticmethod
    def main(args):
        settings = QrSettings()
        try:
            settings = QrCLI.get_settings_from_cli_args(args)
        except Exception as e:
            print("an error has occurred")
            print(e)
            exit(1)

        pipeline = QrPipeline(settings)

        images = pipeline.generate_images()
        pipeline.save_images(images)


    @staticmethod
    def get_settings_from_cli_args(args):
        settings = QrSettings()

        i = 0
        for arg in args:
            if arg == "-o":
                if args[i+1].startswith("-"):
                    raise Exception("Invalid option -o, missing value")
                settings.output = args[i+1]
                i += 2
                continue
            if arg == "-c":
                if args[i+1].startswith("-"):
                    raise Exception("Invalid option -c, missing value")
                c = int(args[i+1])
                if c is None:
                    raise Exception("Invalid option -c, invalid value, must be int")
                settings.count = c
                i += 2
                continue
            if arg == "-s":
                if args[i+1].startswith("-"):
                    raise Exception("Invalid option -s, missing value")
                s = int(args[i+1])
                if s is None:
                    raise Exception("Invalid option -s, invalid value, must be int")
                settings.size = s
                i += 2
                continue
            if arg == "-x":
                if args[i+1].startswith("-"):
                    raise Exception("Invalid option -x, missing value")
                x = int(args[i+1])
                if x is None:
                    raise Exception("Invalid option -x, invalid value, must be int")
                settings.x = x
                i += 2
                continue
            if arg == "-y":
                if args[i+1].startswith("-"):
                    raise Exception("Invalid option -y, missing value")
                y = int(args[i+1])
                if y is None:
                    raise Exception("Invalid option -y, invalid value, must be int")
                settings.y = y
                i+=2
                continue
        return settings