from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    # account = accounts.load("codeAccount")
    # account = accounts.add(config["wallets"]["from_key"])
    # account = accounts[0]
    account = get_account()
    print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    uodated_stored_value = simple_storage.retrieve()
    print(uodated_stored_value)


def get_account():
    if network.show_active() == "theta-privatenet":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
