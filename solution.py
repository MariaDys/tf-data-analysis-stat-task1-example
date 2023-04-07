import pandas as pd
import numpy as np


chat_id = 734920047 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    return np.average(np.log(x - 647))

