# Overview

This repo allows you to bridge USDT from Polygon, Arbitrum and BSC to Aptos using Aptos Bridge from LayerZero for multiple wallets.

# Instructions

1. Make sure to have python, pip and git installed.

2. Clone this repo:
```sh
git clone https://github.com/VolodymyrVozniak/layer0-aptos-bridge.git
```

3. Go to a directory:
```sh
cd layer0-aptos-bridge
```

4. Add your private keys to `data/wallets.txt` (paste private keys, each from the new line, press Ctrl+O, Enter and Ctrl+X):
```sh
nano data/wallets.txt
```

5. Add your Aptos addresses to `data/aptos_wallets.txt` (paste public addresses, each from the new line, press Ctrl+O, Enter and Ctrl+X):
```sh
nano data/aptos_wallets.txt
```

6. Create virtual environment (can skip this step):
```sh
python -m venv env
```

7. Activate virtual environment (must run every time you connect to a server):
```sh
source env/bin/activate
```

8. Install python requirements (install only once):
```sh
pip install -r requirements.txt
```

9. Run the script to use Aptos Bridge:
```sh
python main.py
```

9. You can modify the following parameters in `main.py`:
    * `SLEEP_FROM`: The lowest value to sleep between wallets in seconds;
    * `SLEEP_TO`: The highest value to sleep between wallets in seconds;
    * `AMOUNT_FROM`: The lowest value to bridge in USDT;
    * `AMOUNT_TO`: The highest value to bridge in USDT;
    * `RANDOM_WALLETS`: Rather to shuffle wallets;
    * `WALLETS_PATH`: Path for file with private keys (each private key from new line).
    * `APTOS_WALLETS_PATH`: Path for file with Aptos public addresses (each address from new line).

-----

</br>
</br>

This repo was created for "STD" group.

Donation: `0x34Ec371BA620e6C67A115a6794D44FED038Cc78C`
