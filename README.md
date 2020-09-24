# 最初の設定
1. docker-compose.yamlをプロジェクト用に編集


## Development環境
### データベース
- DockerでMySQLを起動
```
docker-compose.yamlのmysql以外をコメントアウト
$ docker-compose.yaml up -d
```
- 接続確認
```
$ mysql -u root -p -P 4306 --host 127.0.0.1
```
### バックエンド
- ライブラリインストール
```
$ pipenv --python 3.7
$ pipenv install
```
- DB作成
```
$ pipenv run makemigrations
$ pipenv run migrate
$ pipenv run server
```

### フロントエンド
ライブラリインストール
```
$ npm install
$ npm run serve
```


## Production環境
- 未定
