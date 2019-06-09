import logging

from lightnovel import LightNovelApi
from util import HtmlProxy, HtmlCachingProxy

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(name)16s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)
logging.getLogger("urllib3").setLevel(logging.ERROR)

# Set it
URL = 'https://www.wuxiaworld.com/novel/child-of-light'
CACHE = '.cache'
OUT = 'out'
DOWNLOAD = False

# Make it
proxy = HtmlCachingProxy(CACHE) if DOWNLOAD else HtmlProxy(CACHE)
api = LightNovelApi.get_api(URL, proxy)
# if not proxy.load(os.path.join(CACHE, api.name, URL.split('/')[-1])):
#     raise Exception("Couldn't set up proxy")

# Rip,
novel, chapters = api.get_entire_novel(URL, 1.0 if DOWNLOAD else 0.0)

# Export it
if len(chapters) == 0:
    exit(1)
api.compile_to_latex_pdf(novel, chapters, OUT)
