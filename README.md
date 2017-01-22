*NOTE: This is a work in progress.*

# Package mxklabs.dimacs
The Python package mxklabs.dimacs is for reading (and in future possibly writing) files in the DIMACS format. This format is the 'de facto' standard for Boolean formulas in SAT competitions and SAT solvers.

## Quick API Overview

| Object | Type | Description |
|---|---|---|
| [mxklabs.dimacs.Dimacs](#mxklabs.dimacs.Dimacs) | 'class' | A class representing a Boolean formula (in DIMACS format). |
| [mxklabs.dimacs.DimacsException](#mxklabs.dimacs.DimacsException) | 'class' | A class representing an exception. |
| mxklabs.dimacs.read_from_file(file) | 'function' | Parses the content of the 'file' object (as specified by the file parameter) and returns an object of type '[mxklabs.dimacs.Dimacs](#mxklabs.dimacs.Dimacs)'. |
| mxklabs.dimacs.read_from_filename(filename) | 'function' | Opens a file (as specified by the filename parameter), parses its returns an object of type '[mxklabs.dimacs.Dimacs](#mxklabs.dimacs.Dimacs)'. |
| mxklabs.dimacs.read_from_string(string) | 'function' | Parses the string parameter and returns an object of type '[mxklabs.dimacs.Dimacs](#mxklabs.dimacs.Dimacs)'. |


## <a name="mxklabs.dimacs.Dimacs">Class mxklabs.dimacs.Dimacs</a>

| Object | Type | Description |
|---|---|---|
| num_vars | 'int' | The number of Boolean variables. |
| num_clauses | 'int' | The number of clauses. |
| clauses | 'list' of 'list' of 'int' | The clauses. | 

## <a name="mxklabs.dimacs.DimacsException">Class mxklabs.dimacs.DimacsException</a>

*Inherits from Exception.*

## Reading DIMACS input.

1. Reading from a file:

```python
import mxklabs.dimacs as dimacs
dimacs = dimacs.read_from_file('file1.cnf')
```
