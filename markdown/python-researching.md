# Python Shorthand Researching

## Python with vscode

### Auto formatting file after save

> .vscode/setting.json

```JSON
{
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true,
            "source.unusedImports": true
        },
    },
    "isort.args":["--profile", "black"]
}
```

## Python in Game

* [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/)
* [The Pythonic Way](https://python.plainenglish.io/the-pythonic-way-4d59bb8799eb)
* [Python Testing](https://realpython.com/python-testing/)
* [Example Google Style Python Docstring](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* [Working With Classes in Python](https://blog.martinfitzpatrick.com/python-classes/)
* [Creating a Zip Archive of a Directory in Python](https://stackabuse.com/creating-a-zip-archive-of-a-directory-in-python/s)
* [Differences Between Python's defaultdict and dict](https://stackabuse.com/differences-between-pythons-defaultdict-and-dict/)

## Python in Excel

* [Getting started with Python in Excel](https://support.microsoft.com/en-us/office/getting-started-with-python-in-excel-a33fbcbe-065b-41d3-82cf-23d05397f53d)
* [Python in Excel DataFrames](https://support.microsoft.com/en-us/office/python-in-excel-dataframes-a10495b2-8372-4f0f-9179-32771fe0dc04)
