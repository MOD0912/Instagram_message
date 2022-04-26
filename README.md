# Instagram message
This project is about automating sending messages on Instagram.



## Installation(Windows)

1.  open up a terminal and copy paste this in:
 ```
 pip install selenium
 ```
2.  Download driver:
    * Chrome = Chromedriver: https://chromedriver.storage.googleapis.com/index.html?path=94.0.4606.41/
    * Firefox = Geckodriver:  https://github.com/mozilla/geckodriver/releases
    * Only for Chrome users: You need to replace every "Firefox" with "Chrome"(in vsc press ctrl+h) in the code

3.  Add driver to "PATH":
    * Add driver to the enviroment variable "PATH": https://www.youtube.com/watch?v=gb9e3m98avk

4.  specific time:
    * To use a specific time delete line 11 and 12
    * Make sure the program is always running
    * If you use "am" and "pm" you need to find out how to change that


## Error
In case your program starts perfectly fine, but stops on any point:
           - Add more time in time.sleep()
           - Try restarting the program
           - restart your Editor/IDE
           - If it still doesn't work write me


## Hint
Don't use the module Instabot. It does the same as my program, but it contains a virus!!!
## On what does it run?
I tested it for Windows 10 with Python 10.0 and Firefox. I'm pretty sure it does also work with chrome, but I'm not sure if it works for Linux. 
