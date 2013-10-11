# -*- coding: cp1251 -*-
from grab.spider import Spider, Task
import grab
import logging
import time

class UserList(Spider):

    Pass = ''
    file_path = 'result.txt'

    initial_urls = ['http://158.181.161.77/forsergey/']

    def task_initial(self, grab, task):
        print 'Start'
        grab.setup(debug=True, log_dir='log')
        grab.set_input('post_password', self.Pass)
        grab.submit(make_request=False)
        yield Task('auth', grab = grab)

    def task_auth(self, grab, task):
        #print grab.response.body
        download_link = grab.doc.select('//button[@class="button-primary"]/a')
        download_url = download_link.attr('href')
        grab.setup(url=download_url)
        yield Task('download', grab = grab)

    def task_download(self, grab, task):
        grab.response.save(self.file_path)

if  __name__ ==  "__main__" :
	logging.basicConfig(level=logging.DEBUG)

	MyUserList = UserList(thread_number=2)
	MyUserList.Pass = '123456'
	MyUserList.run()
