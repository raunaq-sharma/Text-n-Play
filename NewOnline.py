from flask import Flask
from flask import request
from flask import render_template
import NewGame_v2

app = Flask(__name__)

@app.route('/')
def Start():
    return render_template('Welcome.html')
    
@app.route('/user_inputs',  methods=[ 'GET', 'POST'])
def inputs():
    results = {}
    if request.method == 'POST':
        NewGame_v2.Map['opening_1']
        action = request.form['input1']
        unlock = request.form['input2']
        decision = request.form['input3']
        
        #from Games import main
        output = main(action, unlock, decision)
        
        if output.status == "death":
            return render_template('death.html')
        
        else:
            #continue game until dead or finish
            .
            .
            .
        return games_result
        return render_template('output.html', methods = ['POST'])
    return render_template('User_inputs.html', results=results)
 
    
if __name__ == "__main__":
    app.run(debug=True)
    