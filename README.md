# Markdown_to_HTNL
このプログラムは。MarkdownテキストをHTMLに変換するプログラムです。  
仮想環境の構築や依存関係についての説明も含めています。  
なお、このプログラムはRecursionCSプログラムの一つです。

## 概要
このプログラムでは、指定したMarkdownファイルをHTMLファイルに変換します。

## 必要条件
・Python3.x  
・Linux環境では仮想環境の構築が推奨されます。  

## インストール方法
1. クローンリポジトリの作成
GitHubからリポジトリをクローンします。

```bash  
git clone https://github.com/your_username/your_repo_name.git
cd your-repo-name
```

2. 仮想環境の構築（Linux推奨）
Linux環境では、依存関係を他のプロジェクトやシステムに影響を与えないように、仮想環境を構築することが推奨されます。 

仮想環境の作成と有効化
```bash
# 仮想環境の作成  
python3 -m venv .venv

# 仮想環境の有効化
source .venv/bin/activate
```

仮想環境の無効化  
仮想環境を終了するには、以下のコマンドを実行します。  
```bash
deactivate
```

3. 依存パッケージのインストール  
reqirements.txtに必要なパッケージが記載されているので、以下のコマンドでインストールします。  
```bash
pip install -r requirements.txt
```

## 使用方法
プログラムを実行して、MarkdownファイルをHTMLに変換します。  
```bash
python3 file-converter.py markdown inputfile.md outputfile.html
```
・markdown: 実行するコマンド  
・inputfile.md: 入力するMarkdownファイルのパス  
・outputfile.html: 出力するHTMLファイルのパス  

## 注意事項
Linux環境で依存関係を管理するため、仮想環境を使用することを推奨します。  
依存パッケージはrequirements.txtに記録されているため、他の環境で再現する際には、このファイルを参照してください。
