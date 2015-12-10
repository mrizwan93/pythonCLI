import feedparser

sources = ['http://planet.gnome.org/atom.xml',
			'https://planetkde.org/rss20.xml',
			'http://planet.openstack.org/rss20.xml',
			'http://planetpython.org/rss20.xml',
			'http://fedoraplanet.org/atom.xml']
files = {"http://planet.gnome.org/atom.xml":"planetGnomeReport.txt",
		 "https://planetkde.org/rss20.xml":"planetKdeReport.txt",
		 "http://planet.openstack.org/rss20.xml":"planetOpenStackReport.txt",
		 "http://planetpython.org/rss20.xml":"planetPythonReport.txt",
		 "http://fedoraplanet.org/atom.xml":"planetFedoraReport.txt"}

for source in sources:
	feed = feedparser.parse(source)
	report = open(files[source], "wb")
	i=0
	for entry in feed.entries:
		i += 1
		entry = dict(entry)
		try:
			title = entry['title'].encode('utf-8')
		except Exception, e:
			print "Exception :"+ str(e)
			title = None
		try:
			updated = entry['updated'].encode('utf-8')
		except Exception, e:
			print e
			updated = entry['published'].encode('utf-8')
		report.write(str(i)+". Title :      "+str(title)+"\t on "+str(updated)+"\n")

		# try:
		# 	updated = entry['updated'].encode('utf-8')
		# except Exception, e:
		# 	print "Exception :"+ str(e)
		# 	updated = None
		# report.write("On :"+ str(updated)+"\n")

		try:
			planetName = feed['feed']['title'].encode('utf-8')
		except Exception, e:
			print "Exception :"+ str(e)
			planetName = None
		report.write("  Planet Name :" +str(planetName)+"\n")

		try:
			blogTitle = entry['title'].encode('utf-8')
		except Exception, e:
			print "Exception :"+ str(e)
			blogTitle = None
		report.write("  Blog Title : "+ str(blogTitle)+"\n")

		try:
			author = entry['author'].encode('utf-8')
		except Exception, e:
			print "Exception :"+ str(e)
			author = None
		report.write("  Author : "+ str(author)+"\n")

		try:
			content = entry['summary'].encode('utf-8')
		except Exception, e:
			print "Exception :"+ str(e)
			content = None
		report.write("  Contents : "+str(content)+"\n")

		for l in entry['links']:
			try:
				link = l['href'].encode('utf-8')
			except Exception, e:
				print "Exception :"+ str(e)
				link = None
			report.write("  links : "+ str(link)+"\n")
		report.write("\n \n")
	print 'done with '+ str(files[source])
report.close()
