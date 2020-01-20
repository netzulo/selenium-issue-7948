Can reproduce bug with **windows 10 (x64)** , **Python 3.6.8** and this **snippet**

```
git clone https://github.com/netzulo/maybeissue
cd maybeissue
mkvirtualenv maybeissue
workon maybeissue
python setup.py clean build install
pip install -r requirements-tests.txt
py.test tests/test_poc.py
```

That commands results on this installation dependencies

```
atomicwrites==1.3.0
attrs==19.3.0
colorama==0.4.3
importlib-metadata==1.4.0
maybeissue==0.0.0
more-itertools==8.1.0
packaging==20.0
pluggy==0.13.1
py==1.8.1
pyparsing==2.4.6
pytest==5.3.4
selenium==3.141.0
six==1.14.0
urllib3==1.25.7
wcwidth==0.1.8
zipp==2.0.0
```

With last command you can see traces of "maybe issue" when execute pytest testcases

```
    try:
        basestring
    except NameError:  # Python 3.x
        basestring = str
    
    import shutil
    import sys
    from contextlib import contextmanager
    
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
>   from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
E     File "c:\users\cronos\envs\maybeissue2\lib\site-packages\selenium-3.141.0-py3.6.egg\selenium\webdriver\remote\webdriver.py", line 359
E       """
E        ^
E   SyntaxError: invalid escape sequence \_

c:\users\cronos\envs\maybeissue2\lib\site-packages\selenium-3.141.0-py3.6.egg\selenium\webdriver\firefox\webdriver.py:29: SyntaxError
```
