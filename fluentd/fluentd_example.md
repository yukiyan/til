(例) /var/www/xxxx/xxxx/log/production.log の uri というフィールドに yukiyan という文字が含まれていたら、特定の文面をメールで送ってslackにも通知する。

```
<source>
  @type tail
  path /var/www/xxxx/xxxx/log/production.log
  pos_file /var/tmp/xxxx.production.log.pos
  tag hoge.app
  format /^id:(?<id>.+)[\t]*time:\[(?<time>.+)\][\t]*uri:(?<uri>.*)[\t]*message:(?<message>.*)$/
</source>

<filter hoge.app>
  @type grep
  regexp1 uri yukiyan
</filter>

<match hoge.**>
  @type record_reformer
  tag notification.hoge
  hostname #{Socket.gethostname}
  body ${message.gsub("\\n", "\n").gsub("\\t", "  ")}
</match>

<match notification.**>
  @type copy
  <store>
    @type mail
    host 'localhost'
    port 25
    from sample@gmail.com
    to dev@gmail.com, customer@gmail.com
    subject "application log: %s"
    subject_out_keys hostname
    message %s\n
    message_out_keys body
    time_locale JST
  </store>

  <store>
    @type slack
    webhook_url https://hooks.slack.com/services/xxxx/xxxxxxxxxxxxxx
    channel dev-notification
    username td-agent
    icon_emoji :smile:
    title %s
    title_keys hostname
    message "%s"
    message_keys body
    color good
    flush_interval 0s
    mrkdwn fields
  </store>
</match>
```

## 設定ファイルの解説

### source
```
<source>
  @type tail
  path /var/www/xxxx/xxxx/log/production.log
  pos_file /var/tmp/xxxx.production.log.pos
  tag hoge.app
  format /^id:(?<id>.+)[\t]*time:\[(?<time>.+)\][\t]*uri:(?<uri>.*)[\t]*message:(?<message>.*)$/
</source>
```

sourceディレクティブではログの入力方法を決める。

* `@type`
  * インプットプラグインを指定する。この場合は[in_tailプラグイン](http://docs.fluentd.org/articles/in_tail)を使っている。
* `path`
  * tailするログのパスを指定。chefのtemplateでerbなんかにして`path /var/www/xxxx/xxxx/log/<%=node['environment']>.log`と書くのも良いかもしれない。
* `pos_file`
  * ログを読んだ位置を書き込むファイルを指定する。ここで位置を記憶して異常時に再送するときに使われる。
* `tag`
  * ログを出し分けるためのタグをつける。
* `format`
  * 正規表現でログをマッチさせる。あとでフィールドとして参照したいものは名前付き後方参照にする。

### filter

```
<filter hoge.app>
  @type grep
  regexp1 uri yukiyan
</filter>
```

ログをfilterプラグインで絞り込んだり、整形したりする。
`hoge.app`というタグがつけられたものがここに流れてくる。

* `@type`
  * filterプラグインを指定する。この場合は[filter_grepプラグイン](http://docs.fluentd.org/articles/filter_grep)を使っているので正規表現で絞り込む処理が施される。
* `regexp1`
  * フィールドに対して絞り込みたい正規表現を書く。この場合は、uriというフィールド名にyukiyanという文字が含まれているログが以降に流れていく。

### [WIP]match

```
<match hoge.**>
  type record_reformer
  tag notification.hoge
  hostname #{Socket.gethostname}
  body ${message.gsub("\\n", "\n").gsub("\\t", "  ")}
</match>
```
