import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 682673597 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha=1-p
    size = x.size
    max = x.max()
    return max/((1-alpha/2)**(1./size)), \
           max/(alpha/2**(1./size))
