# Logging verbosity
```{eval-rst}
.. role:: small
```

```{eval-rst}
.. role:: smaller
```

Scanpy's logger function is used by scSELpy to output warnings and info. For example "REMAP_1 is added to ```anndata```" info is displayed after a new key is added. The verbosity settings of Scanpy is temporary overridden by scSELpy's own verbosity setting, which is set to the integer 2 (info) by default. 

The scSELpy's verbosity setting can be changed to not show info messages by:
```scSELpy.settings.verbosity = 1 ```

From scanpy._settings.ScanpyConfig.verbosity:
Level 0: only show ‘error’ messages. Level 1: also show ‘warning’ messages. Level 2: also show ‘info’ messages. Level 3: also show ‘hint’ messages. Level 4: also show very detailed progress for ‘debug’ging.
