from typing import List
from caishen import CaishenSDK
from . import (
    CaishenCryptoGetBalanceTool,
    CaishenCryptoGetRPCTool,
    CaishenCryptoGetSupportedChainTypesTool,
    CaishenCryptoGetSwapRouteTool,
    CaishenCryptoSendTool,
    CaishenBalanceOtherTool,
    CaishenCryptoSwapTool,
    CaishenCashDepositTool,
    CaishenCashGetBalanceTool,
    CaishenCashGetSupportedTokensTool,
    CaishenCashSendTool,
    CaishenCashWithdrawTool
)

def create_agent_tools(sdk: CaishenSDK) -> List:
    return [
        CaishenCryptoGetBalanceTool(sdk),
        CaishenCryptoGetRPCTool(sdk),
        CaishenCryptoGetSupportedChainTypesTool(sdk),
        CaishenCryptoGetSwapRouteTool(sdk),
        CaishenCryptoSendTool(sdk),
        CaishenBalanceOtherTool(sdk),
        CaishenCryptoSwapTool(sdk),
        CaishenCashDepositTool(sdk),
        CaishenCashGetBalanceTool(sdk),
        CaishenCashGetSupportedTokensTool(sdk),
        CaishenCashSendTool(sdk),
        CaishenCashWithdrawTool(sdk),
    ]
