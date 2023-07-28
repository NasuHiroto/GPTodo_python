# GPTodo
# GPTodoアプリケーション

GPTodoはChatGPTを使用して、入力されたやりたいことを解決するためのTodoリストを自動生成するWebアプリケーションです。このアプリケーションはDjangoフレームワークで作成されています。

## セットアップ手順

以下の手順に従って、GPTodoアプリケーションをローカル環境で動作させることができます。

### 1. 必要なソフトウェアのインストール

- Python 3.x
- Git

### 2. リポジトリのクローン

GitHubからリポジトリをクローンします。

```bash
git clone https://github.com/your-username/gptodo.git
cd gptodo
```

### 3. 仮想環境の作成とアクティベート

```bash
python -m venv venv
```
Windowsの場合:
```bash
.\venv\Scripts\Activate
```
macOS/Linuxの場合:
```bash
source venv/bin/activate
```

### 4. パッケージのインストール
```bash
pip install -r requirements.txt
```
### 5. データベースのマイグレーション
```bash
python manage.py migrate
```
### 6. アプリケーションの起動
```bash
python manage.py runserver
```
アプリケーションが起動したら、ブラウザで http://127.0.0.1:8000/ にアクセスしてGPTodoアプリを利用できます。
