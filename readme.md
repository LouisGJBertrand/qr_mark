# QR Mark

A simple CLI tool to generate customized random markings useful for 3D scans of interior environments.

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