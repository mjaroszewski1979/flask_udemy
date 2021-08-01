from flask import url_for, render_template, request
from flask import Blueprint
from send_mail import send_mail


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/success',methods=['GET', 'POST'] )
def success():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        send_mail(name=name, email=email, message=message)
    return render_template('success.html', name=name, email=email)

@main.route('/project02')
def project02():
    return render_template('project02.html')

@main.route('/project03')
def project03():
    return render_template('project03.html')

@main.route('/project04')
def project04():
    return render_template('project04.html')

@main.route('/project05')
def project05():
    return render_template('project05.html')

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
