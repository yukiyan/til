## fluent-catを使ってデバッグする方法
レコードを書き換えたり、ルーティングがうまくいってるかの確認にはfluent-catをよく使っている。

```
<source>
  @type forward
</source>

<filter debug.**>
  @type record_transformer
  <record>
    tag ${hostname}
  </record>
</filter>

<match debug.**>
  @type record_reformer
  tag ${tag}.${hostname}
</match>

<match staging-1.debug.**>
  @type stdout
</match>
```

`tail -f /var/log/td-agent/td-agent.log` しながら色んなパターンのレコードを`fluent-cat`したりする。
```
echo '{"message":"message dayo"}' | /opt/td-agent/embedded/bin/fluent-cat debug
```

## テストを実行しながらデバッグする方法
プラグイン自体の動作確認は`binding.pry`で止めながらテスト実行したりしてる。
[yukiyan/fluent-plugin-slack](https://github.com/yukiyan/fluent-plugin-slack) を題材に説明してみる。  
[sowawa/fluent-plugin-slack](https://github.com/sowawa/fluent-plugin-slack)からforkしてきて機能を改修したのだが、非常に勉強になった。

### 合わせて読みたい
* [Test::Unitでテストを書く - Qiita](http://qiita.com/repeatedly/items/727b08599d87af7fa671)
* [test-unitで指定したテストだけ実行する方法 - Qiita](http://qiita.com/myokoym/items/2c3559ec0e060b7ec943)

### テスト実行(rakeタスク)
```
😀  [wakayama ♟  ~/src/github.com/yukiyan/fluent-plugin-slack ✔  master ]
% rake test
/Users/wakayama/.rbenv/versions/2.2.3/bin/ruby -I"lib:lib:test" -I"/Users/wakayama/src/github.com/yukiyan/fluent-plugin-slack/vendor/bundle/ruby/2.2.0/gems/rake-10.5.0/lib" "/Users/wakayama/src/github.com/yukiyan/fluent-plugin-slack/vendor/bundle/ruby/2.2.0/gems/rake-10.5.0/lib/rake/rake_test_loader.rb" "test/**/test_*.rb"
Loaded suite /Users/wakayama/src/github.com/yukiyan/fluent-plugin-slack/vendor/bundle/ruby/2.2.0/gems/rake-10.5.0/lib/rake/rake_test_loader
Started
...........................

Finished in 8.26497 seconds.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
27 tests, 68 assertions, 0 failures, 0 errors, 0 pendings, 0 omissions, 0 notifications
100% passed
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3.27 tests/s, 8.23 assertions/s
```

### テスト実行(ruby単体実行)
`rake test`と同じ。

```
😀  [wakayama ♟  ~/src/github.com/yukiyan/fluent-plugin-slack ✔  master ]
% ruby test/plugin/test_out_slack.rb
Loaded suite test/plugin/test_out_slack
Started
...........................

Finished in 8.125392 seconds.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
27 tests, 68 assertions, 0 failures, 0 errors, 0 pendings, 0 omissions, 0 notifications
100% passed
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3.32 tests/s, 8.37 assertions/s
```


### テストケースを表示させながら実行
`-v`をつける。

```
😀  [wakayama ♟  ~/src/github.com/yukiyan/fluent-plugin-slack ✔  master ]
% ruby test/plugin/test_out_slack.rb -v
Loaded suite test/plugin/test_out_slack
Started
SlackOutputTest:
  test_auto_channels_create_configure:																							.: (0.055684)
  test_buffer_configure:																								.: (0.002433)
  test_channel_keys:																									.: (0.533932)
  test_color_payload:																									.: (0.540157)
  test_configure:																									.: (0.002970)
  test_default_incoming_webhook:																							.: (0.537573)
  test_default_slack_api:																								.: (0.540416)
  test_default_slackbot:																								.: (0.535278)
  test_https_proxy_configure:																								.: (0.001665)
  test_icon_configure:																									.: (0.002396)
  test_icon_emoji:																									.: (0.541300)
  test_icon_url:																									.: (0.540831)
  test_link_names:																									.: (0.540419)
  test_link_names_configure:																								.: (0.002146)
  test_message_keys:																									.: (0.534327)
  test_mrkdwn:																										.: (0.525824)
  test_mrkdwn_in:																									.: (0.535991)
  test_mrkwn_configure:																								.: (0.003611)
  test_old_config:																									.: (0.006391)
  test_parse:																										.: (0.534959)
  test_parse_configure:																								.: (0.002707)
  test_plain_payload:																									.: (0.537929)
  test_slack_configure:																								.: (0.002588)
  test_time_format_configure:																								.: (0.002324)
  test_timezone_configure:																								.: (0.004941)
  test_title_keys:																									.: (0.535615)
  test_title_payload:																									.: (0.530476)

Finished in 8.136757 seconds.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
27 tests, 68 assertions, 0 failures, 0 errors, 0 pendings, 0 omissions, 0 notifications
100% passed
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3.32 tests/s, 8.36 assertions/s
```


### テストケースを指定して実行
`-n`をつける。

```
😀  [wakayama ♟  ~/src/github.com/yukiyan/fluent-plugin-slack ✔  master ]
% ruby test/plugin/test_out_slack.rb -v -n test_title_payload
Loaded suite test/plugin/test_out_slack
Started
SlackOutputTest:
  test_title_payload:																									.: (0.588766)

Finished in 0.589185 seconds.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1 tests, 0 assertions, 0 failures, 0 errors, 0 pendings, 0 omissions, 0 notifications
100% passed
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1.70 tests/s, 0.00 assertions/s
```

### binding.pryを埋め込みながらアレコレ確認する
```ruby
😀  [wakayama ♟  ~/src/github.com/yukiyan/fluent-plugin-slack ✘  master ]
% d
diff --git a/lib/fluent/plugin/out_slack.rb b/lib/fluent/plugin/out_slack.rb
index 7871650..b540bab 100644
--- a/lib/fluent/plugin/out_slack.rb
+++ b/lib/fluent/plugin/out_slack.rb
@@ -1,4 +1,5 @@
 require_relative 'slack_client'
+require 'pry'

 module Fluent
   class SlackOutput < Fluent::BufferedOutput
@@ -254,6 +255,7 @@ DESC
     def build_title_payloads(chunk)
       ch_fields = {}
       chunk.msgpack_each do |tag, time, record|
+        binding.pry
         channel = build_channel(record)
         per     = tag # title per tag
         ch_fields[channel]      ||= {}
😀  [wakayama ♟  ~/src/github.com/yukiyan/fluent-plugin-slack ✘  master ]
% ruby test/plugin/test_out_slack.rb -v -n test_title_payload
Loaded suite test/plugin/test_out_slack
Started
SlackOutputTest:
  test_title_payload:
From: /Users/wakayama/src/github.com/yukiyan/fluent-plugin-slack/lib/fluent/plugin/out_slack.rb @ line 258 Fluent::SlackOutput#build_title_payloads:

    255: def build_title_payloads(chunk)
    256:   ch_fields = {}
    257:   chunk.msgpack_each do |tag, time, record|
 => 258:     binding.pry
    259:     channel = build_channel(record)
    260:     per     = tag # title per tag
    261:     ch_fields[channel]      ||= {}
    262:     ch_fields[channel][per] ||= Field.new(build_title(record), '')
    263:     ch_fields[channel][per].value << "#{build_message(record)}\n"
    264:   end
    265:   ch_fields.map do |channel, fields|
    266:     {
    267:       channel: channel,
    268:       attachments: [{
    269:         :fallback => fields.values.map(&:title).join(' '), # fallback is the message shown on popup
    270:         :fields   => fields.values.map(&:to_h)
    271:       }.merge(common_attachment)],
    272:     }.merge(common_payload)
    273:   end
    274: end

[1] pry(#<Fluent::SlackOutput>)> chunk
=> #<Fluent::MemoryBufferChunk:0x007feeaaa2c2e0
 @data="\x93\xA4test\xCER\xC4\x8F\xE0\x83\xA7message\xA7sowawa1\xA4time\xA807:00:00\xA3tag\xA4test\x93\xA4test\xCER\xC4\x8F\xE0\x83\xA7message\xA7sowawa2\xA4time\xA807:00:00\xA3tag\xA4test",
 @key="",
 @mon_count=0,
 @mon_mutex=#<Mutex:0x007feeab3bfe60>,
 @mon_owner=nil,
 @unique_id="R\xC9\x16e\x18P\xE4\xB1\x0F \v\xF7d\xD3\xB2\xDD">
[2] pry(#<Fluent::SlackOutput>)> tag
=> "test"
[3] pry(#<Fluent::SlackOutput>)> time
=> 1388613600
[4] pry(#<Fluent::SlackOutput>)> record
=> {"message"=>"sowawa1", "time"=>"07:00:00", "tag"=>"test"}
[5] pry(#<Fluent::SlackOutput>)> build_channel(record)
=> "#channel"
[6] pry(#<Fluent::SlackOutput>)> exit!
```
