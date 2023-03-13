from modules.portfolio import PortfolioConstructionModel
from modules.execution import ExecutionModel
from modules.broker import Oanda


portfolio = PortfolioConstructionModel()
execute = ExecutionModel()

broker = Oanda()

broker.set_leverage(.9)
