from flask import jsonify


def send(data=None, code=200, error=None):
  # wrap = {
  #   'ok'      : (error == None),
  #   'request' : '%s %s%s' % (request.method, request.host_url, request.full_path[1:]),
  #   'date'    : str(datetime.datetime.utcnow()),
  # }
  # if data:
  #   wrap['data'] = data
  # if error:
  #   wrap['error'] = error
  # if 'details' in request.args:
  #   resp = jsonify(wrap)
  # else:
  #   resp = jsonify(data)
  # if code == 401:
  #   resp.headers['WWW-Authenticate'] = 'Basic realm="Code Deploy"'

  resp = jsonify(data)
  resp.status_code = code
  resp.headers['Server'] = 'Rainbows and unicorns'

  return resp

def error(message, code=400):
  resp = jsonify({
    'ok': False,
    'error': message
  })
  resp.status_code = code
  resp.headers['Server'] = 'Rainbows and unicorns'

  return resp
