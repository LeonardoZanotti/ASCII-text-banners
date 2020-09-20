# ASCII-text-banners
How to create ASCII text banners in linux

## Requisites
You will use [figlet](http://www.figlet.org/) and/or toilet. You can install it with:
```bash
$ sudo apt install figlet toilet    [On Debian/Ubuntu]
$ sudo yum install figlet toilet    [On CentOS/RHEL]
$ sudo dnf install figlet toilet    [On Fedora 22+]
```

## Some examples
```bash
$ figlet Zanotti
 _____                 _   _   _ 
|__  /__ _ _ __   ___ | |_| |_(_)
  / // _` | '_ \ / _ \| __| __| |
 / /| (_| | | | | (_) | |_| |_| |
/____\__,_|_| |_|\___/ \__|\__|_|


$ toilet Zanotti

 mmmmmm                        m      m      "   
     #"  mmm   m mm    mmm   mm#mm  mm#mm  mmm   
   m#   "   #  #"  #  #" "#    #      #      #   
  m"    m"""#  #   #  #   #    #      #      #   
 ##mmmm "mm"#  #   #  "#m#"    "mm    "mm  mm#mm 

# Reading from a file
$ echo "I wish I could chmod 644 my Girlfriend" >girlfriend.txt
$ figlet -kp < girlfriend.txt
 ___             _       _       ___                      _      _ 
|_ _| __      __(_) ___ | |__   |_ _|   ___  ___   _   _ | |  __| |
 | |  \ \ /\ / /| |/ __|| '_ \   | |   / __|/ _ \ | | | || | / _` |
 | |   \ V  V / | |\__ \| | | |  | |  | (__| (_) || |_| || || (_| |
|___|   \_/\_/  |_||___/|_| |_| |___|  \___|\___/  \__,_||_| \__,_|
                                                                   
       _                            _    __    _  _    _  _   
  ___ | |__   _ __ ___    ___    __| |  / /_  | || |  | || |  
 / __|| '_ \ | '_ ` _ \  / _ \  / _` | | '_ \ | || |_ | || |_ 
| (__ | | | || | | | | || (_) || (_| | | (_) ||__   _||__   _|
 \___||_| |_||_| |_| |_| \___/  \__,_|  \___/    |_|     |_|  
                                                              
                     ____  _        _   __        _                   _  
 _ __ ___   _   _   / ___|(_) _ __ | | / _| _ __ (_)  ___  _ __    __| | 
| '_ ` _ \ | | | | | |  _ | || '__|| || |_ | '__|| | / _ \| '_ \  / _` | 
| | | | | || |_| | | |_| || || |   | ||  _|| |   | ||  __/| | | || (_| | 
|_| |_| |_| \__, |  \____||_||_|   |_||_|  |_|   |_| \___||_| |_| \__,_|


# Using different fonts (you will need to download the font inside the folder)
$ figlet -f slant "Sudo I Love You" #or
$ toilet -f script "Dale Dele"
   _____           __         ____   __                       __  __           
  / ___/__  ______/ /___     /  _/  / /   ____ _   _____      \ \/ /___  __  __
  \__ \/ / / / __  / __ \    / /   / /   / __ \ | / / _ \      \  / __ \/ / / /
 ___/ / /_/ / /_/ / /_/ /  _/ /   / /___/ /_/ / |/ /  __/      / / /_/ / /_/ / 
/____/\__,_/\__,_/\____/  /___/  /_____/\____/|___/\___/      /_/\____/\__,_/


For more options, see the manual of the tools:
$ man figlet
$ man toilet
```

## References
Thanks for Aaron Kili of TecMint for writing an [article](https://www.tecmint.com/create-ascii-text-banners-in-linux-terminal/) about this