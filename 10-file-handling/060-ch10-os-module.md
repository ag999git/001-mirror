


## Study Extended Concepts & Additional Methods of the `os` module

### 1. `os.remove(path)`

Deletes a file.

-   Raises `FileNotFoundError` if file does not exist
-   Raises `PermissionError` if file is in use

----------

### 2. `os.rmdir(path)`

Removes an **empty directory**

-   Fails if directory is not empty

----------

### 3. `os.makedirs(path, exist_ok=True)`

Creates directories (including nested ones)

----------

### 4. `os.path` Utilities 

  

| Function | Purpose |
| --- | --- |
| os.path.exists(path) | Check if path exists |
| os.path.isfile(path) | Check if file |
| os.path.isdir(path) | Check if directory |
| os.path.join(a,b) | Safe path joining |

### Summary Table

  

| Operation | Function | Works On | Error Type |
| --- | --- | --- | --- |
| Rename | `os.rename()` | File/Dir | `FileNotFoundError` |
| Delete file | `os.remove()` | File | `PermissionError` |
| Remove dir | `os.rmdir()` | Empty dir | `OSError` |
| List files | `os.listdir()` | Directory | `FileNotFoundError` |


### Common Errors & Exceptions

  

| Error | Cause |
| --- | --- |
| `FileNotFoundError` | File/path does not exist |
| `PermissionError` | No permission |
| `OSError` | Invalid operation |


















