# Command Line Stonks

This project was originally housed as part of my arch linux system dotfiles. However, it quickly evolved.

The `cli_stonks` module is a fully-functional, command-line wrapper around various parts of the TD Ameritrade API. It currently features quote and account information retrieval, rudimentary risk analysis (e.g. sharpe ratio/risk-free rate scraping), and various other utlity functions--such as storing daily portfolio volatility in a BigQuery table provided you have a Google Cloud account.

The `config` file is only relevant if using the `watchlist` functionality to hook into Polybar. All parts work as-is. I am not a financial advisor.


Medium Article: https://nealdotpy.medium.com/i-cheated-on-windows-and-it-was-the-best-decision-of-my-life-b380a2f9d9c9

Previous Repository: https://github.com/nealdotpy/dotfiles/tree/master/bin/scripts/stockbar

# Previews

![](img/acc-status-demo.png)

![](img/cli-quote.png)

![](img/actual-ticker-close.png)

![](img/desktop-clutter-lowres.png)

![](img/desktop-no-clutter.png)


