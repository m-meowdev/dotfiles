call plug#begin()
Plug 'catppuccin/vim', { 'as': 'catppuccin' }
Plug 'sainnhe/gruvbox-material'
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
set clipboard+=unnamedplus
set termguicolors
set shortmess+=F
set expandtab
set smarttab
set shiftwidth=4
set tabstop=4
syntax enable

let wm = system('wmctrl -m')
if wm =~ 'LG3D' "qtile
    colorscheme catppuccin_mocha
    let g:lightline = {'colorscheme': 'catppuccin_mocha'}
elseif wm =~ 'awesome'
    set background=dark
    let g:gruvbox_material_background = 'hard'
    let g:gruvbox_material_better_performance = 1
    colorscheme gruvbox-material
    let g:lightline = {'colorscheme': 'gruvbox_material'}
endif

let g:python_highlight_all = 1
let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
