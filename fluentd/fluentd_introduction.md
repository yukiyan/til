## fluentdでできること
ログを受け取ってパースして必要に応じて整形して届けたいところに届ける。
簡単に言うと、データのやり取りを管理する。なのでデータであればログ以外でも良い。
異常時の再送処理もリトライ機構・バッファ機構が整っていて安心。

## インストール方法
curlで取ってきて、デーモン起動するだけ。
[Installing Fluentd Using rpm Package | Fluentd](http://docs.fluentd.org/articles/install-by-rpm#step-1-install-from-rpm-repository) に詳しい説明が書いてあるので簡単にインストールできるはず。
td-agent.confをerbにすると割と便利なのでchefで入れると良いかもしれない。

## プラグインの種類
fluentdはプラガブルな設計になっている。
そのため、fluentdに組み込まれてるプラグインやOSSのプラグインを駆使してログを出し分けたりする。

* Inputプラグイン
  * ログの入力を受け持つ部分。データの流入を司るイメージ。
* Outputプラグイン
  * ログの出力を受け持つ部分。データの流出を司るイメージ。
* Bufferプラグイン
  * 異常時にログをバッファして、あとで再送するための機能を受け持つ部分。書き込みを適当なchunkにまとめて処理をしつつ書き込みに失敗したらリトライしてくれるイメージ。
* Filterプラグイン
  * 流入してくるログを書き換えたり、正規表現で絞り込んだりする部分。
* Parserプラグイン
  * ログのパースを受け持つ部分。Inputプラグインではさばけないような構造化されてないフォーマットのログに対応できるようになるイメージ。
* Formatterプラグイン
  * ログの出力形式を変更できる機能を受け持つ部分。流入してきたログをltsv形式等にして流出できるイメージ。

## ログの流れ
基本的には、
Input → (fluentd内部での処理) → Filter → Output
の流れに沿ってログを処理していく。
場合に応じて、Buffer・Parser・Formatterプラグインを活用する。

## 設定ファイル
td-agent.confを書いてログの出し分け方法を定義する。
