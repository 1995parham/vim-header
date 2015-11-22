# vim-header
## Introduction
Simple header generator for vim based on python script.
## VIM Configuration
In order to use copyrighter vim plugin with
[Plug plugin manager](https://github.com/junegunn/vim-plug)
add following comamnd in your vim configuration (vimrc):
```viml
Plug '1995parham/vim-header', {'do': '~/.vim/plugged/vim-header/init.sh'}
```
You must set your name and your email in your vim configuration (vimrc)
for vim-header plugin as follows:
```viml
g:header_user = "Your Name"
g:header_email = "youremail@mail.com"
```
## Header Template Configuration
You can create new header template for your language
or modify existing ones. Our header template write with
Velocity Template Language (VTL). see
[here](http://velocity.apache.org/engine/devel/user-guide.html)
for more details. Following table shows variables you have in
VTL header.

| Variable      | Description     |
|:-------------:|:---------------:|
| `$user`       | User details    |
| `$time`       | Datetime object |
| `$file`       | Target file data|

for header template sample see *copyrighter/conf/header*

## Dependencies
You must have **python3** installed on your machine ....

## Contribution
if you have time ... nothing else just time :) you can do what
you want with this dummy project :)
