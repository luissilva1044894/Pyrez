import pyrez

fake_dev_id=1004
fake_auth_key='23DF3C7E9BD14D84BF892AD206B6755C'

def standard():
    paladins = pyrez.PaladinsAPI(fake_dev_id, fake_auth_key)
    print(paladins.getDataUsed())
    paladins.close()

def context_manager():
    """Context manager"""
    with pyrez.SmiteAPI(fake_dev_id, fake_auth_key) as smite:
        print(smite.getDataUsed())

def main():
    standard()
    context_manager()

if __name__ == '__main__':
    main()
