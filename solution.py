import pandas as pd
import numpy as np


chat_id = 734920047 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    def solution(x: np.array) -> float:
    mu = np.mean(np.log(x) - np.log(647))
    s2 = np.var(np.log(x) - np.log(647))
    a = np.exp(mu - s2/2)
    return a
