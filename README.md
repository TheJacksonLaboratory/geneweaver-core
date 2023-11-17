# Geneweaver Core

[![Tests](https://github.com/TheJacksonLaboratory/geneweaver-core/actions/workflows/tests.yml/badge.svg?event=push)](https://github.com/TheJacksonLaboratory/geneweaver-core/actions/workflows/tests.yml)
[![Style](https://github.com/TheJacksonLaboratory/geneweaver-core/actions/workflows/style.yml/badge.svg?event=push)](https://github.com/TheJacksonLaboratory/geneweaver-core/actions/workflows/style.yml)
[![Coverage](https://github.com/TheJacksonLaboratory/geneweaver-core/actions/workflows/coverage.yml/badge.svg?event=push)](https://github.com/TheJacksonLaboratory/geneweaver-core/actions/workflows/coverage.yml)

The Geneweaver Core Python library provides shared foundational functionality for the Geneweaver project. 
It is a dependency of all other Geneweaver Python libraries, and is not intended to be used directly.

## Installation
The Geneweaver Core library is available on PyPI and can be installed with pip:
```bash
pip install geneweaver-core
```

If you are using Poetry, you can add the Geneweaver Core library to your project with:
```bash
poetry add geneweaver-core
```

## Overview
This package is structured so as to share an import path with other `geneweaver` packages. This allows you to install
the package and import it without having to worry about the package name. For example, if you install the `geneweaver-core`
package, as well as the `geneweaver-db` package, you can import the `geneweaver` package and access both libraries:
```python
from geneweaver import core, db
```

The Geneweaver Core library provides the following functionality:
* `geneweaver.core.schema`: Pydantic schema definitions
* `geneweaver.core.enum`: Enumerations


* `geneweaver.core.config`: Configuration management
  * `GeneweaverBaseSettings`: Base Settings class to inherit from for your own package's configuration classes
  * `GeneweaverCoreSettings`: Configuration class for Geneweaver Core settings


* `geneweaver.core.exc`: Geneweaver shared exceptions
  * `GeneweaverException`: Base exception class for Geneweaver
  * `GeneweaverError`: Base error class for Geneweaver
  * `GeneweaverWarning`: Base warning class for Geneweaver

* `geneweaver.core.pase`: Geneweaver file parsing functionality
  * `batch`: Functions for parsing a batch file
  * `score`: Functions for parsing a score
  * `csv`: Functions for parsing a CSV file
  * `xlsx`: Functions for parsing an Excel file
  * `enum`: Enumerations for file parsing
  * `exceptions`: Exceptions for file parsing
  * `utils`: Utility functions for file parsing

#### Planned Functionality
* `geneweaver.core.logging`: Shared logging management
* `geneweaver.core.utils`: Shared utility functions
