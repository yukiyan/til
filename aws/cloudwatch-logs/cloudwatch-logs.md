CloudWatch Logsについて
-------------------------
* 概要はこれ読めばわかる。[AWS Blackbelt 2015シリーズ Amazon CloudWatch & Amazon CloudWatch Logs](http://www.slideshare.net/AmazonWebServicesJapan/20150701-aws-blackbeltcloudwatch)
* CloudWatch Logsにとりあえずログを突っ込んで、好きなときにAPI叩いてフィルタする(又はマネジメントコンソールで見る)という用途で使うイメージで良いと思った。
* アラートやメトリクスまわりはmackerelでも良い。

>ログの転送というと、これまではFluentdを使うのが一般的でした。Fluentdを使えば、フィルタを通してElasticSearchやMongoDBにログを転送して検索できるようにしたりなど、いろいろ凝ったことが出来ます。しかし単に長期間保存だけできればよいという場合もあるので、そういったときはFluentdを通してログをS3に放り込むような使い方がお手軽でした。S3に入れておけばデータ保全も万全ですし、古いログを自動で削除したりGlacierに移したりといったことが簡単にできます。しかし、Fluentdを通してS3に転送したログは細切れになっており、閲覧性が最悪でした。
CloudWatch Logsでは、Fluentdと同じように、EC2にログエージェントをインストールします。インストールされたログエージェントは指定されたログを収集し、CloudWatchに転送します。CloudWatch LogsのログエージェントにはFluentdのような高度なフィルタの機能は無く、単にログを転送するだけです。
しかしログ閲覧のUIにはCloudWatchのマネジメントコンソールが使えますので、S3に入れるよりは便利になります。また、特定文字列を検知してアラートを上げることなども可能です。
>>[CloudWatch Logs | インフラ関係のメモ書き](http://rikuga.me/tag/cloudwatch-logs/)


用語
---------------------
用語引用元: [Amazon Web Services ブログ: 【AWS発表】Amazon CloudWatchによるOSやログファイルの蓄積とモニタリング機能の提供](http://aws.typepad.com/aws_japan/2014/07/cloudwatch-log-service.html)

* Log Event
  * モニターされるアプリケーションやリソースが記録したアクティビティです。タイムスタンプとUTF-8でフォーマットされたメッセージで構成されます。
  * アプリのログを送る。
* Log Stream
  * Log Streamは、同じデータ発生元（特定のアプリケーションが動作するインスタンスやリソース）からのLog Eventのシーケンスです。
* Log Group
  * Log Groupは、同じプロパティ、ポリシやアクセスコントロールを共有するLog Streamのグループです。

![](http://image.slidesharecdn.com/20150701aws-blackbelt-cloudwatch-150702064220-lva1-app6892/95/aws-blackbelt-2015-amazon-cloudwatch-amazon-cloudwatch-logs-28-638.jpg?cb=1435819913)
>画像引用元: [AWS Blackbelt 2015シリーズ Amazon CloudWatch & Amazon CloudWatch Logs](http://www.slideshare.net/AmazonWebServicesJapan/20150701-aws-blackbeltcloudwatch)


* Metric Filters
  * Metric Filters は、監視するメトリックスをCloudWatchに投入しメトリックスにするときに抽出する方法です。
  * mackerelのカスタムメトリクスで良いと思う。
* Retention Policies
  * Retention Policiesは、イベントの保持期間に関する定義をします。Log Groupに関連づけられ、グループ内の全てのLog Streamに適用されます。
* Log Agent
  * Log Agentは、EC2インスタンスにインストールし、直接CloudWatchにLog Eventを送信するエージェントです。このエージェントはAmazon Linux AMIとUbuntu AMIでテストされています。
  * [ryotarai/fluent-plugin-cloudwatch-logs: CloudWatch Logs Plugin for Fluentd](https://github.com/ryotarai/fluent-plugin-cloudwatch-logs)で送るからエージェントは入れなくていい。


Price
---------------
[料金 - AWS CloudWatch | AWS](http://aws.amazon.com/jp/cloudwatch/pricing/)

* $0.76 : 取り込み GB あたり
* $0.033 : GB あたりのアーカイブ/月
* CloudWatch ログのデータ転送送信（アウト） はEC2 料金表ページに掲載されている "Amazon EC2 からのデータ転送送信（アウト）" および "Amazon EC2 からインターネットへのデータ転送送信（アウト）" と同じ料金です。


refs
----------------
* [ログファイルのモニタリング - Amazon CloudWatch](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.html)
* [logs — AWS CLI 1.10.1 Command Reference](http://docs.aws.amazon.com/cli/latest/reference/logs/index.html)
* [Amazon CloudWatch Logs logging driver](https://docs.docker.com/engine/admin/logging/awslogs/)
* [ryotarai/fluent-plugin-cloudwatch-logs: CloudWatch Logs Plugin for Fluentd](https://github.com/ryotarai/fluent-plugin-cloudwatch-logs)
