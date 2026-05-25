# Candlestick Chart
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

dates = [1, 2, 3, 4, 5]
open_  = [10, 12, 11, 13, 12]
close  = [12, 11, 13, 12, 14]
high   = [13, 13, 14, 14, 15]
low    = [ 9, 10, 10, 11, 11]

fig, ax = plt.subplots(figsize=(8, 6))

for i in range(len(dates)):
    color = 'green' if close[i] >= open_[i] else 'red'
    ax.plot([dates[i], dates[i]], [low[i], high[i]], color=color, linewidth=1.5)
    ax.add_patch(mpatches.Rectangle(
        (dates[i] - 0.2, min(open_[i], close[i])),
        0.4, abs(close[i] - open_[i]),
        color=color))

plt.title('Candlestick Chart')
plt.xlabel('Day')
plt.ylabel('Price ($)')
plt.show()
# green — price went up (close >= open)
# red   — price went down (close < open)
# wick  — thin line showing high/low range