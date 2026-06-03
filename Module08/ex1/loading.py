#!/usr/bin/env python3

try:
    from typing import List, Dict
    from importlib.metadata import distributions, version
    import requests
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as err:
    print(f"Missing dependency: {err}")
    print("Install packages and run it again.\nUsing pip:\n"
          "\tpip install -r requirements.txt\n\tpython3 loading.py\n"
          "Using Poetry:\n\tpoetry install\n\tpoetry run python loading.py")
    exit(1)


RESTAPI: str = "https://restcountries.com/v3.1/"


def print_dependencies() -> None:
    print("Checking dependencies:")
    print(f"[OK] pandas ({version("pandas")}) - Data manipulation ready")
    print(f"[OK] requests ({version("requests")}) - Network access ready")
    print(f"[OK] matplotlib ({version("matplotlib")}) - Visualization ready")
    print(f"[OK] numpy ({version("numpy")}) - Numerical computation ready\n")


def get_sub_region(region: str) -> List[Dict]:
    region_data = requests.get(RESTAPI + "subregion/" + region, timeout=10)
    region_data.raise_for_status()
    return region_data.json()


def print_sub_region_data(region: List[Dict]) -> None:
    try:
        for country in region:
            print(f"{country["name"]["common"]} {country["flag"]}"
                  f"\n\tArea: {country["area"]}km"
                  f"\n\tPopulation: {country["population"]}"
                  "\n\tCapital: "
                  f"{', '.join(city for city in country["capital"])}"
                  "\n\tTimezones: "
                  f"{', '.join(zone for zone in country["timezones"])}"
                  "\n\tCurrencies: "
                  f"{', '.join(str(curr) for curr in country["currencies"])}"
                  "\n")
    except Exception as err:
        raise Exception(f"Printing region data: {err}")


if __name__ == "__main__":
    try:
        print("LOADING STATUS: Loading programs...\n")
        print_dependencies()
        try:
            df = pd.DataFrame([{
                "name": country["name"]["common"],
                "population": country["population"],
                "area": country["area"],
                "timezones": country["timezones"],
                "currencies": country["currencies"]
            } for country in get_sub_region("Northern Europe")
            ])
        except Exception as err:
            raise Exception(f"Creating data frame: {err}")

        names = df["name"].to_list()
        population = df["population"].to_numpy()
        area = df["area"].to_numpy()
        timezones = (df.explode("timezones")["timezones"]
                     .value_counts().sort_index()
                     )
        currencies = (df.explode("currencies")["currencies"]
                      .value_counts().sort_index()
                      )

        fig, axes = plt.subplots(2, 2, figsize=(25, 12))

        print("Processing data")
        axes[0, 0].bar(names, population // 1000, width=0.9)
        axes[0, 0].tick_params(axis='x', rotation=45)
        for label in axes[0, 0].get_xticklabels():
            label.set_ha('right')
        axes[0, 0].set_title("Population")

        axes[0, 1].bar(timezones.index, timezones.values, width=0.9)
        axes[0, 1].tick_params(axis='x', rotation=45)
        for label in axes[0, 1].get_xticklabels():
            label.set_ha('right')
        axes[0, 1].set_title("Timezones")

        axes[1, 0].bar(names, area, width=0.9)
        axes[1, 0].tick_params(axis='x', rotation=45)
        for label in axes[1, 0].get_xticklabels():
            label.set_ha('right')
        axes[1, 0].set_title("Area")

        axes[1, 1].bar(currencies.index, currencies.values, width=0.9)
        axes[1, 1].tick_params(axis='x', rotation=45)
        for label in axes[1, 1].get_xticklabels():
            label.set_ha('right')
        axes[1, 1].set_title("Currencies")

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
