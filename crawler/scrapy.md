# Scrapy
* [Scrapy | A Fast and Powerful Scraping and Web Crawling Framework](http://scrapy.org/)
* [Scrapy at a glance — Scrapy 1.1.0 documentation](http://doc.scrapy.org/en/latest/intro/overview.html)

Python製のクローラーフレームワーク。Quoraに「[Is there a better crawler than Scrapy?](https://www.quora.com/Is-there-a-better-crawler-than-Scrapy)」っていうスレッドも立つくらいだから結構人気だと思う。

## Feature
>Requests are scheduled and processed asynchronously. This means that Scrapy doesn’t need to wait for a request to be finished and processed, it can send another request or do other things in the meantime. This also means that other requests can keep going even if some request fails or an error happens while handling it.
>While this enables you to do very fast crawls (sending multiple concurrent requests at the same time, in a fault-tolerant way)

非同期にリクエスト投げるからRedis::DistMutexみたいな時限付き分散ロックが不要。エラーが起きてもScrapyがいい感じにハンドリングしてくれる。

>Built-in support for selecting and extracting data from HTML/XML sources using extended CSS selectors and XPath expressions, with helper methods to extract using regular expressions.

CSSセレクタやXPath、正規表現で抽出できるヘルパーもある。

>An interactive shell console (IPython aware) for trying out the CSS and XPath expressions to scrape data, very useful when writing or debugging your spiders.

IPython(pry的なやつ)使ったデバッグもしやすい。XPathとか試行錯誤しやすい。

>Built-in support for generating feed exports in multiple formats (JSON, CSV, XML) and storing them in multiple backends (FTP, S3, local filesystem)

クロール結果をエクスポートするバックエンドは各種取り揃えている。

>Robust encoding support and auto-detection, for dealing with foreign, non-standard and broken encoding declarations.

エンコーディングも自動で判別。

>Strong extensibility support, allowing you to plug in your own functionality using signals and a well-defined API (middlewares, extensions, and pipelines).

独自処理で拡張できる。シグナルとかAPIもあるし。
