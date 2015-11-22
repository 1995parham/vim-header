" In The Name Of God
" Vim plugin file
" Last Change:	2015 Sep 24
" Maintainer:	Parham Alvani <parham.alvani@gmail.com>

if !exists('g:header_user')
	let g:header_user = system ("id -un | tr -d '\n'")
endif
if !exists('g:header_email')
	let g:header_email = ''
endif
autocmd bufnewFile * exe "0read !" . "copyrighter.py --string " . " --name=" . "\"" . g:header_user . "\"" . " --email=" . "\"" . g:header_email . "\"" . " " . @%
