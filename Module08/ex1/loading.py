#!/usr/bin/env python3

try:
    from typing import List, Dict
    from importlib.metadata import version
    import requests  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
except ImportError as err:
    print(f"Missing dependency: {err}")
    print("Install packages and run it again.\nUsing pip:\n"
          "\tpip install -r requirements.txt\n\tpython3 loading.py\n"
          "Using Poetry:\n\tpoetry install\n\tpoetry run python loading.py")
    exit(1)


RESTAPI: str = "https://api.restcountries.com/countries/v5"
APIKEY: str = ""


def print_dependencies() -> None:
    try:
        print("Checking dependencies:")
        print(f"[OK] pandas ({version('pandas')}) - Data manipulation ready")
        print(f"[OK] requests ({version('requests')}) - Network access ready")
        print(f"[OK] matplotlib ({version('matplotlib')})"
              " - Visualization ready")
        print(f"[OK] numpy ({version('numpy')})"
              " - Numerical computation ready\n")
    except Exception:
        raise Exception()


def get_region(region: str) -> Dict:
    if APIKEY == "":
        raise Exception("Err: No API KEY provided")
    try:
        region_data = requests.get(
            RESTAPI + "?region=" + region,
            headers={'Authorization': 
                     'Bearer ' + APIKEY}
            )
        region_data.raise_for_status()
        return region_data.json()
    except Exception as err:
        raise Exception(f"Requesting from API: {err}")


if __name__ == "__main__":
    try:
        print("LOADING STATUS: Loading programs...\n")
        print_dependencies()
        region: List = get_region("europe")["data"]["objects"]
        try:
            df = pd.DataFrame([{
                "name": country["names"]["common"],
                "population": country["population"],
                "area": country["area"]["kilometers"],
                "timezones": country["timezones"],
                "currencies": country["currencies"]
            } for country in region
            ])
        except Exception as err:
            raise Exception(f"Creating data frame: {err}")
        try:
            names = df["name"].to_list()
            population = df["population"].to_numpy()
            area = df["area"].to_numpy()
            timezones = (df.explode("timezones")["timezones"]
                        .value_counts().sort_index()
                        )
            currencies = (df.explode("currencies")["currencies"].str["code"]
                        .value_counts().sort_index()
            )
        except Exception as err:
            raise Exception(f"Transforming data: {err}")

        fig, axes = plt.subplots(2, 2, figsize=(25, 12))

        print("Processing data...")
        axes[0, 0].bar(names, population // 1000, width=0.9)
        axes[0, 0].tick_params(axis='x', rotation=45)
        for label in axes[0, 0].get_xticklabels():
            label.set_ha('right')
        axes[0, 0].set_title("Population (thousands)")
        print("\tpopulation ✅")

        axes[0, 1].bar(timezones.index, timezones.values, width=0.9)
        axes[0, 1].tick_params(axis='x', rotation=45)
        for label in axes[0, 1].get_xticklabels():
            label.set_ha('right')
        axes[0, 1].set_title("Timezones")
        print("\tTimezones ✅")

        axes[1, 0].bar(names, area, width=0.9)
        axes[1, 0].tick_params(axis='x', rotation=45)
        for label in axes[1, 0].get_xticklabels():
            label.set_ha('right')
        axes[1, 0].set_title("Area (km)")
        print("\tArea ✅")

        axes[1, 1].bar(currencies.index, currencies.values, width=0.9)
        axes[1, 1].tick_params(axis='x', rotation=45)
        for label in axes[1, 1].get_xticklabels():
            label.set_ha('right')
        axes[1, 1].set_title("Currencies")
        print("\tCurrencies ✅")

        plt.subplots_adjust(
            left=0.1,
            right=0.96,
            top=0.9,
            bottom=0.25,
            wspace=0.3,
            hspace=0.68
            )
        print("Generating visualization...")
        plt.savefig("matrix_analysis.png", bbox_inches="tight")

        print("Analysis complete!\nResults saved to: matrix_analysis.png")
    except Exception as err:
        print(err)
