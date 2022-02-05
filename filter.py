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
    pair_lambda = lambda pair: (int(pair[:-1])-1, pair[-1])

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--contain", nargs="*", default=[],
        help="filter words that contain given alphabets"
    )
    parser.add_argument(
        "--notcontain", nargs="*", default=[],
        help="filter words that do NOT contain given alphabets"
    )
    parser.add_argument(
        "--at", nargs="*", default=[], type=pair_lambda,
        help="filter words that have a letter at given place"
    )
    parser.add_argument(
        "--notat", nargs="*", default=[], type=pair_lambda,
        help="filter words that DO NOT have a letter at given place"
    )
    parser.add_argument(
        "--nletters", default=5, type=int,
        help="filter words that have given length"
    )
    args = parser.parse_args()

    words = get_words(args.nletters)

    print(f"""Constraints
    Contain    : {args.contain}
    Not contain: {args.notcontain}
    At         : {args.at}  (zero-based)
    Not at     : {args.notat} (zero-based)
    """)

    # filter words using the constraings
    for c in args.contain:
        words = [w for w in words if c in w]
    for c in args.notcontain:
        words = [w for w in words if c not in w]
    for position, key in args.at:
        words = [w for w in words if w[position] == key]
    for position, key in args.notat:
        words = [w for w in words if w[position] != key]

    pprint.pprint(words)
    print("The number of found words:", len(words))