```bash
         ▄▄▄▄▄▄▄▄            ▄▄                                     
         ▀▀▀▀▀███            ██                                     
             ██▀    ▄█████▄  ██▄███▄    ▄█████▄   ▄███▄██   ▄████▄  
           ▄██▀     ▀ ▄▄▄██  ██▀  ▀██   ▀ ▄▄▄██  ██▀  ▀██  ██▄▄▄▄██ 
          ▄██      ▄██▀▀▀██  ██    ██  ▄██▀▀▀██  ██    ██  ██▀▀▀▀▀▀ 
         ███▄▄▄▄▄  ██▄▄▄███  ███▄▄██▀  ██▄▄▄███  ▀██▄▄███  ▀██▄▄▄▄█ 
         ▀▀▀▀▀▀▀▀   ▀▀▀▀ ▀▀  ▀▀ ▀▀▀     ▀▀▀▀ ▀▀   ▄▀▀▀ ██    ▀▀▀▀▀  
                                                  ▀████▀▀           
                                                               
```

# ASCII-text-banners
Zanotti banners generator - create ASCII text banners in linux terminal.

## Samples
```
 _ _ _          _   _     _     
| (_) | _____  | |_| |__ (_)___ 
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
                                

                          .   oooo         o8o           
                        .o8   `888         `"'           
 .ooooo.  oooo d8b    .o888oo  888 .oo.   oooo   .oooo.o 
d88' `88b `888""8P      888    888P"Y88b  `888  d88(  "8 
888   888  888          888    888   888   888  `"Y88b.  
888   888  888          888 .  888   888   888  o.  )88b 
`Y8bod8P' d888b         "888" o888o o888o o888o 8""888P' 
                                                         
                                                             
                             _/      _/        _/            
    _/_/    _/  _/_/      _/_/_/_/  _/_/_/          _/_/_/   
 _/    _/  _/_/            _/      _/    _/  _/  _/_/        
_/    _/  _/              _/      _/    _/  _/      _/_/     
 _/_/    _/                _/_/  _/    _/  _/  _/_/_/        
                                                             
                                                             

or this:

     #           #              #             #
##########      #######    ##########    ##########
    #    #     #     #         #    #         #
    #    #    # #   #          #    #         #
   #     #       ###          #     #        #
  #   # #       ##           #   # #        #
 #     #      ##            #     #       ##

               _     _   _                                     
           ___(_) __| |_| |   __ _ _____   _____    __ _  ___  
          |__ \ |/ _` |__ |  / _` / _ \ \ / / _ \  |__` |/ _ \ 
 _ _ _ _  / __/ | | | |_| | | | | \__  \ V /\__  |    | | (_) |
(_|_|_|_) \___|_|_| |_|__/  |_| |_|___/ \_/ |___/     |_|\___/ 
                                                               
```

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

## LeonardoZanotti