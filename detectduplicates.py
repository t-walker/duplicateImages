import os # files
import hashlib # get the md5 hash
import threading
from datetime import datetime

threadLimiter = threading.BoundedSemaphore(50)

class DetectDuplicates:
	def __init__(self, directory):
		self.multiple_files = []
		self.comparison_files = []
		self.image_dictionary = {}

		for root, directories, filenames in os.walk(directory):
			for filename in filenames:
				self.comparison_files.append(os.path.join(root,filename))

		dt = datetime.now()
		t1 = dt.second
		for _file_ in self.comparison_files:
			#threading.Thread(target=self.imageToHash, args=(_file_,)).start()
			self.imageToHash(_file_)
		dt = datetime.now()
		t2 = dt.second

		print "Time to finish hashing files:", t2 - t1

		return

	def imageToHash(self, image_file):
		image = open(image_file, "rb")
		m = hashlib.md5()
		m.update(image.read())

		hash_line = m.hexdigest()
		if hash_line in self.image_dictionary:
			self.multiple_files.append(image_file)
		else:
			self.image_dictionary[hash_line] = image_file
