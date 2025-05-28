from eth_account import Account
import secrets

# Nonaktifkan key warning
Account.enable_unaudited_hdwallet_features()

# Generate private key
private_key = "0x" + secrets.token_hex(32)

# Buat wallet dari private key
acct = Account.from_key(private_key)

print("🔐 Private Key:", private_key)
print("📬 Ethereum Address:", acct.address)
