from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Connect to database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine  # connect classes to database tables
DBSession = sessionmaker(bind = engine) # create connection
session = DBSession() # create session

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurant"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                restaurants = session.query(Restaurant).all() # retrieve everything in database
                output = ""
                output += "<html><body>"
                output += "<a href='/restaurant/new'>Make a New Restaurant Here</a><br/><br/>"
                for r in restaurants:
                    output += r.name
                    output += "<br/>"
                    output += "<a href='/restaurant/{}/edit'>Edit</a>".format(r.id)
                    output += "<br/>"
                    output += "<a href='/restaurant/{}/delete'>Delete</a>".format(r.id)
                    output += "<br/>"
                    output += "<br/>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/restaurant/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='restaurant/new'>"
                output += "<input name='newRestaurantName' type='text' placeholder='New Restaurant Name'>"
                output += "<input type='submit' value='Create'>"
                output += "</form>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split("/")[2]
                myQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                if myQuery != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<h1>{}</h1>".format(myQuery.name)
                    output += "<form method='POST' enctype='multipart/form-data' "
                    output += "action='/restaurant/{}/edit'>".format(restaurantIDPath)
                    output += "<input name='newRestaurantName' type='text' "
                    output += "placeholder='{}'>".format(myQuery.name)
                    output += "<input type='submit' value='Rename'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                    print output
                    return

            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                if myQuery != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<html><body>"
                    output += "<h1>Are you sure you want to delete {}?</h1>".format(myQuery.name)
                    output += "<form method='POST' enctype='multipart/form-data' "
                    output += "action='/restaurant/{}/delete'>".format(restaurantIDPath)
                    output += "<input type='submit' value='Delete'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                    print output
                    return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                if myQuery != []:
                    session.delete(myQuery)
                    session.commit()

                    self.send_response(303)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurant')
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    restaurantIDPath = self.path.split("/")[2]

                    myQuery = session.query(Restaurant).filter_by(id = restaurantIDPath).one()
                    if myQuery != []:
                        myQuery.name = messagecontent[0]
                        session.add(myQuery)
                        session.commit()

                        self.send_response(303)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurant')
                        self.end_headers()

            if self.path.endswith("/restaurant/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                # Create new Restaurant class
                newRestaurant = Restaurant(name = messagecontent[0])
                session.add(newRestaurant)
                session.commit()

                self.send_response(303)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurant')
                self.end_headers()

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
