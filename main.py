from src.application.controllers.prognosis_controller import app
from src.main.env import envs
if __name__ == '__main__':
    app.run(port=envs.get('PORT'),host=envs.get('HOST'), debug=envs.get('DEBUG'))
