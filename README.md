# Blockchain Simulation

## Introduction
This project is a simple blockchain simulation implemented in Python. It demonstrates the fundamental concepts of blockchain, including blocks, hashing, proof-of-work, and chain validation.

## Features
- Block structure with index, timestamp, transactions, previous hash, and proof-of-work
- SHA-256 hashing for secure block linking
- Proof-of-work mechanism for mining blocks
- Blockchain validation to detect tampering
- Transaction handling and block mining

## Prerequisites
Ensure you have the following installed:
- Python 3.6 or later

## Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: The project currently does not require any external dependencies.)*

## Usage
1. Run the blockchain simulation:
   ```bash
   python blockchain.py
   ```
2. The script will:
   - Create a blockchain
   - Add transactions and mine new blocks
   - Print the blockchain before and after tampering
   - Validate the blockchain

## Example Output
```
Blockchain before tampering:
Index: 0
Timestamp: 1698765432.123456
Transactions: []
Previous Hash: 0
Hash: abcdef123456...
----------------------------------------
Index: 1
Timestamp: 1698765435.789012
Transactions: ['Alice pays Bob 5 BTC']
Previous Hash: abcdef123456...
Hash: 789xyz987...
----------------------------------------
...
Blockchain after tampering:
...
Is blockchain valid? False
```

## Customization
- Modify the `difficulty` parameter in `Blockchain` to adjust proof-of-work difficulty.
- Add more transactions before mining new blocks.

## License
This project is open-source and available under the MIT License.

## Contact
For any issues, feel free to raise an issue or contribute to improvements.
