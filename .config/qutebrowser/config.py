import catppuccin

colorscheme = "catppuccin"

config.load_autoconfig(False)

c.aliases = {
    "q": "quit",
    "w": "session-save",
    "wq": "quit --save",
}

if colorscheme == "catppuccin":
    catppuccin.setup(c, "mocha")
else:
    config.source(colorscheme + ".py")

c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = "lightness-hsl"
c.colors.webpage.darkmode.contrast = -.022
c.colors.webpage.darkmode.threshold.background = 100
c.colors.webpage.darkmode.threshold.text = 150
c.colors.webpage.darkmode.policy.images = "always"
c.colors.webpage.darkmode.grayscale.images = 0.35
c.colors.webpage.preferred_color_scheme = "dark"

c.fonts.default_family = "TerminessTTF Nerd Font"
c.fonts.default_size = "11pt"

c.completion.web_history.exclude = ["*://duckduckgo.com/*"]

c.confirm_quit = ["downloads"]

c.content.autoplay = False
c.content.blocking.adblock.lists = [
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt",
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
    "https://malware-filter.gitlab.io/malware-filter/phishing-filter.txt",
    "https://malware-filter.gitlab.io/malware-filter/pup-filter.txt",
    "https://raw.githubusercontent.com/bogachenko/fuckfuckadblock/master/fuckfuckadblock.txt",
    "https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt",
    "https://raw.githubusercontent.com/yourduskquibbles/webannoyances/master/ultralist.txt",
]
c.content.blocking.method = "adblock"
c.content.canvas_reading = False
c.content.cookies.accept = "no-3rdparty"
c.content.cookies.store = False
c.content.default_encoding = "utf-8"
c.content.headers.custom = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
c.content.headers.user_agent = "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/104.0.0.0 Safari/{webkit_version}"
c.content.notifications.enabled = False
c.content.user_stylesheets = []
c.content.webgl = False
