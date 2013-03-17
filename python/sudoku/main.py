from bottle import route, run, request, static_file
import sudoku

@route("/")
def sudoku_main():
    return static_file('main.html', root='./views')
@route("/css/<filename:path>")
def sudoku_css(filename):
    return static_file(filename, root='./public/css')
@route("/js/<filename:path>")
def sudoku_js(filename):
    return static_file(filename, root='./public/js')

import json
# notice: when you use json, you must use post instead of get.
@route("/sudoku/sudokuresult", method='POST')
def sudoku_result():
    points_hash = request.json
    answer = sudoku.answer_quiz(points_hash)
    if answer:
        return json.dumps(answer)
    else:
        return "false"


print "http://localhost:9998"
run(host='localhost', port=9998,reloader=True)
