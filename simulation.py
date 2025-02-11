import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions: list, previous_hash, nonce=0):
        self.index = index  # Position of the block in the chain
        self.timestamp = time.time()  # Time when the block is created
        self.transactions = transactions  # List of transactions
        self.previous_hash = previous_hash  # Hash of the previous block
        self.nonce = nonce  # Number used for proof-of-work
        self.hash = self.compute_hash()  # Compute hash of the block

    def compute_hash(self):
        """Creates a SHA-256 hash of the block content."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)  # Convert block data to JSON string
        return hashlib.sha256(block_string.encode()).hexdigest()  # Return the SHA-256 hash

class Blockchain:
    def __init__(self, difficulty=2, max_pending_transactions=5):
        self.chain = []  # List to store the blockchain
        self.pending_transactions = []  # List to store unconfirmed transactions
        self.difficulty = difficulty  # Difficulty level for mining
        self.max_pending_transactions = max_pending_transactions  # Limit pending transactions
        self.create_genesis_block()  # Create the first block

    def create_genesis_block(self):
        """Creates the first block (genesis block) with index 0 and no transactions."""
        genesis_block = Block(0, [], "0")  # Genesis block has previous hash "0"
        self.chain.append(genesis_block)  # Add the genesis block to the chain

    def add_transaction(self, transaction):
        """Adds a new transaction to the list of pending transactions."""
        if len(self.pending_transactions) < self.max_pending_transactions:
            self.pending_transactions.append(transaction)
        else:
            print("Transaction pool is full. Please mine a block to clear space.")

    def mine_block(self):
        """Creates a new block from pending transactions and adds it to the blockchain."""
        if not self.pending_transactions:
            print("No transactions to mine.")
            return
        
        last_block = self.chain[-1]  # Get the last block in the chain
        new_block = Block(len(self.chain), self.pending_transactions, last_block.hash)  # Create a new block
        new_block = self.proof_of_work(new_block)  # Perform proof-of-work
        self.chain.append(new_block)  # Add the new block to the chain
        self.pending_transactions = []  # Reset pending transactions after mining

    def proof_of_work(self, block):
        """Implements an adaptive proof-of-work by finding a hash below a target value."""
        target = "0" * self.difficulty + "f" * (64 - self.difficulty)  # Adaptive difficulty mechanism
        while block.hash >= target:
            block.nonce += 1
            block.hash = block.compute_hash()
        return block

    def is_valid_chain(self):
        """Checks if the blockchain is valid by verifying hashes and links between blocks."""
        for i in range(1, len(self.chain)):
            prev_block = self.chain[i - 1]
            curr_block = self.chain[i]
            if curr_block.hash != curr_block.compute_hash():  # Compare stored hash instead of recomputing
                return False
            if curr_block.previous_hash != prev_block.hash:  # Check if previous hash matches actual hash of previous block
                return False
        return True

    def tamper_chain(self, index, new_transactions: list):
        """Tamper with a block by modifying its transactions and updating its hash, affecting subsequent blocks."""
        if 0 < index < len(self.chain):  # Ensure index is valid
            self.chain[index].transactions = new_transactions
            self.chain[index].hash = self.chain[index].compute_hash()  # Recompute hash after tampering
            for i in range(index + 1, len(self.chain)):
                self.chain[i].previous_hash = self.chain[i - 1].hash  # Update previous hash
                self.chain[i].hash = self.chain[i].compute_hash()  # Recompute hash

    def print_chain(self):
        """Prints the details of each block in the blockchain."""
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("-" * 40)

# Running the Blockchain Simulation
if __name__ == "__main__":
    my_blockchain = Blockchain()
    my_blockchain.add_transaction("Alice pays Bob 5 BTC")
    my_blockchain.add_transaction("Bob pays Charlie 3 BTC")
    my_blockchain.add_transaction("Charlie pays David 2 BTC")
    my_blockchain.add_transaction("David pays Eve 1 BTC")
    my_blockchain.add_transaction("Eve pays Frank 4 BTC")
    my_blockchain.add_transaction("Frank pays Grace 2 BTC")  # This should not be added due to transaction limit
    my_blockchain.mine_block()
    
    print("Blockchain before tampering:")
    my_blockchain.print_chain()
    
    my_blockchain.tamper_chain(1, ["Hacked Transaction"])
    
    print("Blockchain after tampering:")
    my_blockchain.print_chain()
    
    print("Is blockchain valid?", my_blockchain.is_valid_chain())
