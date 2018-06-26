# vim-header
[![Travis branch](https://img.shields.io/travis/1995parham/vim-header/master.svg?style=flat-square)](https://travis-ci.org/1995parham/vim-header)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2ce6ccc4d58b4530acaba445adbd1b4b)](https://www.codacy.com/app/1995parham/vim-header?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=1995parham/vim-header&amp;utm_campaign=Badge_Grade)

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
