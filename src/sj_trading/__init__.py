import os

import shioaji as sj
from dotenv import load_dotenv

from .quote import QuoteManager

load_dotenv()


def hello() -> None:
    print("Hello from sj-trading!")


def show_version() -> str:
    print(f"Shioaji Version: {sj.__version__}")
    return sj.__version__


def get_shioaji_client() -> sj.Shioaji:
    api = sj.Shioaji()
    print("Shioaji API created")
    return api


def get_api(simulation: bool = True) -> sj.Shioaji:
    api = sj.Shioaji(simulation=simulation)
    api.login(
        api_key=os.environ["API_KEY"],
        secret_key=os.environ["SECRET_KEY"],
    )
    api.activate_ca(
        ca_path=os.environ["CA_CERT_PATH"],
        ca_passwd=os.environ["CA_PASSWORD"],
    )
    return api


def main():
    api = get_api(simulation=True)
    quote = QuoteManager(api)
    quote.subscribe_stk_tick(["2330"])


if __name__ == "__main__":
    main()
