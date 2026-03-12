import argparse

def main():

    parser = argparse.ArgumentParser(
    )
    parser.add_argument(
        "num",
        type=int,
        help="first argument"
    )
    parser.add_argument(
        "--optional", "-o",
        type=str,
        default="optional",
        help="optional string"
    )

    args=parser.parse_args()
    print(f"ran main({args})")

if __name__ =="__main__":
    main()