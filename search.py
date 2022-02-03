import pathlib
import requests
import argparse
import pprint

def get_words(nletters=5):
    words_file = pathlib.Path("words_alpha.txt")
    if not words_file.exists():
        words_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
        words_file.write_text(requests.get(words_url).text)
    return list(filter(
        lambda x: len(x) == nletters,
        words_file.read_text().split("\n")
    ))


if __name__ == "__main__":
    pair_lambda = lambda pair: (int(pair[0])-1, pair[1])

    parser = argparse.ArgumentParser()
    parser.add_argument("--contains", nargs="*", default=[])
    parser.add_argument("--notcontains", nargs="*", default=[])
    parser.add_argument("--at", nargs="*", default=[], type=pair_lambda)
    parser.add_argument("--notat", nargs="*", default=[], type=pair_lambda)
    args = parser.parse_args()

    words = get_words()

    print("Constraints")
    print("   Contains    : ", args.contains)
    print("   Not contains: ", args.notcontains)
    print("   At          : ", args.at)
    print("   Not at      : ", args.notat)

    # filter words using the constraings
    for c in args.contains:
        words = [w for w in words if c in w]
    for c in args.notcontains:
        words = [w for w in words if c not in w]
    for position, key in args.at:
        words = [w for w in words if w[position] == key]
    for position, key in args.notat:
        words = [w for w in words if w[position] != key]

    pprint.pprint(words)
    print(len(words))