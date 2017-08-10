## python爬虫学习

博客资料参考 : http://cuiqingcai.com/2599.html

一直认为前端工程师更加适合作为一名爬虫er，以前只会使用node+cheerio来进行网页爬取，现在想通过python系统学习一下爬虫的相关知识，因此开了这个repos记录一下自己的学习过程，至于为什么要从最简单的urllib学起，而不是直接上pySpider和scrapy这样成熟的爬虫框架，我的理解是，这样能够更加清楚的理解爬虫过程，万丈高楼平地起，其实和前端学习一样，当然可以一开始就上手Vue这样的框架，然而我一直觉得原生js才是最美的～

1.qiushibaike.py

对糗事百科网站进行爬取，这个网站没有登录限制，然而直接使用最简单的方式并不能爬取成功，原因是因为要加上user-agent，然后就能拿到html源码啦，接下来就是正则表达式的操作了，想念cheerio的第一天～

2.baidubaike.py

对百度百科网站进行爬取，由于有了第一个例子的基础，较为轻松，在这个文件内部封装了一个tool工具类，用于使用正则表达式过滤字符串，还是hin有意思的

3.taobaomm.py

对淘宝美眉进行爬取，爬取每个美眉的头像，身份等各种信息，通过这次练习，了解了如何判断文件是否存在os.path.exists，如何创建文件，os.makedirs，如何保存一个图片，其实就是写入二进制文件2333

4.hupubbs.py

对虎扑bbs进行爬取，爬取一个帖子的每一层，不难，主要为了练习requests和beautiful soup，特别是bs4，哇，有了他，仿佛在node爬虫中有了cheerio，摆脱正则的感觉简直要飞了起来

5.phantom.js

使用phantom.js愉快的玩帅，前面我们进行爬取的方式都是抓取HTML进行分析，然而有很多JS渲染的网站[允悲]，PhantomJS是一个无界面的,可脚本编程的WebKit浏览器引擎，可以把phantomjs当做一个微型浏览器，通过它，我们可以进行网页截图！！！，这是最大的卖点，现在phantomjs支持从外部引入js文件，可以引入jqeury，然后调用evaluate方法对网页进行分析

6. selenium.py

看到第五个练习，可能很多同学都会觉得我好好的写着python，突然给我来个js的东东，怎么玩啊，其实phantomjs就是个没有浏览器页面的webkit内核浏览器，我们可以通过phantomjs动态进行页面的操作，从而进行python的爬取，建议调试的时候用Chrome，真实环境用phantomJS即可，需要将phantomjs添加进入环境遍历～
