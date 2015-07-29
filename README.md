# pandas-io
External IO utilities for pandas

## ROOT integration

ROOT is a data format commonly used in high energy physics

Usage:
```python
from pandas.io.external import read_root, to_root

df = read_root('in.root', 'mykey', columns=['test*'], where='test > 0')

to_root(df, 'out.root')
```
