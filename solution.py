import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 682673597 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    size = x.size
    max = x.max()
    return max/(p**(1./size)), \
           max/((1-p)**(1./size))
