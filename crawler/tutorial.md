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
クロールしたデータをぶち込むコンテナ。Pythonのdictみたいな振る舞いをするイメージ。  
