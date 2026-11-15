# Data Processing Lab

## Lab Overview

This lab demonstrates a small in-memory data-processing workflow built with Python and CSV files. It loads city and country records, stores them as `Table` objects in a simple `DB` container, and supports filtering, aggregation, and joining tables.

When run, the script prints examples including Italian cities and their average temperature, non-EU countries, countries with coastlines, joined city and country records, and temperature queries over the joined data.

## Project Structure

```text
data-processing-lab/
├── data_processing.py   # Data-loading, table, database, and demonstration code
├── Cities.csv           # City location and temperature records
├── Countries.csv        # Country population, EU, and coastline records
└── README.md            # Lab documentation and run instructions
```

Both CSV files are read from the directory containing `data_processing.py`. `Cities.csv` has the columns `city`, `country`, `latitude`, `longitude`, and `temperature`. `Countries.csv` has `country`, `population`, `EU`, and `coastline`. CSV values are loaded as strings; aggregation converts values to numbers when the requested key is `temperature`.

## Design Overview

### `DataLoader`

Loads CSV files and returns their rows as dictionaries.

- **Attribute — `base_path`:** A `Path` used as the directory for data files. It defaults to the directory containing `data_processing.py`; callers can pass a different directory to the constructor.
- **`__init__(base_path=None)`:** Sets the directory used for subsequent loads.
- **`load_csv(filename)`:** Opens `filename` under `base_path`, reads it with `csv.DictReader`, and returns a list of dictionaries. Each dictionary maps a CSV column name to its string value.

### `DB`

An in-memory collection of `Table` objects.

- **Attribute — `tables`:** A list that holds inserted tables.
- **`insert(table)`:** Adds a `Table` to `tables`. Raises `TypeError` if the argument is not a `Table`.
- **`search(table_name)`:** Returns the first table whose `table_name` matches, or `None` if there is no match.

### `Table`

Represents a named collection of row dictionaries and provides basic data operations.

- **Attribute — `table_name`:** The table's name.
- **Attribute — `table`:** A list of row dictionaries. The constructor copies each input row into a new dictionary.
- **`__init__(table_name, data)`:** Creates a table from a name and an iterable of row dictionaries.
- **`__str__()`:** Formats the table as its name followed by its rows.
- **`filter(condition)`:** Returns a new table containing rows for which `condition(row)` is true. The returned table name appends `_filtered` to the original name.
- **`aggregate(aggregation_function, aggregation_key)`:** Collects the specified field from every row and passes the resulting list to `aggregation_function`. Values are converted to `float` when `aggregation_key` is `temperature`; other fields are passed through as stored.
- **`join(other, key)`:** Matches rows from this table and `other` where the chosen key has equal values, returning a new table with the matching row fields combined. Raises `TypeError` if `other` is not a `Table`. If both rows contain the same column name, the value from `other` takes precedence.

### Script workflow

At the bottom of `data_processing.py`, the script loads both CSV files, wraps their rows in `Table` objects, and inserts those objects into `my_DB`. It then searches the database for each table and demonstrates filtering, aggregation, and joining. The examples use `country` as the join key and use the CSV text values `yes` and `no` for EU and coastline checks.

## How to Run and Test

Python 3 is required. The code uses Python's standard library, so no third-party package installation is needed. From the project directory, run:

```bash
python data_processing.py
```

On systems where the Python 3 command is named `python3`, use:

```bash
python3 data_processing.py
```

The script prints each demonstration result to the terminal. To smoke-check the lab, confirm that it completes without an exception and prints sections for Italian cities, average temperature, non-EU countries, coastline count, joined rows, and the temperature queries. Keep `Cities.csv` and `Countries.csv` beside `data_processing.py`, or construct `DataLoader` with the directory containing the CSV files.

There is currently no separate automated test suite in the project. The script's built-in examples serve as the manual smoke check; `DataLoader`, `DB`, and `Table` can also be exercised directly from another Python script.
