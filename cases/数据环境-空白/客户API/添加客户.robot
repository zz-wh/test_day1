*** Settings ***

Library  添加客户.py   WITH NAME  M

Library  添加客户.c1   WITH NAME  c1



*** Test Cases ***

客户API-0101

  c1.teststeps
