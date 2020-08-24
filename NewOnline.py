from flask import Flask
from flask import request, url_for, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def Start():
    return render_template('opening.html')
    
    
@app.route('/input_3',  methods=[ 'GET', 'POST'])

def input_3():
    results = {}
    if request.method == 'POST':
        decision = request.form['input3']
        from NewGame_v3 import treasure_room, Map
        results = treasure_room(decision)
        if results == (Map['more_than_50'] + "\n" +  Map['victory']):
            return render_template('victory.html', methods = 'POST', results = results)
        else:
            return render_template('death.html', methods = 'POST', results = results)
 
    return render_template('input_3.html', results = results)

@app.route('/input_2',  methods=[ 'GET', 'POST'])

def input_2():
    results = {}
    #return render_template('input_2.html', results = results)
    if request.method == 'POST':
        unlock = request.form['input2']
        from NewGame_v3 import lower_level, Map
        results = lower_level(unlock)[0]
        if results == lower_level(unlock)[1]:
            return redirect(url_for('input_3'))
        else:
            return render_template('death.html', methods = 'POST', results = results)
        
    return render_template('input_2.html', results = results)

@app.route('/input_1',  methods=[ 'GET', 'POST'])
    
def input_1():
    results = {}
    if request.method == 'POST':
        action = request.form['input1']
        from NewGame_v3 import entrance
        results = entrance(action)
        if action == "right":
            #return render_template('input_2.html', methods = ['GET', 'POST'], result = result)
            return redirect(url_for('input_2'))
            
        else:
            return render_template('death.html', methods = 'POST', results = results)
        
    return render_template('input_1.html', results = results)
        
        #from Games import main
        # output = main(action, unlock, decision)
        
        # if output.status == "death":
            # return render_template('death.html')
        
        # else:
            # #continue game until dead or finish
            # .
            # .
            # .
        # return games_result
        # result['key of stuff to be accessed']
        # return render_template('output.html', methods = ['POST'])
    
    # result['key of stuff to be accessed']
    # return render_template('User_inputs.html', results=results)
 
    
if __name__ == "__main__":
    app.run(debug=True)
    