local colorscheme = "catppuccin"

if colorscheme == "catppuccin" then
    vim.g.catppuccin_flavour = "mocha"
    local status_ok, catppuccin = pcall(require, colorscheme)
    if not status_ok then
        return
    end
    catppuccin.setup{
        integrations = {
            ts_rainbow = true,
        },
    }
elseif colorscheme == "gruvbox-material" then
    vim.g.gruvbox_material_background = "medium"
    vim.g.gruvbox_material_better_performance = 1
end

local status_ok, _ = pcall(vim.cmd, "colorscheme " .. colorscheme)
if not status_ok then
    return
end

return colorscheme
