import sys
from markdown_it import MarkdownIt

# コマンドラインの引数の数をチェック
if len(sys.argv) != 4:
	print("使用方法: python3 file-converter.py markdown inputfile outputfile")
	sys.exit(1)

# 引数を取得
command = sys.argv[1]
inputfile = sys.argv[2]
outputfile = sys.argv[3]

# コマンドがmarkdownかどうか確認
if command != "markdown":
	print("Unknwon command:", command)
	sys.exit(1)

# マークダウンファイルを読み込み、HTMLに変換
try:
	with open(inputfile, "r", encoding="utf-8") as infile:
		markdown_text = infile.read()
		md = MarkdownIt()
		html = md.render(markdown_text)

	# 変換したHTMLを出力ファイルに書き込み
	with open(outputfile, "w", encoding="utf-8") as outfile:
		outfile.write(html)
	
	print(f"Markdown has been successfully converted to HTML and saved to {outputfile}")

except FileNotFoundError:
	print(f"Error: The file {outputfile} was not found.")
	sys.exit(1)

except Exception as e:
	print(f"An error occurred: {e}")
	sys.exit(1)