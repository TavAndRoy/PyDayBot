from http.server import BaseHTTPRequestHandler,HTTPServer
import PyDayBot

#DEFINE PORT NUMBER HERE:
PORT_NUMBER = 6969
BOT_NAME = "UTTTL"
HANDLER_FUNC = None
INFO_FUNC = None

class myHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return
    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type','text/html')
        self.end_headers()

        if (self.path.startswith("/info")):
            self.wfile.write(INFO_FUNC(self.path))
        elif (self.path.startswith("/turn")): #HERE YOU HANDLE THE REQUEST FROM THE ENGINE
            opponent_move = self.path.split('/')[2] #This is the move that the opponent has made (2 letters - board + square)
            self.wfile.write(HANDLER_FUNC(opponent_move)) #This is the output - should be 2 letters - board + square. (A,B,C,D,E,F,G,H,I)
        return

def start_bot(f, e, pn):
    global HANDLER_FUNC, INFO_FUNC, PORT_NUMBER
    HANDLER_FUNC = f
    INFO_FUNC = e
    PORT_NUMBER = pn
    try:
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print("Press Ctrl+C to stop the bot")
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()

def main():
    start_bot(BoardHandler, InfoHandler, PORT_NUMBER);

def InfoHandler(data):
    print("Info: " + data)
    return BOT_NAME.encode()

def BoardHandler(move):
    print("OP move: " + move)
    return "EE".encode() if move == "NN" else move.encode()

if __name__ == "__main__":
    main()