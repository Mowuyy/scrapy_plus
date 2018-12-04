#coding:utf-8

#### baidu 的SpiderMiddleware和DownloaderMiddleware



class BaiduSpiderMiddleware1(object):
    def process_item(self, item, spider):
        print("[BaiduSpiderMiddleware1] process_item : {}".format(item.data))
        return item

    def process_request(self, request, spider):
        print("[BaiduSpiderMiddleware1] process_request : {}".format(request.url))
        return request


class BaiduSpiderMiddleware2(object):
    def process_item(self, item, spider):
        print("[BaiduSpiderMiddleware2] process_item : {}".format(item.data))
        return item

    def process_request(self, request, spider):
        print("[BaiduSpiderMiddleware2] process_request : {}".format(request.url))
        return request




class BaiduDownloaderMiddleware1(object):
    def process_response(self, response, spider):
        print("[BaiduDownloaderMiddleware1] process_response : {}".format(response.url))
        return response

    def process_request(self, request, spider):
        print("[BaiduDownloaderMiddleware1] process_request : {}".format(request.url))
        return request


class BaiduDownloaderMiddleware2(object):
    def process_response(self, response, spider):
        print("[BaiduDownloaderMiddleware2] process_response : {}".format(response.url))
        return response

    def process_request(self, request, spider):
        print("[BaiduDownloaderMiddleware2] process_request : {}".format(request.url))
        return request








#### douban 的SpiderMiddleware和DownloaderMiddleware



class DoubanSpiderMiddleware1(object):
    def process_item(self, item, spider):
        print("[DoubanSpiderMiddleware1] process_item : {}".format(item.data))
        return item

    def process_request(self, request, spider):
        print("[DoubanSpiderMiddleware1] process_request : {}".format(request.url))
        return request


class DoubanSpiderMiddleware2(object):
    def process_item(self, item, spider):
        print("[DoubanSpiderMiddleware2] process_item : {}".format(item.data))
        return item

    def process_request(self, request, spider):
        print("[DoubanSpiderMiddleware2] process_request : {}".format(request.url))
        return request




class DoubanDownloaderMiddleware1(object):
    def process_response(self, response, spider):
        print("[DoubanDownloaderMiddleware1] process_response : {}".format(response.url))
        return response

    def process_request(self, request, spider):
        print("[DoubanDownloaderMiddleware1] process_request : {}".format(request.url))
        return request


class DoubanDownloaderMiddleware2(object):
    def process_response(self, response, spider):
        print("[DoubanDownloaderMiddleware2] process_response : {}".format(response.url))
        return response

    def process_request(self, request, spider):
        print("[DoubanDownloaderMiddleware2] process_request : {}".format(request.url))
        return request



class DownloaderMiddleware(object):
    def process_response(self, response, spider):
        print("[DownloaderMiddleware] process_response : {}".format(response.url))
        return response

    def process_request(self, request, spider):
        print("[DownloaderMiddleware] process_request : {}".format(request.url))
        return request


