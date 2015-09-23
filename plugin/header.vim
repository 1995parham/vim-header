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
let s:bin_dir = expand('<sfile>:p:h:h') . '/bin/'
autocmd bufnewFile *.c,*.cpp,*.h,*.s,*.S,*.v,*.go,*.py,*.java,*.asm,*.bash,*.vim,*.js exe "read !" . s:bin_dir . "copyrighter.py --string " . " --user=" . g:header_user . " --email=" . g:header_email . " " . @%
