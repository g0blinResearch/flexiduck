import os
from subprocess import call
from xml.dom import minidom
xmldoc = minidom.parse('/tmp/results.xml')

FNULL = open(os.devnull, 'w')
osParts = ['payloads'] + xmldoc.getElementsByTagName('osclass')[0].getElementsByTagName('cpe')[0].firstChild.nodeValue.split('cpe:/o:')[1].split(':')

while len(osParts):
	curDir = '/'.join(osParts)
	if os.path.isdir(curDir):
		payloads = [f for f in os.listdir(curDir) if os.path.isfile(os.path.join(curDir, f))]
		payloads.sort()
		for payload in payloads:
			filename, file_extension = os.path.splitext(payload)

			if file_extension == '.ds' or file_extension == '':
				call(["python", "duckhunter/duckhunter.py", "-l", "uk", os.path.join(curDir, payload), "/tmp/payload"], stdout=FNULL, stderr=FNULL)
				call(["chmod", "+x", "/tmp/payload"])
				call(["/bin/bash", "/tmp/payload"])
			elif file_extension == '.sh':
				call(["/bin/bash", os.path.join(curDir, payload)])
		break
	osParts.pop()
