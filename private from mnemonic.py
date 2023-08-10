from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet as Cryptocurrency


with open('mnemonics.txt', 'r') as file:
    for line in file:
        MNEMONIC = line.strip()
        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=Cryptocurrency, account=0, change=False, address=0)
        bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=None, language='english')
        address = bip44_hdwallet.p2pkh_address()
        private = '0x' + bip44_hdwallet.private_key()

        with open('address;private;mnemonic.txt', 'a') as file_write:
            file_write.write(f'{address};{private};{MNEMONIC}\n')
