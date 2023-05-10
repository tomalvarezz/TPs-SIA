import json
from src.utils import DataConfig, get_csv_data
from src.Kohonen import Kohonen

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)
        f.close()

    config = DataConfig(data)
    data, data_standarized, countries, labels = get_csv_data("europe.csv")

    print(data)
    print("---------------------------------------")
    print(data_standarized)
    print("---------------------------------------")
    print(countries)
    print("---------------------------------------")
    print(labels)

    kohonen = Kohonen(data_standarized, config.k, config.learning_rate,
                      config.radius, config.epochs)

if __name__ == "__main__":
    main()