なんか便利らしい。CentOS6から。CentOS7はsystemd。
Amazon linuxはsystemdではなくupstartを採用している。

upstart ってsysvinitに変わるサービス起動するマンがいて、そっち使うとpidファイルとかシェルスクリプト書かなくてもデーモン化できる。


```
[ec2-user@hogehoge ~]$ cat /etc/init/task_runner.conf
description "hogehoge"
author  "hoge<hoge@hoge.jp>"

start on runlevel [2345]
stop on runlevel [016]

chdir /opt
exec java -jar TaskRunner-1.0.jar --workerGroup=dp_workers --region=ap-northeast-1 --logUri=s3://hoge/hoge
respawn
```

て作って `sudo initctl start task_runner`  でデーモンになる。kill してもすぐ立ち上がる。

* [Upstart を使ってお手軽 daemon 化 - インフラエンジニアway - Powered by HEARTBEATS](http://heartbeats.jp/hbblog/2013/02/upstart-daemon.html)
* [Amazon Linuxでupstartを使ってmonitを止めない方法 ｜ Developers.IO](http://dev.classmethod.jp/cloud/amazon-linux-monit-non-kill/)
