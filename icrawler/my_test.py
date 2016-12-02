from icrawler.examples import GoogleImageCrawler
from icrawler.examples import BingImageCrawler
#from icrawler.examples import BaiduImageCrawler

# max number of images to download from each source
num = 500
# max number of threads to use for each source
num_threads = 8

google_crawler = GoogleImageCrawler('data/google')
google_crawler.crawl(keyword='daesh flag', offset=0, max_num=num,
                     date_min=None, date_max=None, feeder_thr_num=1,
                     parser_thr_num=1, downloader_thr_num=num_threads,
                     min_size=(200,200), max_size=None)

bing_crawler = BingImageCrawler('data/bing')
bing_crawler.crawl(keyword='daesh flag', offset=0, max_num=num,
                   feeder_thr_num=1, parser_thr_num=1, downloader_thr_num=num_threads,
                   min_size=None, max_size=None)

#baidu_crawler = BaiduImageCrawler('data/baidu')
#baidu_crawler.crawl(keyword='daesh flag', offset=0, max_num=num,
#                    feeder_thr_num=1, parser_thr_num=1, downloader_thr_num=num_threads,
#                    min_size=None, max_size=None)
