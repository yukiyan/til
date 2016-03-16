## API
* [API Reference](http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/Welcome.html)
* [Module: Aws::DynamoDB — AWS SDK for Ruby V2](http://docs.aws.amazon.com/sdkforruby/api/Aws/DynamoDB.html)


## BatchGetItemやBatchWriteItemとは
* [BatchGetItem - Amazon DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html)
* [BatchWriteItem - Amazon DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html)


>Amazon DynamoDBが複数アイテム同時処理に対応しました。1つのアイテムを追加/削除したいならば、PutItem/DeleteItemを用いれば事足りるのですが、例えばElasticMapReduceによって大量のデータをDynamoDBにアップロードする等の場合に効果を発揮します。
* 1回のリクエストにまとめて追加/削除/置換を指示するため、スループットが向上する。
* サーバー側で同時に処理を行ってくれるため、クライアント側でスレッド処理を組む必要がない。
* PutItem/DeleteItemに比べて、追加/削除/置換の平均遅延が低い。

>BatchWriteItemには以下の制約があります
* 追加/削除/置換処理を1回に25個まで同時に処理できる。サイズ制限は全体で1MB。
* アイテムの追加/削除で用いることができるが、既存のアイテムの更新に用いることはできない。
* BatchWriteItem内で命令される個々の操作はアトミックであるが、BatchWriteItem自体はアトミックではない。要するに追加/削除など個々の操作の一部が失敗したとしても全体が取り消されることはない。もし、ネットワーク遅延やスループット制限により一部の操作が失敗した場合には、UnprocessedItemsとして戻り値が返されるので再処理などをすれば良い。
* アイテムを返さない。BatchWriteItemは大量のデータを効率的にアップロードするための仕組みである。DeleteItemはReturnValueを返すが、BatchWriteItemはPutItemやDeleteItemのように洗練されたAPIを持っていない。
* PutItemやDeleteItemとは異なり、BatchWriteItemは個々の操作内で書き込み時条件を指定することはできません。

>以下のような条件に1つでも当てはまる場合、DynamoDBはBatchWriteItem命令を拒否します。
* BatchWriteItem内で指定されたテーブルが存在しないとき。
* 指定された主キーが、対応するテーブルの主キーのスキーマに合致しないとき。
* 同じアイテムに対して追加や削除を行うとき。
* リクエストの合計サイズが1MBを超えているとき。
>>[Amazon DynamoDBがBatchWriteItemに対応しました ｜ Developers.IO](http://dev.classmethod.jp/cloud/amazon-dynamodb-batch-write-items/)

こんな感じでデータは簡単に取れた。
```ruby
client = Aws::DynamoDB::Client.new
resp = client.get_item({
  table_name: "awesome_table",
  key: {
    "my_id": "001",
    "date": "2016-03-16T04:00:30.860+09:00",
  },
})

=> #<struct Aws::DynamoDB::Types::GetItemOutput item={"my_id"=>"001", "file_name"=>"hoge.csv", "size"=>"12345", "date"=>"2016-03-16T04:00:30.860+09:00"}, consumed_capacity=nil>
```


あとクエリ投げるときは予約語と被るとダメ。置換が必要だった。置換の方法は調査中。

```ruby
resp = client.query({
   table_name: "awesome_table",
   select: "ALL_ATTRIBUTES",
   key_condition_expression: "my_id = :my_id and date <= :date",
   expression_attribute_values: {
     ":my_id": "001",
     ":date": "2016-03-16T04:00:30.860+09:00",
   },
})

# => Aws::DynamoDB::Errors::ValidationException: Invalid KeyConditionExpression: Attribute name is a reserved keyword; reserved keyword: date
```

* [DynamoDB の予約語 - Amazon DynamoDB](https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/ReservedWords.html)
* [DynamoDBで予約語を使う時は置換しないと怒られる - Qiita](http://qiita.com/kei-sato/items/2b7ae81e757f409fde21)

`ProjectionExpression`は何書けばいいかまだ理解してない。
