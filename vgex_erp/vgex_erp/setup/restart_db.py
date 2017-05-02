from pathlib import Path 

def get_folders(this_folder):
	arr = []
	for item in this_folder.iterdir():
		if item.name[0] == '.':
			pass
		elif item.is_dir():
			arr.append(item)
	return arr

def get_files(this_folder):
	arr = []
	for item in this_folder.iterdir():
		if item.name[0] == '.':
			pass
		elif item.is_dir():
			pass
		else:
			arr.append(item)
	return arr

wf = Path(__file__)
pf = wf.parent.parent.parent

for app in get_folders(pf):
	mig_folder = app.joinpath('migrations')
	if not mig_folder.exists():
		continue
	for folder in get_folders(mig_folder):
		for file in get_files(folder):
			print('Deleting file {}'.format(file))
			file.unlink()
	for file in get_files(mig_folder):
		if file.name == '__init__.py':
			continue
		file.unlink()
		print('Deleting file {}'.format(file))

db = pf.joinpath('db.sqlite3')
if db.exists():
	print('Deleting database')
	db.unlink()

print('Process completed')