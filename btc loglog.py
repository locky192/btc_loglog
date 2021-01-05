import quandl
import matplotlib.pyplot as plt


price = quandl.get("BCHAIN/MKPRU", authtoken="dRsdc8njMS4QHeKqoJy-").values.tolist()

plt.plot(price)
plt.yscale("log")
plt.xscale("log")
plt.xlim(500, None)
plt.show()
