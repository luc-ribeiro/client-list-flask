from flask import Flask, render_template, request, redirect

app = Flask(__name__)

clients = []
clients_search = []

# HOME #


@app.route('/')
def index():
    return render_template('index.html', list_clients=clients, list_clients_search=clients_search)

# SAVE #


@app.route('/save-client', methods=['POST'])
def save():
    end_search()

    if not clients:
        id = 1
    else:
        id = clients[-1]['id'] + 1

    name = request.form['name']
    phone = request.form['phone']
    subject = request.form['subject']

    client = {"id": id, "name": name, "phone": phone, "subject": subject}
    clients.append(client)

    return redirect('/')

# DELETE #


@app.route('/delete-client/<int:id>')
def delete(id):
    end_search()

    for i in range(len(clients)):
        if clients[i]['id'] == id:
            del clients[i]
            break

    return redirect('/')

# SEARCH #


@app.route('/search-client', methods=['POST'])
def search():
    end_search()

    query = request.form['search-client'].lower()

    if query == '':
        return redirect('/')
    else:
        for i in range(len(clients)):
            if query in clients[i]['name'].lower() or \
                    query in clients[i]['phone'].lower() or \
                    query in clients[i]['subject'].lower():
                clients_search.append(clients[i])

    return redirect('/')

# END SEARCH #


@app.route('/search-client/end')
def end_search():
    clients_search.clear()

    return redirect('/')


app.run(debug=True)
