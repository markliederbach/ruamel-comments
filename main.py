import pathlib
from ruamel.yaml import YAML


def main():
    with open("test.yml", "r") as f:
        yaml = YAML()
        data = yaml.load(f)

    # Root level comment
    print(f"Comment 1: {repr(data.ca.comment[1][0].value)}")

    # Comments under a key, before items
    print(f"Comment 2: {repr(data['key2'].ca.comment[1][0].value)}")
    print(f"Comment 3: {repr(data['key2'].ca.comment[1][1].value)}")

    # Comments on EOL list items
    print(f"Comment 4: {repr(data['key2'].ca.items[1][0].value)}")

    # Comments below list items
    print(f"Comment 5: {repr(data['key2'].ca.items[2][0].value)}")

    # Comments on EOL dict key (Warning, this is counterintuitive)
    print(f"Comment 6: {repr(data['key3'].ca.comment[0].value)}")

    # Comments below dict key (Warning, this is counterintuitive)
    print(f"Comment 7: {repr(data['key3'].ca.items['subkey1'][2].value)}")

    # Comments below dict key, not indented
    print(f"Comment 8/9/10: {repr(data['key3'].ca.items['subkey2'][2].value)}")

    # Comments on EOL and below
    print(f"Comment 11/12: {repr(data.ca.items['key4'][2].value)}")


if __name__ == "__main__":
    main()
