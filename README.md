# SoozPy

SoozHub API Wrapper: Python-Powered API for Market Insights

## Installation

SoozPy is not currently available on PyPI. To install, clone the repository and install the required dependencies:

**1. Clone the Repository**:

```
git clone https://github.com/your-username/soozpy.git
cd soozpy
```

**2. Install Dependencies**:
Ensure you have Python 3.x installed on your system. Then install the required packages using:

```
pip install -r requirements.txt
```

**3. Configure environment variables**:
Create a .env file in the root of the project directory and set the database URI. This URI should match the PostgreSQL database configuration:
```
SOOZHUB_DB_URI=postgresql://your_username:your_password@your_host:your_port/your_database
```

Replace your_username, your_password, your_host, your_port, and your_database with the actual PostgreSQL credentials and details.

After completing these steps, you can start using SoozPy by importing it into your Python script or Jupyter notebook.

## Getting Started

```from datetime import datetime
from soozpy.queries import get_historical_prices

# Define a date range for the test
from_date = datetime(2023, 3, 9)
to_date = datetime(2023, 4, 9)

result = get_historical_prices(from_date, to_date, symbols=['BTC'])

result.head()
```

First available datetime: 2023-01-11 17:52:00

## Sample Output

After fetching historical price data, the output will be a Pandas DataFrame. Here's an example of what the output might look like:

```
  symbol            datetime         price        volume
0    BTC 2023-03-09 00:02:00  21723.077495  2.251922e+10
1    BTC 2023-03-09 00:07:00  21724.449532  2.245498e+10
2    BTC 2023-03-09 00:12:00  21735.450191  2.244329e+10
3    BTC 2023-03-09 00:17:00  21723.250426  2.244539e+10
4    BTC 2023-03-09 00:22:00  21709.559090  2.245276e+10
```

## Contact

For questions or feedback, please contact:

soozzarsoftware@gmail.com

carlos.mastrangelo@gmail.com
