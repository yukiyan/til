# Tutorial
* [Scrapy Tutorial — Scrapy 1.1.0 documentation](http://doc.scrapy.org/en/latest/intro/tutorial.html)

## プロジェクト作成

https://www.dmoz.org/ をクロールする。  

`$ scrapy startproject tutorial` でプロジェクト作成。  

```
tutorial
├── scrapy.cfg    デプロイの設定書く
└── tutorial
    ├── __init__.py
    ├── items.py    クロールするアイテム情報を書く
    ├── pipelines.py
    ├── settings.py
    └── spiders
        ├── __init__.py
```

## Itemについて
https://github.com/yukiyan/til/pull/12/commits/cecb18b  
クロールしたデータをぶち込むコンテナ。Pythonのdictみたいな振る舞いをするイメージ。  

## Spiderについて
https://github.com/yukiyan/til/pull/12/commits/099e02e  
どのようにクロール処理を施すか定義するクラス。  
クロール先URL、ドメイン、レスポンスをどうパースしていくかを記述していく。  

* `name` はSpiderを識別するもの。Spiderを複数作る場合は各々の `name` は一意でなければならない。
* `start_urls` はクロール先URLを書く。
* `parse()` はレスポンスをパースしてItemオブジェクトを返す責務を持ったメソッド。

## クロールする
https://github.com/yukiyan/til/pull/12/commits/a774183  
`$ scrapy crawl dmoz` でSpiderがクロールしにいく。  
`parse()` に基づいた処理が施される。  

## クロール時の動き
Scrapyによって `scrapy.http.Request` オブジェクトが `start_urls` の各値に対して生成される。  
`scrapy.Request` オブジェクトはコールバック関数として `parse()` にアサインされる。  
`parse()` 後、`scrapy.http.Response` オブジェクトとして返ってくる。  

## セレクタについて
Scrapyは、[XPathやCSSセレクタ](http://doc.scrapy.org/en/latest/topics/selectors.html#topics-selectors)を使っている。
XPathの学習は、  

* [XPath 1.0 Tutorial @ZVON.org](http://zvon.org/comp/r/tut-XPath_1.html)
* [A very brief primer to thinking in XPath // plasmasturm.org](http://plasmasturm.org/log/xpath101/)

が良い。  

ScrapyにはヘルパーとしてSelectrorクラスがあるのでXPathを生で毎回ガッツリ書かなくても良い。  

## XPathの試行錯誤
IPythonでインタラクティブにXPathを試せる。

```
% scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
2016-05-27 08:36:30 [scrapy] INFO: Scrapy 1.1.0 started (bot: tutorial)

...

[s] Available Scrapy objects:
[s]   crawler    <scrapy.crawler.Crawler object at 0x10944d390>
[s]   item       {}
[s]   request    <GET http://www.dmoz.org/Computers/Programming/Languages/Python/Books/>
[s]   response   <200 http://www.dmoz.org/Computers/Programming/Languages/Python/Books/>
[s]   settings   <scrapy.settings.Settings object at 0x109cace48>
[s]   spider     <DmozSpider 'dmoz' at 0x10a062d30>
[s] Useful shortcuts:
[s]   shelp()           Shell help (print this help)
[s]   fetch(req_or_url) Fetch request (or URL) and update local objects
[s]   view(response)    View response in a browser

...

In [1]: response.xpath('//title').extract()
Out[1]: ['<title>DMOZ - Computers: Programming: Languages: Python: Books</title>']

In [2]: response.xpath('//title/text()').re('(\w+):')
Out[2]: ['Computers', 'Programming', 'Languages', 'Python']
```
