import json

import yaml



def main():
    with open("data/exex/data.yml") as f:
        data = list(yaml.load_all(f, Loader=yaml.SafeLoader))
    data = sorted(data, key=lambda x: x['authors'][0]['name'])

    with open("data/index.json", "w") as f:
        json.dump(data, f)
        

if __name__ == "__main__":
    main()
