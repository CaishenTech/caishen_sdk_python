from typing import TypedDict, Optional

class SendTransactionParams(TypedDict):
    toAddress: str
    amount: str
    account: int

class DepositCashParams(TypedDict):
    amount: str
    account: str
    tokenAddress: int
    chainId: int

class WithdrawCashParams(TypedDict):
    amount: str
    account: str
    tokenAddress: int
    chainId: int

class Token(TypedDict):
    address: str
    chainId: int
    decimals: int
    name: str
    symbol: str

class BalanceResponse(TypedDict):
    success: bool
    balance: str
    balanceRaw: str

class TransactionResponse(TypedDict):
    success: bool
    balance: str
    balanceRaw: str

class TransactionResponse(TypedDict, total=False):
    success: bool
    message: Optional[str]
    txHash: Optional[str]
    isSuccess: Optional[bool]