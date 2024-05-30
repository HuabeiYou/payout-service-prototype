"""
业务场景:
    公司兼职老师的薪酬通常是每次上完课后按 (上课时长 * 老师的时薪) 结算，自动进入老师的可提现余额。
    有余额的老师可以自主发起提现申请，如果提现的是人民币，系统需要记录下来，由财务定期导出处理，
    其他币种都会发送请求到对接的出账平台，直接完成工资发放。

要完成的功能:
    1. 为用户添加可提现余额
    2. 用户发起提现，发送请求到第三方出账平台

可以假设:
    1. 用户的可提现余额(balance)和对应币种(currency)会储存在Wallet里(见wallet.py)。
    2. 新增或提现的具体金额(amount)，币种(currency)，和哪位用户(user_id)，都已经在其他地方判断好，
        使用PayoutService时会直接当作参数转入。
    3. 发给第三方平台的请求有失败的可能性，可以用send_payout_request模拟。
    4. 只是prototype所以不需要数据库，everything should be in memory.
    5. 不用考虑performance.
    6. 可以更改已有代码。

评判标准（按重要性排序）:
    1. 是否完成功能
    2. 是否能保持项目的代码风格
    3. 代码的可读性和可测试性
    4. Test cases
"""

import random

from wallet import Currency, WalletRepository


class PayoutService:
    def __init__(self):
        pass

    def send_payout_request(self, amount, currency, error_rate: float = 0.5):
        # error_rate > 1 就一定失败，< 0 就一定成功
        if random.random() < error_rate:
            raise Exception("Payout request failed")
        return amount, currency

    def add_funds(self, amount, currency, user_id):
        # 1. 为用户添加可提现余额
        pass

    def withdraw_funds(self, amount, currency, user_id):
        # 2. 用户发起提现，发送请求到第三方出账平台
        pass
