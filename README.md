pyutil
![](https://img.shields.io/badge/python%20-%203.7-brightgreen.svg)
========
> python utils 

## `Install`
` pip install git+https://github.com/zhouxianggen/pyutil.git`

## `Upgrade`
` pip install --upgrade git+https://github.com/zhouxianggen/pyutil.git`

## `Uninstall`
` pip uninstall pyutil`

## `Basic Usage`
```python
import time
from pyutil import SingletonScript

def main():
    print('main start')
    time.sleep(5)
    print('main end')

if __name__ == '__main__':
    # 保证当前脚本只有一个实例在运行
    SingletonScript()
    main()

```
