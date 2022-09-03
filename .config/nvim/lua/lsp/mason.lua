local mason_status_ok, mason = pcall(require, "mason")
if not mason_status_ok then
    return
end

local mlsp_status_ok, mason_lspconfig = pcall(require, "mason-lspconfig")
if not mlsp_status_ok then
    return
end

local lspconfig_status_ok, lspconfig = pcall(require, "lspconfig")
if not lspconfig_status_ok then
    return
end

local servers = {
    "pylsp",
    "sumneko_lua",
}

mason.setup()
mason_lspconfig.setup()

local opts = {}

for _, server in pairs(servers) do
    opts = {
        on_attach = require("lsp.handlers").on_attach,
        capabilities = require("lsp.handlers").capabilities,
    }

    if server == "sumneko_lua" then
        local sumneko_opts = require("lsp.settings.sumneko_lua")
        opts = vim.tbl_deep_extend("force", sumneko_opts, opts)
    elseif server == "pylsp" then
        local pylsp_opts = require("lsp.settings.pylsp")
        opts = vim.tbl_deep_extend("force", pylsp_opts, opts)
    end

    lspconfig[server].setup(opts)
end
