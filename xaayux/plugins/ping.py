
from .. import client
from telethon import events
import logging 
import asyncio
import time
from xaayux.config import DELAY

D = DELAY

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -- Constants -- #
HELP = """
𝘼𝙪𝙩𝙤𝙋𝙞𝙘𝙓 __Commands__

`!start` - __To Start Changing DP__
`!cancel` - __To Cancel Changing DP__
`!alive` - __To Check If Bot Is Alive__
`!repo` - __To Get The Repo__
`!about` - __Details About Me__
`!help` - __For This Message__
"""

ABOUT_TXT = """
᪥ **Name:** 𝘼𝙪𝙩𝙤𝙋𝙞𝙘𝙓
᪥ **Library: [Telethon](https://docs.telethon.dev/)**
᪥ **Language: [Python 3](https://www.python.org)**
᪥ **Dev:** [𝙄𝙩𝙨 ⚡ 𝙅𝙤𝙚𝙡](https://t.me/joel_noob)
᪥ **Inspiration: [Dᴋ 🇮🇳](https://t.me/AbOutMe_DK)**
"""

REPO = """
𝘼𝙪𝙩𝙤𝙋𝙞𝙘𝙓 __is an Open Source UserBot based on Telethon you can access it's source code from **[here](https://github.com/git-itsjoel/AutoPicX)**__
"""

@client.on(events.NewMessage(outgoing=True, pattern='!repo'))
async def repo(event):
    await event.edit(REPO, link_preview=False)

@client.on(events.NewMessage(outgoing=True, pattern='!about'))
async def about(event):
    await event.edit(ABOUT_TXT, link_preview=False)


@client.on(events.NewMessage(outgoing=True, pattern='!help'))
async def help_me(event):
    await event.edit(HELP)


@client.on(events.NewMessage(outgoing=True, pattern='!alive'))
async def alive(event):
    txt = await event.edit("▢▢▢")
    await event.edit("▣▢▢")
    await event.edit("▣▣▢")
    await event.edit("▣▣▣")
    await event.edit("𝗔𝘂𝘁𝗼 𝗦𝗰𝗵𝗲𝗱𝘂𝗹𝗲𝗿 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗜𝘀 𝗔𝗰𝘁𝗶𝘃𝗲 𝗔𝗻𝗱 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗦𝗲𝗻𝗱𝗶𝗻𝗴 𝗔𝗻𝗱 𝗦𝗰𝗵𝗲𝗱𝘂𝗹𝗶𝗻𝗴 𝗗𝗲𝗮𝗹𝘆 𝗜𝘀 𝗦𝗲𝘁 𝗧𝗼 {D}(𝗦𝗲𝗰𝗼𝗻𝗱𝘀)")
