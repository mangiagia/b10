from flask import Flask,request,make_response
from werkzeug.contrib.fixers import ProxyFix
import showSked
import volunteer
import json,time
import user


app = Flask(__name__)

@app.route('/user/login',methods=['POST'])
def login():
    a=request.get_json(silent=False)
    login_name=a.get('login_name')
    login_pwd=a.get('login_pwd')
    userInfo=user.login(login_name)
    if (userInfo):
        user_type=userInfo.get('user_type')
        correct_pwd= userInfo.get('login_pwd')
        user_id=userInfo.get('user_id')
        if(login_pwd==correct_pwd):
            date={'result_code':'200','result_msg':'登陆成功','user_id':user_id,'user_type':user_type}

        else:
            date = {'result_code':'201','result_msg':'密码错误'}
    else:
        date = {'result_code':'202', 'result_msg': '账号不存在'}

    json_str = json.dumps(date, ensure_ascii=False)
    return make_response(json_str)





@app.route('/show/insert' ,methods=['POST'])
def showAdd():
    a=request.get_json(silent=False)
    performer=a.get('performer')
    showTime = a.get('showTime')
    show=showSked.show(performer,showTime)
    showSked.insert(show.performer,show.showTime)
    return make_response('成功')

@app.route('/show/query' ,methods=['GET'])
def showQuery():
    show = showSked.select()
    date = {'show': show}
    jasn_str = json.dumps(date, ensure_ascii=False)
    return make_response(jasn_str)


@app.route('/volunteer/insert',methods=['POST'])
def addVolunteer():
    a=request.get_json(silent=False)
    name = a.get('name')
    mobile = a.get('mobile')
    volunteer_type = a.get('volunteer_type')
    is_food = a.get('is_food')
    is_volunteer = a.get('is_volunteer')
    remark = a.get('remark')
    show_id=a.get('show_id')
    created_date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  #时间格式转换成str
    volunteer.insert(name,show_id,mobile, volunteer_type, is_food, is_volunteer, remark, created_date)
    return make_response('成功')


@app.route('/volunteer/query',methods=['POST'])
def queryVolunteer():
    a=request.get_json(silent=False)
    # print (a)
    show_id=a.get('show_id')
    date={"volunteer":volunteer.select(show_id)}
    jasn_str = json.dumps(date, ensure_ascii=False)
    return make_response(jasn_str)
    # return make_response('jasn_str')


@app.route('/volunteer/update',methods=['POST'])
def updateVolunteer():
    a=request.get_json(silent=False)
    print (a)
    id=a.get('id')
    is_volunteer=a.get('is_volunteer')
    volunteer.update(id,is_volunteer)
    return make_response('成功')


if __name__ == '__main__':
	app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host="172.31.145.125")
