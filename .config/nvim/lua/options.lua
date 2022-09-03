local options = {

	-- pretty colors
	termguicolors = true,

    -- dark background
    background = "dark",

	-- line numbering
	number = true,
	relativenumber = true,

	-- nice indents
	expandtab = true,
	smarttab = true,
	smartindent = true,
	shiftwidth = 4,
	tabstop = 4,

	-- use system clipboard
	clipboard = "unnamedplus",

	-- ignore case in searches unless told otherwise
	ignorecase = true,
	smartcase = true,

	-- no backups, yes undo
	backup = false,
	writebackup = false,
	swapfile = false,
	undofile = true,

	-- don't highlight previous search results
	hlsearch = false,

	-- mouse support
	mouse = "a",

	-- split behavior
	splitbelow = true,
	splitright = true,

	-- highlight current line
	cursorline = true,

	-- completion
	completeopt = "menu,menuone,noselect",

    timeoutlen = 500,

}

for k, v in pairs(options) do
  vim.o[k] = v
end
