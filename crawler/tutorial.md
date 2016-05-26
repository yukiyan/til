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
