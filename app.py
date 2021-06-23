from ariadne import graphql_sync, make_executable_schema, ObjectType, gql, load_schema_from_path, \
    snake_case_fallback_resolvers
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
from flask_cors import CORS
from queries import resolve_user_repos

query = ObjectType("Query")
query.set_field("user_repos", resolve_user_repos)
type_defs = gql(load_schema_from_path("./schema.graphql"))
schema = make_executable_schema(type_defs, query, snake_case_fallback_resolvers)

app = Flask(__name__)
cors = CORS(app, resources={r"/graphql": {"origins": "*"}})


@app.route('/')
def root():
    return 'Hello World!', 200


@app.route("/graphql", methods=["GET"])
def graphql_playgroud():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)
    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == '__main__':
    app.run(debug=True)
