# pip install flask
# pip install connexion
#
# Optional:
# pip install connexion[swagger-ui]   >>> enables http://127.0.0.1:5000/api/ui to access the swagger

# Run this and open: http://127.0.0.1:5000/api/people
# The service is defined in swagger.yml, the implementation is in rest-service-people.py
# The swagger references the implementation (operationId)

import connexion


# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)