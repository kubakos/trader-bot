from blackbox.broker import Oanda


class RiskModel(object):
    """ Risk models are designed to help limit the amount of exposure the quant has to those factors that are unlikely to generate returns but could drive losses. For example, the trend follower could choose to limit his directional exposure to a given asset class, such as commodities, because of concerns that too many forecasts he follows could line up in the same direction, leading to excess risk; the risk model would contain the levels for these commodity exposure limits. """

    def __init__(self):
        pass

    def kelly_formula(self):
        pass
