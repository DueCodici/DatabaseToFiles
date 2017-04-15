import cmd

class DbShell(cmd.Cmd):
	def do_connect(self, args):
		"Connects to a database given its name"
		print("Connecting to db...")

	def do_show_classes(self, args):
		"Shows the database's classes"
		print("Showing classes...")

	def do_show_class_types(self, args):
		"Shows the class types"
		print("Showing class types...")

	def do_export_to_csv(self, args):
		"Exports the DB rows to the given CSV file name"
		print("Exporting to CSV...")

	def do_quit(self, args):
		"Exits the program"
		print("Exiting...")
		quit()

if __name__ == '__main__':
	DbShell().cmdloop()