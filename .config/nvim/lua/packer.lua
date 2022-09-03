local fn = vim.fn

-- packer auto install
local install_path = fn.stdpath "data" .. "/site/pack/packer/start/packer.nvim"

if fn.empty(fn.glob(install_path)) > 0 then
	PACKER_BOOTSTRAP = fn.system{
		"git",
		"clone",
		"--depth",
		"1",
		"https://github.com/wbthomason/packer.nvim",
		install_path,
    }

    print("Installing packer...")
    print("Please restart Neovim for installation to take effect.")
    vim.cmd [[packadd packer.nvim]]
end

-- restart neovim when plugins.lua is saved
vim.cmd [[
    augroup packer_user_config
        autocmd!
        autocmd BufWritePost plugins.lua source <afile> | PackerSync
    augroup end
]]

local status_ok, packer = pcall(require, "packer")
if not status_ok then
    return
end

-- display packer as popup
packer.init{
    display = {
        open_fn = function()
            return require("packer.util").float()
        end,
    },
}

-- plugins
return packer.startup(function(use)

    -- packer self-manage
    use "wbthomason/packer.nvim"

    -- colorschemes
	use { "catppuccin/nvim", as = "catppuccin" }
    use "sainnhe/gruvbox-material"

    -- statusline
    use {
        "nvim-lualine/lualine.nvim",
        requires = { "kyazdani42/nvim-web-devicons", opt = true }
    }

    -- lsp
    use "neovim/nvim-lspconfig"
    use "williamboman/mason-lspconfig.nvim"
    use "williamboman/mason.nvim"

    -- completion
    use "hrsh7th/cmp-nvim-lsp"
    use "hrsh7th/cmp-nvim-lua"
    use "hrsh7th/cmp-buffer"
    use "hrsh7th/cmp-path"
    use "hrsh7th/cmp-cmdline"
    use "hrsh7th/nvim-cmp"
    use "saadparwaiz1/cmp_luasnip"

    -- snippets
    use "L3MON4D3/LuaSnip"
    use "rafamadriz/friendly-snippets"

    -- telescope
    use {
        "nvim-telescope/telescope.nvim", branch = "0.1.x",
        requires = { "nvim-lua/plenary.nvim" }
    }
    use {'nvim-telescope/telescope-fzf-native.nvim', run = 'make' }

    -- treesitter
    use {
        "nvim-treesitter/nvim-treesitter",
        run = function() require("nvim-treesitter.install").update{ with_sync = true } end
    }
    use "p00f/nvim-ts-rainbow"
    use "JoosepAlviste/nvim-ts-context-commentstring"

    -- autopairs
    use "windwp/nvim-autopairs"

    -- comments
    use "numToStr/Comment.nvim"

    -- tree
    use "kyazdani42/nvim-tree.lua"

    -- color highlight
    use "NvChad/nvim-colorizer.lua"

    -- indent lines
    use "lukas-reineke/indent-blankline.nvim"

    -- fast loading
    use "lewis6991/impatient.nvim"

    -- whichkey
    use "folke/which-key.nvim"

    -- automatically install all plugins after installing packer
    if PACKER_BOOTSTRAP then
        require("packer").sync()
    end

end)
