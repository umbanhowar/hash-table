from hash_map import HashMap, Bucket
import unittest

class TestHashMap(unittest.TestCase):
	def test_set(self):
		# test that set correctly increments the counter when new
		# and that it doesn't increment the size when already in table
		h = HashMap(100)
		self.assertEqual(h.count, 0)
		h.set('1', SampleObject('A'))
		self.assertEqual(h.count, 1)
		h.set('1', SampleObject('A2'))
		self.assertEqual(h.count, 1)
		h.set('2', SampleObject('B'))
		self.assertEqual(h.count, 2)

		# test that it returns false when the table is full
		h = HashMap(100)
		for i in xrange(0, 100):
			added = h.set(str(i), SampleObject(chr(i + 10)))
			self.assertEqual(added, True)
		added = h.set(str(100), SampleObject(chr(100 + 10)))
		self.assertEqual(added, False)

	def test_get(self):
		h = HashMap(100)
		h.set('1', SampleObject('A'))
		b_obj = SampleObject('B')
		h.set('2', b_obj)
		h.set('3', SampleObject('C'))
		self.assertEqual(h.get('2'), b_obj)
		self.assertEqual(h.get('4'), None)

	def test_delete(self):
		pass
	def test_load(self):
		############# test full load ##############
		h = HashMap(100)
		for i in xrange(0, 100):
			added = h.set(str(i), SampleObject(chr(i + 10)))
		self.assertEqual(h.load(), 1)
		######## test partially full load #########
		h = HashMap(100)
		for i in xrange(0, 67):
			added = h.set(str(i), SampleObject(chr(i + 10)))
		self.assertEqual(h.load(), 0.67)
		############# test empty load #############
		h = HashMap(100)
		self.assertEqual(h.load(), 0)
	def test_change_val(self):
		h = HashMap(3)
		h.set('1', SampleObject('A'))
		b_obj = SampleObject('B')
		h.set('2', b_obj)
		self.assertEqual(h.get('2'), b_obj)
		h.set('3', SampleObject('C'))
		b_obj_2 = SampleObject('B2')
		h.set('2', b_obj_2)
		self.assertEqual(h.get('2'), b_obj_2)


class TestBucket(unittest.TestCase):
	def test_set(self):
		######################################################
		######### test first add behaves as expected #########
		######################################################
		b = Bucket()
		# obj is some arbitrary object reference, we'll use a SampleObject
		obj = SampleObject("A")
		first = ("1", obj)
		self.assertEqual(b.length, 0)
		b.set(first)
		self.assertEqual(b.length, 1)

		######################################################
		########## test n adds behave as expected ############
		######################################################
		b = Bucket()
		self.assertEqual(b.length, 0)
		for i in xrange(0, 10):
			to_add = (str(i), SampleObject(chr(i + 10)))
			b.set(to_add)
		self.assertEqual(b.length, 10)

		########################################################################
		###### test that set changes value when key already in list ############
		########################################################################
		b = Bucket()
		self.assertEqual(b.length, 0)
		for i in xrange(0, 10):
			to_add = (str(i), SampleObject(chr(i + 10)))
			b.set(to_add)


	def test_get(self):
		#########################################################
		########## test that get returns correct val ############
		#########################################################
		b = Bucket()
		self.assertEqual(b.length, 0)
		for i in xrange(0, 9):
			to_add = (str(i), SampleObject(chr(i + 10)))
			b.set(to_add)
		last_obj = SampleObject(chr(9 + 10))
		last_pair = ('9', last_obj)
		b.set(last_pair)
		self.assertEqual(b.get('9'), last_obj)

		########################################################################
		########## test that get returns None for key not in bucket ############
		########################################################################
		b = Bucket()
		self.assertEqual(b.length, 0)
		for i in xrange(0, 9):
			to_add = (str(i), SampleObject(chr(i + 10)))
			b.set(to_add)
		self.assertEqual(b.get('K'), None)

	def test_remove(self):
		b = Bucket()
		self.assertEqual(b.length, 0)
		for i in xrange(0, 9):
			to_add = (str(i), SampleObject(chr(i + 10)))
			b.set(to_add)
		b.remove('B')
		self.assertEqual(b.get('B'), None)
		self.assertEqual(b.remove('B'), None)


class SampleObject():
	"""
	Class SampleObject is a test object that holds a string
	"""
	def __init__(self, string):
		self.str = string
	def __str__(self):
		return 'SO[' + self.str + ']'

if __name__ == '__main__':
	unittest.main(verbosity=2)

