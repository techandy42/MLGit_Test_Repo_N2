# MLGit_Test_Repo_N2

A Test Repo for MLGit.

### Descriptions

- Python
- Relative Imports

### Naming Scheme

- `<module name or module acronym>_dummy_<type>_<n>` for each identifier.

### Circular Imports

> Circular Imports

```
a <-> b [one import at runtime]
c <-> d [both imports at runtime]
```

> Triple Circular Imports

```
   a
 /   \
b --- c
```

> Diamond Circular Imports

```
   a
 / | \
b  |  c
 \ | /
   d
```

### Import Graph

> Graph

- (1) `src/outer_module_producer_a.py`:
- (2) `src/outer_module_consumer_a.py`: (7)
- (3) `src/app/app.py`: (4), (5), (7)
- (4) `src/app/definitions.py`:
- (5) `src/app/externals_modules.py`: (os), (math), (6)
- (6) `src/app/utils.py`:
- (7) `src/app/subdirectory_1/inner_module_producer_a.py`: (sys), (os), (9)
- (8) `src/app/subdirectory_1/inner_module_consumer_a.py`: (sys), (os), (1)
- (9) `src/app/subdirectory_2/inner_module_circular_import_a.py`: (10)
- (10) `src/app/subdirectory_2/inner_module_circular_import_b.py`: (9)
