# Command Line Stonks

This project was originally housed as part of my arch linux system dotfiles. However, it quickly evolved.

The `cli_stonks` module is a fully-functional, command-line wrapper around various parts of the TD Ameritrade API. It currently features quote and account information retrieval, rudimentary risk analysis (e.g. sharpe ratio/risk-free rate scraping), and various other utlity functions--such as storing daily portfolio volatility in a BigQuery table provided you have a Google Cloud account.

I am not a financial advisor.

Medium Article: https://nealdotpy.medium.com/i-cheated-on-windows-and-it-was-the-best-decision-of-my-life-b380a2f9d9c9

Previous Repository: https://github.com/nealdotpy/dotfiles/tree/master/bin/scripts/stockbar

# Documentation

This module assumes a decent level of familiarity with the TD Ameritrade API.

Browsing `main.py` should help in understanding how this executable script works under the hood. I've refactored it in such a way that reading it becomes trivial.

In order to get our own module up and running, you'll need to create an `.env` file and browse the `cli_stonks.constants` module in order to see the constants needed for functionality to work.

Of course, you may need to adjust the terminal color codes for your own system and emulator. I use rxvt-unicode, so mine are set accordingly.

In addition, if you use a broker other than TD Ameritrade, you'll likely find no use in this module. I would like to automate the the 90-day refresh token intervals. Currently, those are handled manually when the system notifies me of repeated failures to get a new `access_token`.

`cloud/` contains the code for the cloud function I set up in Google Cloud Platform. In turn, this function is linked to a BigQuery Table. Much of the cloud functionality is in its infancy at the moment. I intend to put the risk-free rate scraping into its own table as well and automate it via a cloud function.

The `config` file is only relevant if using the `watchlist` functionality to hook into Polybar (see: `main.py`).

I've done my best to make the code as readable as I can, including using `typing` and comments where functionality might be unclear. 


# Previews

![](img/acc-status-demo.png)

![](img/cli-quote.png)

![](img/actual-ticker-close.png)

![](img/desktop-clutter-lowres.png)

![](img/desktop-no-clutter.png)


