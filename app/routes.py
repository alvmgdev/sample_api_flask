from app import app


@app.route('/')
def index():
    return "Hello World from Flask"


@app.route('/users', methods=['POST'])
def create_user():
    return "Create user"


@app.route('/users', methods=['GET'])
def get_users():
    return "Users list"


@app.route('/users/<int:id>', methods=['GET'])
def get_user_detail(id):
    return "User detail"


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    return "Update user"


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    return "Delete user"
