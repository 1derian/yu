import argparse
import textwrap


def main(file):
    d = {}
    with open(file, mode="r", encoding="utf-8") as f:
        for line in f:
            ip_c, n = line.strip().rsplit(".", 1)
            if ip_c not in d:
                d[f"{ip_c}"] = [n]
            else:
                d[f"{ip_c}"].append(n)
    k_list = sorted(d, key=lambda k: len(d[k]), reverse=True)
    print(f"{file} c段信息如下:")
    for k in k_list:
        msg = f"{k}.1/24 {d[k]} {len(d[k])}"
        print(msg)


if __name__ == '__main__':
    banner = """
                  ___    ___ ___  ___     
                 |\  \  /  /|\  \|\  \    
                 \ \  \/  / | \  \\ \  \   
                  \ \    / / \ \  \\ \  \  
                   \/   / /   \ \  \\ \  \ 
                 __/   / /     \ \_______\\
                |\____/ /       \|_______|
                \|____|/                   
                                        author:derian
                                        version:0.0.1"""
    print(banner)
    parser = argparse.ArgumentParser(description='yu is clean ip tool',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''example:
        python3 yu.py -f ip.txt
        '''))
    parser.add_argument("-f", "--file",dest="file",type=str, help="input a file path", default="ip.txt")
    args = parser.parse_args()

    main(args.file)
