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
                settings.output = QrCLI.parse_output_args(args, i)
                i += 1
                continue
            if arg == "-c":
                settings.count = QrCLI.parse_count_args(args, i)
                i += 1
                continue
            if arg == "-s":
                settings.size = QrCLI.parse_size_args(args, i)
                i += 1
                continue
            if arg == "-x":
                settings.x = QrCLI.parse_x_args(args, i)
                i += 1
                continue
            if arg == "-y":
                settings.y = QrCLI.parse_y_args(args, i)
                i += 1
                continue
            i += 1
        return settings

    @staticmethod
    def parse_output_args(args, i):
        if len(args) <= i+1:
            raise Exception("Invalid option -o, no value")
        if args[i+1].startswith("-"):
            raise Exception("Invalid option -o, missing value")
        return args[i+1]

    @staticmethod
    def parse_count_args(args, i):
        if len(args) <= i+1:
            raise Exception("Invalid option -c, no value")
        if args[i+1].startswith("-"):
            raise Exception("Invalid option -c, missing value")
        c = int(args[i+1])
        if c is None:
            raise Exception("Invalid option -c, invalid value, must be int")
        return c

    @staticmethod
    def parse_size_args(args, i):
        if len(args) <= i+1:
            raise Exception("Invalid option -s, no value")
        if args[i+1].startswith("-"):
            raise Exception("Invalid option -s, missing value")
        s = int(args[i+1])
        if s is None:
            raise Exception("Invalid option -s, invalid value, must be int")
        return s

    @staticmethod
    def parse_x_args(args, i):
        if len(args) <= i+1:
            raise Exception("Invalid option -x, no value")
        if args[i+1].startswith("-"):
            raise Exception("Invalid option -x, missing value")
        x = int(args[i+1])
        if x is None:
            raise Exception("Invalid option -x, invalid value, must be int")
        return x

    @staticmethod
    def parse_y_args(args, i):
        if len(args) <= i + 1:
            raise Exception("Invalid option -y, no value")
        if args[i + 1].startswith("-"):
            raise Exception("Invalid option -y, missing value")
        y = int(args[i + 1])
        if y is None:
            raise Exception("Invalid option -y, invalid value, must be int")
        return y
