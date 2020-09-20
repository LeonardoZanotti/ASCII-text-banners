# ASCII-text-banners
Zanotti banners generator - create ASCII text banners in linux terminal.

## Requisites
It's necessary to have [python 3.7](https://www.python.org/downloads/) and
you will use [figlet](http://www.figlet.org/) and toilet. You can install it with:
```bash
$ sudo apt install figlet toilet    [On Debian/Ubuntu]
$ sudo yum install figlet toilet    [On CentOS/RHEL]
$ sudo dnf install figlet toilet    [On Fedora 22+]
```

## How to use
Zabage reads a string an then make some custom banners with different fonts and formats. You can use it with:
```bash
$ python3 zabage.py your text comes here
```
If you want more fonts than this project use, you can go to `/usr/share/figlet` and add new fonts (i think .flf and .tlf formats only).

For more options, see the manual of the tools:
```bash
$ man figlet
$ man toilet
```

## References
Thanks for Aaron Kili of TecMint for writing an [article](https://www.tecmint.com/create-ascii-text-banners-in-linux-terminal/) about this.