call plug#begin()
Plug 'catppuccin/vim', { 'as': 'catppuccin' }
Plug 'itchyny/lightline.vim'
Plug 'ap/vim-css-color'
Plug 'Fymyte/rasi.vim'
Plug 'vim-python/python-syntax'
call plug#end()

set laststatus=2
set noshowmode
set nocompatible
set incsearch
set wildmenu
set nobackup
set noswapfile
set t_Co=256
set number relativenumber
set clipboard=unnamedplus
set termguicolors
set shortmess+=F
set expandtab
set smarttab
set shiftwidth=4
set tabstop=4
syntax enable
colorscheme catppuccin_mocha
let g:lightline = {'colorscheme': 'catppuccin_mocha'}
let g:python_highlight_all = 1
let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
