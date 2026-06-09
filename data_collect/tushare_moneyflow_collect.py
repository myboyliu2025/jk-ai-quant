# -*- coding: utf-8 -*-
"""
Tushare 同花顺资金流向采集脚本。

功能：
1. 股票资金流向：pro.moneyflow_ths
   - 单日全部股票：--trade-date 20241011
   - 单股区间：--ts-code 002149.SZ --start-date 20241001 --end-date 20241011
2. 同花顺行业资金流向：pro.moneyflow_ind_ths
   - 单日全部行业：--trade-date 20240927
3. 自动保存到 MySQL：默认使用项目根目录 .env 里的 WUCAI_SQL_* 配置。

注意：
- 不要把 TUSHARE_TOKEN 写死到代码里，放到项目根目录 .env。
- 脚本会自动建表、自动补字段，并按唯一键做 upsert。
"""

from __future__ import annotations

import argparse
import os
