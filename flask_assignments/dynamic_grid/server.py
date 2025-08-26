from flask import Flask, render_template, redirect, request

app = Flask(__name__)


# THIS IS THE CONTROLLER PART - WILL MOVE TO THE CONTROLLER FILES

# Stacking routes -> must have default (python) params for routes that have additional args
@app.route('/')
@app.route('/<int:rows>')
@app.route('/<int:rows>/<int:cols>')
def index(rows=3, cols=3): # default (python) params

    # getting html params coming from a form. MUST access the form through the "request" object
    rows = int(request.args.get('qty_rows', rows))
    cols = int(request.args.get('qty_cols', cols))

    
    # passing vars through to the html page. 
    return render_template('/public/index.html', rows=rows, cols=cols)

# END OF CONTROLLER



# LEAVE THIS AT THE BOTTOM
if __name__ == '__main__':
    app.run(debug=True)