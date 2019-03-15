# study_cloudfunctions

## 使うもの

- Cloud Functions
- Cloud Datastore

## やってみる

**gcloudコマンドをインストール**

```shell
curl https://sdk.cloud.google.com | bash
source ~/.bash_profile
which gcloud
```

**認証**

```shell
gcloud init
```

**componentをインストール**

```shell
gcloud components install beta
```

**バケットを作成**

※バケット名は世界で１つだけのにしないとダメ
```shell
gsutil mb gs://test-cloud-functions-xxx
```

**このリポジトリをclone**

```shell
git clone git@github.com:ikedanatsuko/study_cloudfunctions.git
cd study_cloudfunctions
```

**Hello World関数をCloud Functionsにデプロイ**

```shell
gcloud functions deploy hello --runtime python37 --trigger-http
```

**ブラウザのコンソール見てみるとCloudFunctions関数が追加されてる！**

https://console.cloud.google.com/functions/list

**実行してみる**

「トリガー」タブに表示されてるURLにアクセス、もしくは  
`gcloud functions call hello`  
で実行できる

**関数の確認**

```shell
gcloud functions list
gcloud functions logs read
```

**Datastoreにエンティティを追加**

https://console.cloud.google.com/datastore/entities

種類は「Todo」にする  
パラメータに「name」パラメータを登録

**Todo関数をデプロイ**

```shell
gcloud functions deploy add_todo --runtime python37 --trigger-http
gcloud functions deploy get_todo --runtime python37 --trigger-http
```

**Todo追加、取得してみる**
```shell
gcloud functions call add_todo --data='{"name": "todo1"}'
gcloud functions call get_todo
```

**Datastoreにデータが登録されてる！**

https://console.cloud.google.com/datastore/entities

**関数の削除**

```shell
gcloud functions delete 関数名
```

**バケット削除**

https://console.cloud.google.com/storage/browser
