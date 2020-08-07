from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def Start():
    return render_template('Welcome.html')
    
@app.route('/user_inputs',  methods=[ 'GET', 'POST'])
def inputs():
    results = {}
    if request.method == 'POST':
        mood = request.form['input1']
        games = request.form['input2']
        from Games import output
        games_result = output(mood, games) ##print or return
        
        if game_result == dead:
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
    