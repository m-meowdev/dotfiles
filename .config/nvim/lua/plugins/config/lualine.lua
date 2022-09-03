local colorscheme = require("colors")

require("lualine").setup {
    options = {
        theme = colorscheme,
        component_separators = { left = "|", right = "|" },
        section_separators = { left = "", right = "" }
    }
}
