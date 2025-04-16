# This entrypoint file to be used in development. Start by reading README.md
from sea_level_predictor import draw_plot

# Just call show directly from plt module after calling draw_plot
draw_plot()
import matplotlib.pyplot as plt
plt.show()