import scrapy

class ExpSpider(scrapy.Spider):
    name = 'vnexpress'
    start_urls = [
        'https://vnexpress.net/kinh-doanh',
        'https://vnexpress.net/thoi-su',
        'https://vnexpress.net/giai-tri',
        'https://vnexpress.net/the-thao',
        'https://vnexpress.net/phap-luat',
        'https://vnexpress.net/the-gioi',
        'https://vnexpress.net/goc-nhin',
        'https://vnexpress.net/giao-duc',
        'https://vnexpress.net/suc-khoe',
        'https://vnexpress.net/doi-song',
        'https://vnexpress.net/oto-xe-may',
    ]

    def parse(self, response):
        links = response.css(".title_news a::attr('href')").getall()
        print('LINK ==========', links)
        for link in links:
            url = link
            yield response.follow(url = url, callback = self.parse_content)

    def parse_content(self, response):
        domain = response.request.url.split("/")[3]
        if domain != "suc-khoe":
            intro = response.css('h1.title_news_detail::text').get().strip()
            description = response.css('.description::text').get().strip()
            content = response.xpath('/html/body/section[2]/section[1]/section[1]/article').css('.Normal::text').getall()
            yield {
                "link": response.request.url,
                "domain": domain,
                "intro": intro,
                "description": description,
                "content": ' '.join(content).strip().replace("\xa0", "").replace("\n", "").replace("\t", "")
            }
        else:
            intro = response.css('h1.title_news_detail::text').get().strip()
            description = response.css('.description::text').get().strip()
            content = response.xpath('/html/body/section[2]/section[1]/article').css('.Normal::text').getall()
            yield {
                "link": response.request.url, 
                "domain": domain,
                "intro": intro,
                "description": description,
                "content": ' '.join(content).strip().replace("\xa0", "").replace("\n", "").replace("\t", "")
            }

