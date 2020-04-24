from flask import request,redirect

from common.libs.UrlManager import UrlManager
from application import app

import re

# 每次请求之前都要先经过这里
@app.before_request
def before_request():
    path = request.path

    # if not user_info:
    #     return redirect(UrlManager.buildUrl("/user/login"))
    # return


# 判断用户是否登录
def check_login():
    return