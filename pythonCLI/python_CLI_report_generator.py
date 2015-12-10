import argparse
import feedparser

class Report():
	sources = ['http://planet.gnome.org/atom.xml',
			'https://planetkde.org/rss20.xml',
			'http://planet.openstack.org/rss20.xml',
			'http://planetpython.org/rss20.xml',
			'http://fedoraplanet.org/atom.xml']

	def generateReport(self):
		i=0
		report = open('postReport.txt', "wb")
		for source in self.sources:
			feed = feedparser.parse(source)
			for entry in feed.entries:
				i += 1
				entry = dict(entry)
				try:
					title = entry['title'].encode('utf-8')
				except Exception, e:
					# print "Exception :"+ str(e)
					title = None
				try:
					updated = entry['updated'].encode('utf-8')
				except Exception, e:
					# print e
					updated = entry['published'].encode('utf-8')
				report.write(str(i)+". Title :      "+str(title)+"\t on "+str(updated)+"\n")

				try:
					planetName = feed['feed']['title'].encode('utf-8')
				except Exception, e:
					# print "Exception :"+ str(e)
					planetName = None
				report.write("  Planet Name :" +str(planetName)+"\n")

				try:
					blogTitle = entry['title'].encode('utf-8')
				except Exception, e:
					# print "Exception :"+ str(e)
					blogTitle = None
				report.write("  Blog Title : "+ str(blogTitle)+"\n")

				try:
					author = entry['author'].encode('utf-8')
				except Exception, e:
					# print "Exception :"+ str(e)
					author = None
				report.write("  Author : "+ str(author)+"\n")

				try:
					content = entry['summary'].encode('utf-8')
				except Exception, e:
					# print "Exception :"+ str(e)
					content = None
				report.write("  Contents : "+str(content)+"\n")

				for l in entry['links']:
					try:
						link = l['href'].encode('utf-8')
					except Exception, e:
						# print "Exception :"+ str(e)
						link = None
					report.write("  links : "+ str(link)+"\n")
				report.write("\n \n")
		report.close()
		print 'Report generated, check for postReport.txt in working directory!'


parser = argparse.ArgumentParser(description="generates plain text report for posts from the source(s)",
								epilog="creates file report.txt in working directory")
parser.add_argument("-r", "--report", action="count",
                    help="generates plain text report", required=True)
args = parser.parse_args()
if args.report :
	print 'generating report, please wait...'
	r = Report()
	r.generateReport()
