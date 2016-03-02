## fluentdの楽しさ・気づいたこと
* td-agent.confのうまい書き方をあれこれ探るのが楽しい。
* store先を増やしたいときに簡単に増やせる。僕はよくrelabel使って増やしやすいようにする。
* あらゆるサービスのハブとなれる存在なので、レガシー脱却するときは最初にfluentd導入から始めると幸せになりそう。

## fluentdを使い始めたのは運用を楽にしたいという気持ちが根本にある、その思想を忘れないために読むもの
* [運用を楽にするためのアプリケーションコードを書くということ - sonots:blog](http://blog.livedoor.jp/sonots/archives/44075238.html)

## disposableなアーキテクチャを目指す上でfluetndを使ってるとログは全て外部に保存したくなる、そんなときに読むもの
* [[Ruby] 例えば、Rails の標準ログを止める - sonots:blog](http://blog.livedoor.jp/sonots/archives/38927788.html)

## 最初に読みたいもの
* [Quickstart Guide | Fluentd](http://docs.fluentd.org/articles/quickstart)
* [Slides | Fluentd](http://www.fluentd.org/slides)
* [fluentdを導入時にまず知っておいたほうがよさそうなこと（インストール、監視、HA構成、チューニングなど） - Qiita](http://qiita.com/uzresk/items/3bfeeac82dfcb2a4300e)
* [Fluentdが流行る理由がいま分かる、10の実践逆引きユースケース集 - Y-Ken Studio](http://y-ken.hatenablog.com/entry/fluentd-case-studies)
* [Big Data入門に見せかけたFluentd入門](http://www.slideshare.net/keithseahus/big-datafluentd)

## 内部構造周り
* [Flutned Forward Protocol (Draft)](https://gist.github.com/kawanet/078e274952638fd53150)

## イマドキ(Fluentd v0.12時点)の事情を知りたいときに読む
* [Fluentd v0.12 master guide](http://www.slideshare.net/repeatedly/fluentd-v012-master-guide)
* [Fluentd v0.12 ラベル機能の使い方とプラグインの改修方法 - Qiita](http://qiita.com/sonots/items/a01d22210b7b059967)
* [Fluentd v0.12でのFilterとLabel - Go ahead!](http://repeatedly.github.io/ja/2014/08/fluentd-filter-and-label/)

## エラー周り
* [Fluentd の out_forward プラグインで良く出る warning メッセージとその負荷対策まとめ - sonots:blog](http://blog.livedoor.jp/sonots/archives/36895001.html)
* [fluentdでログが欠損する可能性を考える - sonots:blog](http://blog.livedoor.jp/sonots/archives/44690980.html)

## なんか新しい技術触るときはRelease NotesやChangeLogは全部読むよね
* [Blog | Fluentd](http://www.fluentd.org/blog/)
* [The td-agent ChangeLog | Treasure Data](https://docs.treasuredata.com/articles/td-agent-changelog)

## なんか新しい技術触るときはAdvent Calendar全部読むよね
* [Fluentd Advent Calendar 2013 - Qiita](http://qiita.com/advent-calendar/2013/fluentd)
* [Fluentd Advent Calendar 2014 - Qiita](http://qiita.com/advent-calendar/2014/fluentd)
* [Fluentd Advent Calendar 2015 - Qiita](http://qiita.com/advent-calendar/2015/fluentd)

## [WIP]プラグイン周りの知見
[gonsuke/fluent-plugin-dynamodb: Amazon DynamoDB output plugin for Fluent event collector](https://github.com/gonsuke/fluent-plugin-dynamodb) を今使いながら学んでいる

## [WIP]プラグイン周りの参考資料
* [fluentdプラグイン講座](http://toyama0919.bitbucket.org/fluentd_plugin_how_to.html#/)
* [fluentdのBufferedOutputプラグインを書くときの注意点とか | おそらくはそれさえも平凡な日々](http://www.songmu.jp/riji/entry/2015-01-29-fluent-buffer-plugin.html)
* [fluentdのためのプラグインをイチから書く手順 - たごもりすメモ](http://tagomoris.hatenablog.com/entry/20111117/1321511988)

## 正規表現の試行錯誤について
* [Tomohiro/fluentular: Fluentular is a Fluentd regular expression editor](https://github.com/Tomohiro/fluentular)

## バッファについて
* [td-agent のメモリバッファとファイルバッファでどんな違いが発生するか観察してみた - ようへいの日々精進XP](http://inokara.hateblo.jp/entry/2013/11/03/104235)
  * Output プラグインのメモリバッファとファイルバッファの性能はほとんど差異は無い
  * デフォルトはメモリバッファだがファイルバッファがオススメ

## buffer_chunk_limitについて
* [#fluentd fluentdでログ集約する際にwarnが多発した件 - oranie's blog](http://oranie.hatenablog.com/entry/20120508/1336490175)
  * 1プロセスの性能限界が来たけどOSレベルではリソースに余力がある場合、手動マルチプロセスを行えば、とりあえずOSレベルの限界くるまではスケールする。
* [FluentdでバッファつきOutputPluginを使うときのデフォルト値 - たごもりすメモ](http://tagomoris.hatenablog.com/entry/20130123/1358929254)

## secondaryまわり
* [fluentdで始めるログ管理【フォワード設定まとめ】 | Tech-Sketch](http://tech-sketch.jp/2014/02/fluentd%E3%81%A7%E5%A7%8B%E3%82%81%E3%82%8B%E3%83%AD%E3%82%B0%E7%AE%A1%E7%90%86%E3%80%90%E3%83%95%E3%82%A9%E3%83%AF%E3%83%BC%E3%83%89%E8%A8%AD%E5%AE%9A%E3%81%BE%E3%81%A8%E3%82%81%E3%80%91.html)

## logrotate
* [td-agent/td-agent.logrotate at master · treasure-data/td-agent](https://github.com/treasure-data/td-agent/blob/master/td-agent.logrotate)

## オッと思ったこと
```
<record>
  foo ${foo}           # existing syntax
  foo ${record["foo"]} # new syntax
</record>
```
[Fluentd v0.12.20 has been released | Fluentd](http://www.fluentd.org/blog/fluentd-v0.12.20-has-been-released)

```
td-agent --show-plugin-config=output:slack
```

[Fluentd v0.12.18 has been released | Fluentd](http://www.fluentd.org/blog/fluentd-v0.12.18-has-been-released)

## Railsアプリで使ってる人は...
[fluent/fluent-logger-ruby: A structured logger for Fluentd (Ruby)](https://github.com/fluent/fluent-logger-ruby)でアプリからfluentdにログ送ってる

## fluent-plugin-forestとは
[tagomoris/fluent-plugin-forest](https://github.com/tagomoris/fluent-plugin-forest)
冗長になりがちなmatchディレクティブをtemplateを使って共通化できる。
いくつかのプレースホルダーもサポートしている
${hostname}、${escaped_tag}、${tag_parts[n]}
case文も使える。caseはtemplateを上書きする。
remove_prefixも便利。

## fluent-plugin-slackとは
[sowawa/fluent-plugin-slack](https://github.com/sowawa/fluent-plugin-slack)
slackに送れるやつ。
デスクトップ通知時に文章が表示されない。READMEに書いてある。
[Attachments](https://api.slack.com/docs/attachments)を充実させたい。

## fluent-plugin-record-reformerとは
タグの付け替えやレコードの編集ができる。
filterプラグインを使ってもいいかも。[record_transformer Filter Plugin | Fluentd](http://docs.fluentd.org/articles/filter_record_transformer)とか。
record_transformerはタグの付け替えが出来ない。labelあるし、tagの付け替えをするケースはこれから減っていきそう。これからはrelabel。

## タグ設計について
labelディレクティブを使えばタグを付け替えで消耗せずに済んだりする.
[Fluentd v0.12 ラベル機能の使い方とプラグインの改修方法 - Qiita](http://qiita.com/sonots/items/a01d2233210b7b059967)

## LTSVについて

* [LTSV FAQ - LTSV って何? どういうところが良いの? - naoyaのはてなダイアリー](http://d.hatena.ne.jp/naoya/20130209/1360381374)
* [【今北産業】3分で分かるLTSV業界のまとめ【LTSV】 - naoyaのはてなダイアリー](http://d.hatena.ne.jp/naoya/20130207/1360240992)
* [sonots/ltsv_log_formatter: A ruby logger formatter to output log in LTSV format](https://github.com/sonots/ltsv_log_formatter)

## リトライ時の挙動
fluentdがリトライすると`2016-03-02 16:21:06 +0900 [warn]: retry succeeded. plugin_id="cloudwatch_logs"`というログが出る。
https://github.com/fluent/fluentd/blob/master/lib/fluent/output.rb#L344

plugin_idは`@id`で付けたやつなので、やっぱり位置付け的に大事なプラグインには`@id`をちゃんとつけたほうが障害調査時に助かる。
