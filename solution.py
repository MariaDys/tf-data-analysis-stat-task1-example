import pandas as pd
import numpy as np


chat_id = 734920047 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    x_mean = np.mean(x)
    a = np.log(x).mean() - 0.5 * np.log(((np.log(x) - np.log(x_mean))**2).mean())
    return a
