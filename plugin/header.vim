" In The Name Of God
" Vim plugin file
" Last Change:	2015 Sep 24
" Maintainer:	Parham Alvani <parham.alvani@gmail.com>

let s:user = system ("id -un | tr -d '\n'")
let s:email = ''
let s:install_dir = expand('<sfile>:p:h') . '/bin'
autocmd bufnewFile *.c,*.cpp,*.h,*.s,*.S,*.v,*.go,*.py,*.java,*.asm,*.bash,*.vim,*.js exe "read !" . s:install_dir . "copyrighter.py --string " . " --user=" . s:user . " --email=" . s:email . " " . @%
