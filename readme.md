<picture><source media="(prefers-color-scheme: dark)" srcset="https://www.shieldcn.dev/github/stars/LouisGJBertrand/qr_mark.svg?variant=secondary&amp;size=sm&amp;mode=dark"><img alt="GitHub Stars" src="https://www.shieldcn.dev/github/stars/LouisGJBertrand/qr_mark.svg?variant=secondary&amp;size=sm&amp;mode=light"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://www.shieldcn.dev/github/last-commit/LouisGJBertrand/qr_mark.svg?variant=secondary&amp;size=sm&amp;mode=dark"><img alt="Last commit" src="https://www.shieldcn.dev/github/last-commit/LouisGJBertrand/qr_mark.svg?variant=secondary&amp;size=sm&amp;mode=light"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://www.shieldcn.dev/github/open-issues/LouisGJBertrand/qr_mark.svg?variant=secondary&amp;size=sm&amp;mode=dark"><img alt="Open issues" src="https://www.shieldcn.dev/github/open-issues/LouisGJBertrand/qr_mark.svg?variant=secondary&amp;size=sm&amp;mode=light"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="https://www.shieldcn.dev/github/ci/LouisGJBertrand/qr_mark.svg?variant=secondary&amp;size=sm&amp;mode=dark"><img alt="CI" src="https://www.shieldcn.dev/github/ci/LouisGJBertrand/qr_mark.svg?variant=secondary&amp;size=sm&amp;mode=light"></picture>

# QR Mark

A simple CLI tool to generate customized random markings useful for 3D scans of interior environments.

## Requirements
production:
```
Pillow==13.0.0
```

dev:
```
Pillow==13.0.0
flake8
pytest
```

## Installation
```bash
git clone https://github.com/LouisGJBertrand/qr_mark.git
cd qr_mark
pip install -r requirements.txt
```
recommended: setup venv
```bash
python -m venv venv
```

## Usage

```bash
# default settings:
# - formatted output in "./out/mark_%03d.png"
# - size is 25 (5x5px)
# - count is 8

# available params:
# -o <string> formatted output path
# -c <int> output count
# -s <int> size interpreted as square by default
# -x <int> size X override
# -y <int> size Y override
# note: if -x is present but not -y, y will be calculated (same reversed). if x and y are present, s is omitted.

# generate with default settings (8 markings of size 5x5)
py ./main.py
# equivalent to
py ./main.py -c 8 -o "./out/%03d.png" -s 25

# generates a marking in "./out" formated with 5 floating 0 as pngs of size 8*8 (sqrt(32))
py ./main.py -c 1 -o "./out/%05d.png" -s 32

# generates 4 markings of size 16x32px
py ./main.py -c 4 -x 16 -y 32
```