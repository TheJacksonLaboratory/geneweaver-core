# Geneweaver Core
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

#### Planned Functionality
* `geneweaver.core.logging`: Shared logging management
* `geneweaver.core.utils`: Shared utility functions


## Acknowledgements
This project was developed by the Computational Systems and Synthetic Biology Center at the Jackson Laboratory in
conjunction with the Baylor University Computational Biology and Bioinformatics Program.

