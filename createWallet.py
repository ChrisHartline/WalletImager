from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic
import random
import subprocess
import json
import os

def select_random_mnemonic_words(mnemonic, num_words):
    """
    Randomly select 'num_words' from the mnemonic phrase
    """
    words = mnemonic.split()
    if num_words > len(words):
        num_words = len(words)
    
    # Randomly select indices
    selected_indices = random.sample(range(len(words)), num_words)
    selected_words = [words[i] for i in selected_indices]
    
    return selected_words, selected_indices

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

# Select random number between 2 and 6
random_count = random.randint(2, 6)
print(f"Random count: {random_count}")

# Select random words from mnemonic
selected_words, selected_indices = select_random_mnemonic_words(mnemonic, random_count)

print(f"Mnemonic: {mnemonic}")
print(f"Selected {random_count} random words: {selected_words}")
print(f"Selected word positions: {[i+1 for i in selected_indices]}")  # +1 to show 1-based indexing
print(f"Private Key: {address.wif}")
print(f"Public Address: {address.address}")
print(f"Public Key: {address.key().public_hex}")

# Send wallet name and selected words to Story.py
print(f"\nGenerating story with wallet '{wallet_name}' and selected words...")
try:
    # Pass wallet name first, then selected words as command line arguments
    # Use sys.executable to ensure we're using the correct Python interpreter
    import sys
    result = subprocess.run([sys.executable, 'Story.py', wallet_name] + selected_words, 
                          capture_output=True, text=True, check=True)
    print("Story generated successfully!")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error generating story: {e}")
    print(f"Error output: {e.stderr}")
    print(f"Return code: {e.returncode}")
except FileNotFoundError:
    print("Error: Story.py file not found in current directory")
except Exception as e:
    print(f"Unexpected error: {e}")