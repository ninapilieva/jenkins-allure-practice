[1mdiff --git a/test_login.py b/test_login.py[m
[1mindex b81782b..77ec29a 100644[m
[1m--- a/test_login.py[m
[1m+++ b/test_login.py[m
[36m@@ -29,7 +29,7 @@[m [mdef test_invalid_username(page: Page):[m
         page.goto(LOGIN_URL)[m
 [m
     with allure.step("Enter an invalid username"):[m
[31m-        page.locator("#username").fill("student")[m
[32m+[m[32m        page.locator("#username").fill("wrongUser")[m
         page.locator("#password").fill("Password123")[m
 [m
     with allure.step("Submit the login form"):[m
