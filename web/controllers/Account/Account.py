from flask import Blueprint,render_template,request,redirect,jsonify

from common.models.User import User
from common.libs.UrlManager import UrlManager


router_account = Blueprint("account_page",__name__)

@router_account.route('/index')
def index():
    resp_data = {}
    li = User.query.all()
    resp_data["list"] = li
    return render_template("/account/index.html",**resp_data)


@router_account.route('/info')
def info():
    resp_data = {}
    uid = int(request.args.get("id",0))
    reback_url = UrlManager.buildUrl("/account/index")
    if uid < 1:
        return redirect(reback_url)
    info = User.query.filter_by(uid=uid).first()
    if not info:
        return redirect(reback_url)
    resp_data['info'] = info
    return render_template("/account/info.html",**resp_data)

'''
    带id参数，就是修改：更新数据库
    不带id参数，就是添加：创建数据，插入数据库
'''
@router_account.route('/set',methods=["GET","POST"])
def set():
    if request.method == "GET":
        resp_data = {}
        uid = int(request.args.get("id",0))
        info = None
        if uid:
            info = User.query.filter_by(uid=uid).first()
        resp_data['info'] = info   
        return render_template("/account/set.html",**resp_data)
    # POST
    resp = {
        'code':200,
        'msg':'操作成功',
        'data':{}
    }

    req = request.values
    id = req['id'] if 'id' in req else 0
    nickname = req['nickname'] if 'nickname' in req else ""
    mobile = req['mobile'] if 'mobile' in req else ""
    email = req['email'] if 'email' in req else ""
    login_name = req['login_name'] if 'login_name' in req else ""
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ""

    # 校检
    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入规范的昵称'
        return jsonify(resp)

    if mobile is None or len(mobile) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入规范的手机号'
        return jsonify(resp)

    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入规范的邮箱'
        return jsonify(resp)

    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入规范的登录名'
        return jsonify(resp)

    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入规范的登陆密码'
        return jsonify(resp)

    # 筛选
    is_exits = User.query.filter(User.login_name == login_name,User.uid != id).first()
    if is_exits:
        resp['code'] = -1
        resp['msg'] = '该用户名已存在，请重新输入'
        return jsonify(resp)
    return jsonify(resp)