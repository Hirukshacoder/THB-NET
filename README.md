
![thb net (2)](https://user-images.githubusercontent.com/97717488/211159703-1b64d0fd-3449-4def-afbe-f820eb31b25d.png)

# THB - NET

* An app to chat, create new servers, learn databases, enjoy!

![](https://img.shields.io/badge/TryHackMe-THB-212C42?style=for_the_badge&logo=thb)
![](https://img.shields.io/pypi/l/hashlib?color=yellow&logo=python)
![python](https://img.shields.io/badge/Python-v3.10-3776AB?style=for_the_badge&logo=Python)
![sqlite](https://img.shields.io/badge/Sqlite-v3-003B57?style=for_the_badge&logo=Sqlite)


## Installation

Install THB-NET with git

```bash
$ git clone https://github.com/Hirukshacoder/THB-NET
$ cd THB-NET
$ pip install -r requirements.txt
$ python3 client.py
```
# Documentation

## ~ client.py ~

* Signup - creates `database_mine.db`
* Login
* Create new servers
* Join to existing servers
* Performs most of the part of the app here 

## ~ database_mine.db ~

* A sqlite database 
* Saved passwords and usernames safely

#### Login and signup database (database_mine.db)


| id        | username | password                |
| :-------- | :------- | :-----------------------|
| 1         | John     | hashed password (sha256)|
| 2         | Beckham  | hashed password (sha256)|
| 3         | Ann      | hashed password (sha256)|

## Ngrok - configuration

* Ngrok is a bit buggy on `client_v1-0.py`

* It works only on `client_v1-1.py`

### Config ngrok

* Install [ngrok](https://ngrok.com/)

* Go to the extracted ngrok directory and save your auth token.

* Run `./ngrok tcp 9999` in the terminal.

* Run `python3 client.py`

* Type the new `ip` and `port` from ngrok tcp connection to the `client.py`.

```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("0.tcp.in.ngrok.io", 11441))
```


## Contact us

- [📱Telegram](https://t.me/+wrtEUZA9_j8yMjM9)

- [💽 Discord](https://discord.gg/H6P5VEn2)

## Authors

- [@Treveen](https://github.com/Hirukshacoder)

<a href="https://www.buymeacoffee.com/thborg"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=thborg&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>

# Thank you!
