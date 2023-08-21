"""Bridge USDT from Polygon, Arbitrum or BSD to Aptos using Aptos Bridge"""

import random

from src import aptos_bridge, sleeping


# In seconds
SLEEP_FROM = 100
SLEEP_TO   = 200

# All values in USDT
AMOUNT_FROM = 0.1
AMOUNT_TO   = 0.3

RANDOM_WALLETS     = True  # Shuffle wallets
WALLETS_PATH       = "data/wallets.txt"  # Path for file with private keys
APTOS_WALLETS_PATH = "data/aptos_wallets.txt"  # Path for file with Aptos addresses


if __name__ == "__main__":
    response = int(input('''
Module:
1. Bridge from Polygon  to Aptos
2. Bridge from Arbitrum to Aptos
3. Bridge from BSC      to Aptos

Choose module: '''))

    with open(WALLETS_PATH, "r") as f:
        wallets = [row.strip() for row in f]

    with open(APTOS_WALLETS_PATH, "r") as f:
        aptos_wallets = [row.strip() for row in f]

    aptos_wallets_dict  = dict(zip(wallets, aptos_wallets))

    if RANDOM_WALLETS:
        random.shuffle(wallets)

    for i, wallet in enumerate(wallets):
        if response == 1:
            aptos_bridge(
                name=str(i),
                private_key=wallet,
                from_chain="Polygon",
                wallet=aptos_wallets_dict[wallet],
                amount=random.uniform(AMOUNT_FROM, AMOUNT_TO),
                max_gas=0.1,   # ~0.1$ for Polygon fees
                max_value=1.5  # ~0.9$ for Layer0 fees
            )
        elif response == 2:
            aptos_bridge(
                name=str(i),
                private_key=wallet,
                from_chain="Arbitrum",
                wallet=aptos_wallets_dict[wallet],
                amount=random.uniform(AMOUNT_FROM, AMOUNT_TO),
                max_gas=0.00023,  # ~0.4$ for Arbitrum fees
                max_value=0.0007  # ~1.2$ for Layer0 fees
            )
        elif response == 3:
            aptos_bridge(
                name=str(i),
                private_key=wallet,
                from_chain="BSC",
                wallet=aptos_wallets_dict[wallet],
                amount=random.uniform(AMOUNT_FROM, AMOUNT_TO),
                max_gas=0.0014,   # ~0.3$ for BSC fees
                max_value=0.0046  # ~1.1$ for Layer0 fees
            )
        else:
            raise NotImplementedError

        sleeping(SLEEP_FROM, SLEEP_TO)
