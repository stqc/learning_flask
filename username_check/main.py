from flask import Flask, render_template, request

app  = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html', filled=True,contains_upper=True,contains_lower=True,contain_num=True,home=True)


@app.route('/check')
def check():
    name = request.args.get('user')
    contain_num = False
    contains_upper = False
    contains_lower = False
    filled = False
    if len(name)>0 :
        filled = True
        for i in name:
            if i.isdigit():
                contain_num = True
                break
        for i in name:
            if i.isupper():
                contains_upper = True
                break

        for i in name:
            if i.islower():
                contains_lower = True
                break

        return render_template('base.html', name=name,contains_upper=contains_upper,contains_lower=contains_lower,contain_num=contain_num, filled=filled)
    else:
        return render_template('base.html', filled=filled,name=name,contains_upper=True,contains_lower=True,contain_num=True)

if __name__ == "__main__":
    app.run(debug=True)
