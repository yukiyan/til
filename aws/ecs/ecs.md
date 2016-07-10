## ECSとは
* 高性能なコンテナ管理サービス
* 複数のEC2インスタンスを取りまとめて管理した上で、あらかじめ定めた通りにコンテナをグリグリ動かすためのマネージドサービス
* たくさんのサーバーを徘徊して docker run コマンドを実行する手間を省いてくれます。
* Amazon ECS の管理下で新たにコンテナを走らせようとすると、まずは Amazon ECS は取りまとめて管理している ECS インスタンスの中で空いている場所を探してそこでコンテナを走らせようとします。
* コンテナがどこで動いているかを考えずに Docker コンテナのクラスタを構成/管理できる

## 競合
### フルマネージドサービス
* [GKE](https://cloud.google.com/container-engine/?hl=ja)

### 自前運用
* [Docker Swarm](https://docs.docker.com/swarm/)
* [Kubernetes](http://kubernetes.io/)

## 用語
* [What is Amazon EC2 Container Service? - Amazon EC2 Container Service](http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/Welcome.html)

## 使い始めによく困ること
* [Amazon ECS に途中で挫折しないために | ORIH](http://orih.io/2015/12/a-few-things-i-wanted-to-know-before-playing-with-amazon-ecs/)

## CircleCIとECRの親和性
* [CircleCI + AWS ECR/ECS | The CircleCI Blog](http://blog.circleci.com/circleci-aws-ecrecs/)

## 親和性の高いコンテナサービス
* [Container Partners - Amazon Web Services (AWS)](https://aws.amazon.com/jp/containers/partners/)

## 関連資料
* [Amazon EC2 Container Service(ECS)と戯れた1年とコンテナ芸人の来年について - tehepero note(・ω<)](http://stormcat.hatenablog.com/entry/2015/12/21/210000)
* [Rails アプリの Docker Image ビルドと Amazon EC2 Container Service へのデプロイの自動化 - Atsushi Nagase](https://ja.ngs.io/2015/09/14/ecs-docker-rails/)
* [EC2 Container Service(ECS)を管理して、Blue-Green Deploymentを実現するツールを書いた - tehepero note(・ω<)](http://blog.stormcat.io/entry/2015/07/22/130000)
* [production環境でRailsアプリをdockerコンテナとしてECSで運用するために考えたこと - Qiita](http://qiita.com/joker1007/items/b8a932c1ae29705cef8d)
* [Git プッシュから Amazon ECS に自動デプロイする仕組みを構築する | ORIH](http://orih.io/2015/12/run-automated-deployment-by-git-push-with-ecs-deploy-script/)
* [aws/amazon-ecs-cli: A custom Amazon ECS CLI that eases up the cluster setup process, enables users to run their applications locally or on ECS using the same Docker Compose file format and familiar Compose commands.](https://github.com/aws/amazon-ecs-cli)
* [Flexible Blue Green Deploymentのススメ｜サイバーエージェント 公式エンジニアブログ](http://ameblo.jp/principia-ca/entry-12071871177.html)
* [UbuntuでUpstartを使ってECS Agentをサービス化する - tehepero note(・ω<)](http://blog.stormcat.io/entry/2015/08/27/120000)
* [Docker+CoreOSを本番環境に乗せるためにやったこと | nanapi TechBlog](http://blog.nanapi.co.jp/tech/2015/04/10/nanapi_on_docker/)
