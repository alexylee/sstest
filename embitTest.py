from embit import bip39, bip32

mnem = "absorb artist mirror lunar become season daughter father health various outer cruise";

binaryseed = bip39.mnemonic_to_seed(mnem)
root = bip32.HDKey.from_seed(binaryseed)

xpub = root.derive("m/84h/0h/0h").to_public()
print(xpub)
