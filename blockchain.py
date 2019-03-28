# transaction: use dictionaries, do not care about the order
# list of transaction: list
# blockchain: list
# block: dictionaries
# managing the list of paticipants: use Sets so that we dont get any duplicate value

# Initiallizing our blockchain list
genesis_block = {
    'previous_hash': "",
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'John'


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_last_blockchain_value():
    """Returns the las value of the current blockchain."""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# This function accepts two arguments.
# One required one (transaction_amount) and one optional (last_transaction)
# The optional one it has a default value of [1]

def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain
    Arguments:
        :sender: The sender of the coin.
        :recipient: The recipient of the coin
        :amount: The amount of coins sent with the transaction (default=1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)

def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)
    block = {'previous_hash': "xyz",
             'index': len(blockchain),
             'transactions': open_transactions
            }
    blockchain.append(block)


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float."""
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)


def get_user_choice():
    """Prompts the user for its choice and return it."""
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    """ Outputs all blocks of the blockchain."""
    for block in blockchain:
        print("Outputting Block")
        print(block)
    else:
        print('-' * 20)
    
def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False if not"""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True

Waiting_for_input = True

while Waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Mine new block")
    print("3: Output the blocks")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add the transaction amount, recipient, sender to the blockchain
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) <= 1:
            blockchain[0] = {'previous_hash': "xyz",
                             'index': len(blockchain),
                             'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 232.0}]
                            }
    elif user_choice == 'q':
        Waiting_for_input = False
    else:
        print("Input was invalid, Please pick a value from the list!")
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid Blockchain!')
        break
else:
    print("User left!")

print("Done!")