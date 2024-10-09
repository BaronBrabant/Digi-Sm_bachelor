from my_app import app
from my_app.models import db, createUserTaskInit, createAdmin
import sys
import os
from os.path import exists

if __name__ == '__main__':

	with app.app_context():
		
		database_exists = exists(os.path.dirname(__file__)+ "/data.db")

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
				if not database_exists:
					print("Database file not found, creating new database...")
					db.create_all()
					createAdmin()
		else:
			print("Loading existing database...")
			if not database_exists:
				print("Database file not found, creating new database...")
				db.create_all()
				createAdmin()
			
	app.run(debug=True)


	
