""""Christmas tree farm"""

class ChristmasTreeFarm:
    plots: list[int]

    def __int__(self, plots: int, initial_planting: int) -> None:
        i: int = 1
        self.plots = []
        while i < initial_planting:
            self.plots.append[i]
            i += 1
        while i < plots:
            self.plots.append(0)
            i += 1

    def plant(self, plot_i: int) -> None:
        self.plots[plot_i] = 1

