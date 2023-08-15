import sys
import markdown

def markdown_to_html(inputfile, outputfile):
    try:
        # マークダウンファイルを読み込む
        with open(inputfile, 'r', encoding="utf-8") as md_file:
            md_content = md_file.read()

        # マークダウンをHTMLに変換
        html_content = markdown.markdown(md_content)

        # 全角のコロンを半角のコロンに置き換える
        html_content = html_content.replace('：', ':')

        # HTMLを出力ファイルに書き込む
        with open(outputfile, 'w', encoding="utf-8") as html_file:
            html_file.write(html_content)

        print(f"{inputfile} was successfully converted to {outputfile}!")

    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 file-converter.py markdown inputfile outputfile")
        return

    command = sys.argv[1]

    if command == "markdown":
        markdown_to_html(sys.argv[2], sys.argv[3])
    else:
        print("Invalid command!")

if __name__ == "__main__":
    main()
