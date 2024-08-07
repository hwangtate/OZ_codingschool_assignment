from utils import CrawlUtil, MELON_HEADER, MELON_SEARCH,melon_print


class MelonCrawler(CrawlUtil):
    def __init__(self, url, header_user):
        super().__init__(url, header_user)


if __name__ == '__main__':
    #멜론 차트 크롤링
    melon = MelonCrawler(MELON_SEARCH, MELON_HEADER)
    wrap = melon.select('#conts')
    melon_print(wrap)

