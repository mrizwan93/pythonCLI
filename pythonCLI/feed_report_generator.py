import feedparser
d = feedparser.parse('http://fedoraplanet.org/atom.xml')
print d

entries=open("entries.txt","wb")		#file to store all entries
report = open("report.txt", "wb")		#file to store the report
for i in d.entries:
	i=dict(i)
	entries.write(str(i))

	title = i['title'].encode('utf-8')
	report.write("Title :      "+str(title)+"\n")

	updated = i['updated'].encode('utf-8')
	report.write("On :"+ str(updated)+"\n")

	planetName = d['feed']['generator'].encode('utf-8')
	report.write("Planet Name :" +str(planetName)+"\n")

	blogTitle = i['title'].encode('utf-8')
	report.write("Blog Title : "+ str(blogTitle)+"\n")

	author=i['author'].encode('utf-8')
	report.write("Author : "+ str(author)+"\n")

	content = i['summary'].encode('utf-8')
	report.write("Contents : "+str(content)+"\n")

	for l in i['links']:
		link = l['href'].encode('utf-8')
		report.write("links : "+ str(link)+"\n")
	for k in range(1, 2) :
		report.write('\n')
report.close()
entries.close()
