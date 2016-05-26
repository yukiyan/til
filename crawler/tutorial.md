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
cecb18b  
クロールしたデータをぶち込むコンテナ。Pythonのdictみたいな振る舞いをするイメージ。  

## Spiderについて

どのようにクロール処理を施すか定義するクラス。  
クロール先URL、ドメイン、レスポンスをどうパースしていくかを記述していく。  

* `name` はSpiderを識別するもの。Spiderを複数作る場合は各々の `name` は一意でなければならない。
* `start_urls` はクロール先URLを書く。
* `parse()` はレスポンスをパースしてItemオブジェクトを返す責務を持ったメソッド。
