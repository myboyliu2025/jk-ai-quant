# -*- coding: utf-8 -*-
"""
Tushare 同花顺资金流向采集脚本。

采集内容：
1. 个股资金流向：pro.moneyflow_ths
2. 同花顺行业资金流向：pro.moneyflow_ind_ths
3. 保存到 MySQL，使用项目根目录 .env 中的 WUCAI_SQL_* 数据库配置。

请在 .env 中配置：
TUSHARE_TOKEN=你的token
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from typing import List, Sequence