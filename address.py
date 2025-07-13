from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic

# Get wallet name from user input
wallet_name = input("Enter wallet name: ")

# Create a new wallet with a random mnemonic
mnemonic = Mnemonic().generate()
wallet = Wallet.create(
    name=wallet_name,
    keys=mnemonic,
    network='testnet'
    #network='bitcoin'
)

# Get the first address
address = wallet.get_key()
print(f"Mnemonic: {mnemonic}")
print(f"Private Key: {address.wif}")
print(f"Public Address: {address.address}")
print(f"Public Key: {address.key().public_hex}")


