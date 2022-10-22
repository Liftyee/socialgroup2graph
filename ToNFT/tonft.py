#program that makes an nft with polygon

def makeNFT(account_address, account_private_key, image_url):
    #import libraries
    from brownie import network, config, accounts, SimpleCollectible
    from metadata import sample_metadata
    import requests
    import json

    #load metadata
    metadata = sample_metadata.metadata_template
    metadata["image"] = image_url

    #get the most recent network
    network.connect("polygon-main-fork")
    #get the most recent account
    account = accounts.add(account_private_key)
    #create the collectible
    simple_collectible = SimpleCollectible[-1]
    #create a transaction
    transaction = simple_collectible.createCollectible(metadata, {"from": account})
    #wait for the transaction to be mined
    transaction.wait(1)
    #get the event
    event = simple_collectible[-1].events["createdCollectible"]
    #get the value of the event
    value = event["tokenId"]
    #get the transaction id
    transaction_id = event["transactionHash"].hex()
    #return the value
    return value, transaction_id

