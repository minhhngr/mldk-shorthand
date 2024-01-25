# Locator

## XPath

* [XPath](https://developer.mozilla.org/en-US/docs/Web/XPath)
* [XPath Tester](https://extendsclass.com/xpath-tester.html)
* [XPath Function](https://developer.mozilla.org/en-US/docs/Web/XPath/Functions)
* [XPath Axes](https://developer.mozilla.org/en-US/docs/Web/XPath/Axes)

## Programming

## Debugging

* [Get the Text of an HTML Element in JavaScript](https://bobbyhadz.com/blog/javascript-get-text-of-html-element)
* [Evaluate and validate XPath/CSS selectors in Chrome Developer Tools
](https://yizeng.me/2014/03/23/evaluate-and-validate-xpath-css-selectors-in-chrome-developer-tools/)

### Get Text in Console log and create constructor

```javascript
$$('.navCategory > ul > li > a').forEach(e => console.log(e.textContent.toLowerCase().replace(/[\s,&]+/g, '_') + ' = "' + e.textContent + '"'));

const modifiedStrings = $$('.navCategory > ul > li > a').map(e => e.textContent.toLowerCase().replace(/[\s,&]+/g, '_') + ' = "' + e.textContent + '"');

console.log(modifiedStrings);
```

### Python

```python

from selenium.webdriver.common import by
class By:
    """Set of supported locator strategies."""

    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"

from appium.webdriver.common.appiumby import AppiumBy
class AppiumBy(By):
    IOS_PREDICATE = '-ios predicate string'
    IOS_UIAUTOMATION = '-ios uiautomation'
    IOS_CLASS_CHAIN = '-ios class chain'
    ANDROID_UIAUTOMATOR = '-android uiautomator'
    ANDROID_VIEWTAG = '-android viewtag'
    ANDROID_DATA_MATCHER = '-android datamatcher'
    ANDROID_VIEW_MATCHER = '-android viewmatcher'
    # Deprecated
    WINDOWS_UI_AUTOMATION = '-windows uiautomation'
    ACCESSIBILITY_ID = 'accessibility id'
    IMAGE = '-image'
    CUSTOM = '-custom'

from appium.webdriver.common.mobileby import MobileBy
class MobileBy(AppiumBy):
    """
        deprecated:: 2.1.0
        Please use 'from appium.webdriver.common.appiumby import AppiumBy' instead of 'MobileBy'.
    """

```

## References

* [How Selenium 4 Relative Locator Can Change The Way You Test](https://www.lambdatest.com/blog/selenium-4-relative-locator/)
* [XPath Axes: Ancestor, Following Sibling, Preceding](https://www.scientecheasy.com/2019/08/xpath-axes.html/)
