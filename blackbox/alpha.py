from blackbox.broker import Oanda
import random


class AlphaModel(object):
    """ The alpha model is designed to predict the future of the instruments the quant wants to consider trading for the purpose of generating returns. For example, in a trend-following strategy in the futures markets, the alpha model is designed to forecast the direction of whatever futures markets the quant has decided to include in his strategy. """

    def __init__(self):
        self.broker = Oanda()

    def gaussian(self, mu=0, sigma=.34):
        alpha = {}
        for symbol in self.broker.universe():
            alpha[symbol] = round(random.gauss(mu, sigma), 4)
            if alpha[symbol] > 1.0:
                alpha[symbol] = 1.0
            if alpha[symbol] < -1.0:
                alpha[symbol] = -1.0
        return alpha
