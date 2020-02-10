import argparse
import logging
from myapp.core import do_something, do_anything


def main():
    parser = argparse.ArgumentParser(
        description="""
    コマンドパラメータを扱うサンプルです。
    """
    )

    parser.add_argument("-t", "--test", help="何か文字列を指定")
    parser.add_argument("-m", "--mode", help="モードを指定します", choices=["mode1", "mode2"])
    parser.add_argument("-d", "--debug", help="デバッグログ出力をONにします", action="store_true")

    args = parser.parse_args()

    # log設定
    formatter = "%(asctime)s : %(levelname)s : %(message)s"
    if args.debug:
        # ログレベルを DEBUG に変更
        logging.basicConfig(level=logging.DEBUG, format=formatter)
    else:
        logging.basicConfig(format=formatter)

    if args.mode == "mode1":
        do_something(args.test)
    elif args.mode == "mode2":
        do_anything(args.test)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
