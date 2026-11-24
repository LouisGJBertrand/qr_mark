from qr_mark.qr_settings import QrSettings
from qr_mark.qr_pipeline import QrPipeline

class QrCLI:
    @staticmethod
    def main(args):
        settings = QrCLI.get_settings_from_cli_args(args)

        pipeline = QrPipeline(settings)

        images = pipeline.generate_images()
        pipeline.save_images(images)


    @staticmethod
    def get_settings_from_cli_args(args):
        settings = QrSettings()

        i = 0
        for arg in args:
            if arg == "-o":
                if len(args) <= i+1:
                    raise Exception("Invalid option -o, no value")
                if args[i+1].startswith("-"):
                    raise Exception("Invalid option -o, missing value")
                settings.output = args[i+1]
                i += 1
                continue
            if arg == "-c":
                if len(args) <= i+1:
                    raise Exception("Invalid option -c, no value")
                if args[i+1].startswith("-"):
                    raise Exception("Invalid option -c, missing value")
                c = int(args[i+1])
                if c is None:
                    raise Exception("Invalid option -c, invalid value, must be int")
                settings.count = c
                i += 1
                continue
            if arg == "-s":
                if len(args) <= i+1:
                    raise Exception("Invalid option -s, no value")
                if args[i+1].startswith("-"):
                    raise Exception("Invalid option -s, missing value")
                s = int(args[i+1])
                if s is None:
                    raise Exception("Invalid option -s, invalid value, must be int")
                settings.size = s
                i += 1
                continue
            if arg == "-x":
                if len(args) <= i+1:
                    raise Exception("Invalid option -x, no value")
                if args[i+1].startswith("-"):
                    raise Exception("Invalid option -x, missing value")
                x = int(args[i+1])
                if x is None:
                    raise Exception("Invalid option -x, invalid value, must be int")
                settings.x = x
                i += 1
                continue
            if arg == "-y":
                if len(args) <= i+1:
                    raise Exception("Invalid option -y, no value")
                if args[i+1].startswith("-"):
                    raise Exception("Invalid option -y, missing value")
                y = int(args[i+1])
                if y is None:
                    raise Exception("Invalid option -y, invalid value, must be int")
                settings.y = y
                i+=1
                continue
            i += 1
        return settings