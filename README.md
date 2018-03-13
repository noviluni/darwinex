
# Darwinex API Client

[Darwinex](https://www.darwinex.com/) API in Python

*Note: This is not an official package and it uses the [Darwinex for investors mobile app](https://play.google.com/store/apps/details?id=com.darwinex.investors) API. Darwinex owners can change this API and api keys without previous notice.*

Still in progress.

## Instalation
Just download and import the script. It will soon be available in *[Python Package Index](https://pypi.python.org/pypi/pip)*.

## Usage

##### Initialization of the client:

```python
>>> from darwinex_client import DarwinexAPIClient
>>> d = DarwinexAPIClient(user='...', password='...')
Using DEMO account. To use real account add demo=False.
```

By default, the client uses the demo account. To use the real account you should add `demo=False`.

```python
>>> from darwinex_client import DarwinexAPIClient
>>> d = DarwinexAPIClient(user='...', password='...', demo=False)
Using REAL account. Use at YOUR OWN RISK!
```

##### Information about the user:

```python
>>> d.me
{'investorAccount': {'currency': 'EUR', 'type': 'REAL'},
 'me': 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX',
 'user': {'username': 'XXXXX'}}
```

##### User balance:

```python
>>> d.balance
{'available': 0.03,
 'availableToInvest': 0.06,
 'equity': 601.87,
 'wallet': 0.0}
```

##### User portfolio summary:

```python
>>> d.portfolio_summary
{'available': 0.02,
 'availableToInvest': 0.04,
 'closedPnL': -83.54,
 'equity': 603.43,
 'equityAtRisk': 64.97,
 'invested': 1232.64,
 'maxRisk': 80.0,
 'openPnL': -12.9,
 'pfees': 2.7795284357312826,
 'rebates': 2.66}
```

##### User portfolio distribution:

```python
>>> d.portfolio_distribution
[{'averageQuote': 254.79,
  'currentQuote': 256.69,
  'invested': 342.69,
  'openPnL': 2.71,
  'product': 'DLF.4.7'},
 {'averageQuote': 206.3,
  'currentQuote': 200.71,
  'invested': 221.14,
  'openPnL': -6.98,
  'product': 'VTJ.4.2'},
 {'averageQuote': 216.13,
  'currentQuote': 219.4,
  'invested': 281.75,
  'openPnL': 4.68,
  'product': 'JZH.4.13'},
 {'averageQuote': 285.8,
  'currentQuote': 276.14,
  'invested': 387.07,
  'openPnL': -13.36,
  'product': 'QUA.4.3'}]
```

##### Search for darwins:

```python
>>> d.search('QU')
[{'dscore': 77.96831050154333, 'product_name': 'QUA.4.3'},
 {'dscore': 10.391335758989062, 'product_name': 'QUE.4.20'},
 {'dscore': 4.682561128567671, 'product_name': 'QUJ.4.9'}]
```

##### Darwin current quote:

```python
>>>  d.darwin_quote('QUA.4.3')
{'quote': 276.1400721992568, 'timestamp': 1520632740122}
```

##### Darwin quotes from last two years:

```python
>>>  d.darwin_quote('QUA.4.3')
{'chart': {'max': 142.92,
  'min': 0.0,
  'values': [0.0,
   5.1502119295446285,
   5.669752968691046,
   ...
   107.92114846431498]},
   'quote': 276.1400721992568,
   'return': 107.92114846431498,
   'zoom': '2Y'}
```

##### Buy a darwin:

```python
>>>  d.buy('VTJ.4.2', 25)
{'price': 200.71}
```

##### Sell a darwin:

```python
>>>  d.sell('VTJ.4.2', 25)
{'price': 200.71}
```

##### Get investment in a darwin:

```python
>>>  d.get_investment('VTJ.4.2')
{'darwin_availability':
    {'availableOperations': ['BUY', 'SELL'],
    'status': 'ACTIVE'},
 'investment':
    {'averageQuote': 285.8,
     'closedPnL': -39.43,
     'divergence': -0.07,
     'highwatermark': 0.0,
     'invested': 387.07,
     'openPnL': -13.36,
     'paidPfees': 0.0,
     'pendingPfees': 0.0,
     'quarterEnds': 18},
 'investor_balance':
    {'available': 0.02,
     'availableToInvest': 0.04,
     'equity': 603.37,
     'wallet': 0.0}
}
```

### NOTE: A complete documentation is under construction. You can see all available methods and how to use them diving into the code.

## Requirements
##### Python Requirements:
`requests`

##### System Requirements:
`Python 3`

## Colaboration
Pull requests are welcome!

## License
MIT license
