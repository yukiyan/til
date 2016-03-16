## Capture Fluentd logs
* [Logging of Fluentd | #capture-fluentd-logs](http://docs.fluentd.org/articles/logging#capture-fluentd-logs)


fluentd自身のログは`fluent.**`というタグでキャプチャできる。  
キャプチャした際、keyはmessageのみでlogレベルはタグに含まれる。 例: `fluent.info: { "message":"hogehoge"} `  


こんな感じで別の場所に飛ばしても良いかもしれない。  

```
<filter fluent.**>
  @type record_transformer
  <record>
    message "[${tag_parts[1]}] ${message}"
  </record>
</filter>

<match **>
  @type どこか
  message_keys message
</match>
```

ログレベルで動作を分けたいならこんな感じで振り分ければいい。  

```
<match fluent.**>
  @type grep
  regexp1 original_tag fluent.(warn|error|fatal)
  add_tag_prefix filtered
</match>

<match filtered.**>
  @type forest
  subtype slack
  <template>
    ...
  </template>
  <case **.warn>
    ...
    channel warn-notify
    ...
  </case>
  <case **.error>
    ...
    channel error-notify
    ...
  </case>
  <case **.fatal>
    ...
    channel fatal-notify
    ...
  </case>
</match>
```

filter grep使いたいところだが、ログレベルの情報がタグにしか含まれてないので使えない。(filter grepはタグから情報を取れない)

## 地味にハマったところ
こうだとうまくいかなかった。

```
<match fluent.warn>
  @type slack
  ...
</match>

<match fluent.error>
  @type slack
  ...
</match>

<match fluent.fatal>
  @type slack
  ...
</match>
```

最初に`fluent.**`でキャプチャしてからルーティングしないといけない。
なので以下のようにすると良い。

```
<match fluent.**>
  @type relabel
  @label @fluent_log_to_slack
</match>

<label @fluent_log_to_slack>
  <match fluent.warn>
    @type slack
    ...
  </match>

  <match fluent.error>
    @type slack
    ...
  </match>

  <match fluent.fatal>
    @type slack
    ...
  </match>
</label>
```

`<match fluent.**>`としているところは実際タグとしてどんな値が入ってるのかはまだ調べてない。
`<match fluent>`でも`<match fluent.info>`でもダメだったので謎。
ちゃんと https://github.com/fluent/fluentd/blob/master/lib/fluent/log.rb を読んだほうがいいかも。
