## DynamoDBとは
* フルマネージドなNoSQLデータベース

## DynamoDBを推す言い回し
* フルマネージドなサービスを使用することによる運用コストの低さ
* リソースのコントロールによるコストの最適化

## range keyについて
* DynamoDBはrange keyというキーでテーブルをソートすることが可能であり、時系列データ用のテーブルは時刻をrange keyとして保存しています。

## Write/Readについて
* 書き込み時
  * DynamoDBは3つのAZへ書き込みを行いますが、2つのAZへの書き込み完了確認がとれたら書き込み完了とみなします。
* 読み込み時(デフォルト)
  * 結果整合性の読み込みモデルとなっております。書き込みを行った直後に、読み込みを行った場合古いデータを返す可能性がります。
  * 結果整合性とは、結果的に整合性がとれてればよいという考え方でS3でも採用されています。即座にデータが反映されるのではなく、ある程度時間がたったら整合性がとれているというモデルになります。
* 読み込み時(Consistent Readオプションを指定)
  * 強力な整合性のある読み込みが可能となります(GetItem、Query、Scan)
  * Readするときに、Read前のWriteが全て反映されたレスポンスを保証
  * ただし、Capacity Unitを２倍消費

## 合わせて読みたい
* [Amazon DynamoDB ドキュメント | AWS](https://aws.amazon.com/jp/documentation/dynamodb/)
* [よくある質問 - Amazon DynamoDB | AWS](http://aws.amazon.com/jp/dynamodb/faqs/)
* [NoSQL とは | AWS](http://aws.amazon.com/jp/nosql/)
* [コンセプトから学ぶAmazon DynamoDB【Amazon RDSとの比較篇】 ｜ Developers.IO](http://dev.classmethod.jp/cloud/aws/amazon-dynamodb-comparison-with-rds/)
* [AWS再入門 Amazon DynamoDB 編 ｜ Developers.IO](http://dev.classmethod.jp/cloud/aws/cm-advent-calendar-2015-aws-re-entering-dynamodb/)
* [既存のコードをかえずにAdapterをかませることでMySQLからDynamoDBに移行したときの話 - Qiita](http://qiita.com/kentokento/items/9fbc73a4372e28696ba0)
* [DynamoDB ベストプラクティス - Qiita](http://qiita.com/inouet/items/bcf9467a65b27c362ecf)
* [DynamoDBを使ったKPI保存システム | GREE Engineers' Blog](http://labs.gree.jp/blog/2015/12/14582/)
* [DynamoDB での制限 - Amazon DynamoDB](http://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/Limits.html)
* [コンピュータでの DynamoDB の実行 - Amazon DynamoDB](http://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html)
* [ここにハマった！DynamoDB - Technology Topics by Brains](http://blog.brains-tech.co.jp/entry/2015/09/30/222148)
* [DynamoDBにおけるテーブル設計 - Qiita](http://qiita.com/naomichi-y/items/eb42491932b46821bb6c)
* [DynamoDBでのポイントまとめ - Qiita](http://qiita.com/yoskhdia/items/6897f66bdf93017ca033)
* [DynamoDBいくらかかるの？なにがいいの？RDBじゃだめなの？ - Qiita](http://qiita.com/daikissdd/items/d20449ecbd95bfcdb973)
