from typing import Type

class ToolBase:
    # Define the ToolBase class as the base class
    pass

class Tools:
    cash_get_balance: Type[ToolBase]
    cash_deposit: Type[ToolBase]
    cash_send: Type[ToolBase]
    cash_withdraw: Type[ToolBase]
    crypto_get_balance: Type[ToolBase]
    send_crypto: Type[ToolBase]
    swap_crypto: Type[ToolBase]
    crypto_get_swap_route: Type[ToolBase]
