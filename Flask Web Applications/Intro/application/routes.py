from application import app, db
from flask import Flask, render_template, request, redirect
from application.models import User, Userspost

@app.route('/') 
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        comment_id = Userspost.objects.count()
        comment_id += 1
        user_comment = request.form['comment']
        try:
            Userspost(comment_id = comment_id, user_comment = user_comment).save()
            return redirect('/')
        except:
            return "Your submission failed"
    else:
        db_comments = Userspost.objects.all()
        return render_template('index.html', db_comments=db_comments)

@app.route('/delete/<int:id>')
def delete(id):
    comment_to_del = Userspost.objects(comment_id = id)
    try:
        comment_to_del.delete()
        return redirect('/')
    except:
        return render_template('index.html')

@app.route('/edit/<int:edi>',methods= ['POST','GET'])
def edit(edi):
    eddit = True
    comment_to_edit = Userspost.objects(comment_id = edi)
    if request.method == 'POST':
        comment_id = edi
        user_comment = request.form['newComment']
        try:
            Userspost.objects(id = _id).update(comment_id = edi, user_comment = user_comment).save()
            return redirect('/')
        except:
            return "Comment was not updated " + str(user_comment)
    else:
        return render_template('update.html', comment_to_edit = comment_to_edit, eddit= eddit)



@app.route('/contact')
def contacts():
    return render_template('contact.html')# make sure that the templates folder is spelled as template

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name'] #Getting the username from the login form
        user_pass = request.form['password']
        user_verification = User.objects(username=user_name, password=user_pass).first()

        if user_verification:
            return redirect('/')
        else:
            return redirect('/login')
    else:
        return render_template('login.html')


@app.route('/registration',methods =['GET','POST'])
def registration():

    if request.method == 'POST':
        user_id = User.objects.count()
        user_id +=1
        user_name = request.form['user_name'] #Getting the username from the registration form
        user_pass = request.form['password']
        user_email = request.form['email']
        User(user_id = user_id,username = user_name,password = user_pass,email = user_email).save()
        return redirect('/login')

    return render_template('registration.html')
