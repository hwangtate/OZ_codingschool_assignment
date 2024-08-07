from utils.crawl_util import CrawlInform

#멜론차트 100 스크래핑
melon_inform = CrawlInform(
    'https://www.melon.com/chart/index.htm',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
)
MELON_SEARCH = melon_inform.url
MELON_HEADER = melon_inform.header

