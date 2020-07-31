# vim-header

## Introduction
Advance-Dummy source codes header generator based on neovim python client.

## NeoVIM Configuration
In order to use vim-header plugin with
[Plug plugin manager](https://github.com/junegunn/vim-plug),
add following comamnd in your neovim configuration (init.vim):

```viml
Plug '1995parham/vim-header', {'do': ':UpdateRemotePlugins'}
```

You must set your name and your email in your vim configuration (init.vim)
for vim-header plugin as follow:

```viml
g:header_name = "Your Name"
g:header_email = "youremail@mail.com"
```

## Header Template Configuration
You can create new header template for your custom language
or modify existing ones. template language is based on [python
format](https://docs.python.org/3/library/string.html#formatspec).

Following table shows variables you have in
header template.

| Variable     | Description     |
|:------------:|:---------------:|
| `*` `-` `=`  | Symbols         |
| `user`       | User details    |
| `time`       | Datetime object |
| `file`       | Target filename |

for header template samples see [conf/header](conf/header)

## Dependencies
* Neovim
* Python3

## Contribution
If you have time ... nothing else just time ... you can do what
you want to do with this dummy neovim plugin. :joy:
