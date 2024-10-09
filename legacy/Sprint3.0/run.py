from my_app import app
from my_app.models import db, createUserTaskInit, createAdmin
import sys

if __name__ == '__main__':

	with app.app_context():

		## Create the dummy database !!! THIS DELTES ALL DATA IN THE DATABASE !!!   
		if len(sys.argv) > 1:
			if sys.argv[1] == "-dummy":
				print("Creating dummy database...")
				db.drop_all()
				db.create_all()
				
				createUserTaskInit()
			elif sys.argv[1] == "-create":
				print("Creating database file...")
				db.drop_all()
				db.create_all()
				createAdmin()
			else:
				print("Unknown command...")
				print("Loading existing database...")
		else:
			print("Loading existing database...")
			
	app.run(debug=True)


	
