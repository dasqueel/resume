import sys
import time
import socket
import webbrowser

#questions
def questCont():
	while True:
		answer = raw_input('thus far, are you interested in continuing? (options: yes/no) \n\n')

		if answer == 'yes':
			read('\nawwwwwggghh thanks! you are making me blush, let us continue...')
			return answer
		elif answer == 'no':
			read('\n:( awwww shucks thats too bad, well I wish the best on your endeavors!')
			return answer
		else:
			read('plz answer yes or no ;)')
			continue

	return answer

def questInterested():
	while True:
		answer = raw_input('Would you care to see my beta site for this idea? (options: heck yeah/na pass) \n\n')

		if answer == 'heck yeah':
			read('\nooo boy, I am excited to show ya!')
			return answer
		elif answer == 'na pass':
			read('\n:( awwww shucks thats too bad, then I do not think we make a fit for one another FeelsBadMan')
			return answer
		else:
			read('plz answer "heck yeah" or "na pass" ;)')
			continue

	return answer

def questPostBS():
	while True:
		answer = raw_input('when you are done checking out brainswole and would like to continue with my resume script, type, "continue", else type "pass" \n\n')

		if answer == 'continue':
			read('\nSweet! if ya like to get a better understanding of myself, my intentions, and my other projects...')
			read('check out neilbarduson.com/resume, the passcode is "neilsawesomeresume"')
			read('Once again thanks for checking out my resume script, (^_^)/  have a swell day!!')
			return answer
		elif answer == 'pass':
			read('\n:( awwww shucks thats too bad, then I do not think we would make a fit for one another FeelsBadMan')
			return answer
		else:
			read('\nplz answer "continue" or "pass" ;)')
			continue

	return answer

def seeDemo():
	while True:
		answer = raw_input('would you like to see a video demonstration? (options: yup/nope) \n\n')

		if answer == 'yup':
			return answer
		elif answer == 'nope':
			read('\nthats cool, if you want to watch it later, you can find the video at neilbarduson.com/resume')
			return answer
		else:
			read('\nplz answer yes or no ;)')
			continue

	return answer

def afterDemoCont():
	while True:
		answer = raw_input('\nwould you like to continue? (options: yup/nope) \n\n')

		if answer == 'yup':
			return answer
		elif answer == 'nope':
			return answer
		else:
			read('plz answer yup or nope ;)')
			continue

	return answer

#helper func to print out text
def read(text):
	i=0
	while i < len(text):
	    sys.stdout.write(text[i])
	    sys.stdout.flush()
	    time.sleep(0.05)
	    i += 1
	time.sleep(0.15)
	print '\n'


#start the program
read('good day! my name is Neil')
read('thanks for taking the time to check out my profile! :D')
read('the quick scivy on me is:')
read('I ask myself the question:')
time.sleep(1)
read('What will humanities best, most efficient, way of education look like?')
time.sleep(2)
read('I try to answer that, and build it.')
time.sleep(0.8)

read('Why?')
time.sleep(1.5)
read('Because I want to make the most impact for human prosperity.')
read('And the more accessible, compelling, veracious, and lucid information is; the smarter the individual and society are.')
time.sleep(1.5)

contAnsw = questCont()

if contAnsw == 'yes':

	read('If I could, I would build the holodeck from Star Trek and put one in every local library.')
	read('Then anybody could imagine any scenario to learn any concept, and run the simulation.')
	time.sleep(1)
	read('Too bad the actual holodeck is not feasible any time soon.  (We will see how far VR and AR progress. :D)')
	time.sleep(1)
	read('In the mean time, I think there is a basic primitive version of the holodeck with all the online learning modules.')
	read('For example, Khanacademy, Codecademy, Treehouse, etc...')
	read('I have made a few of my own learning modules too, however...')
	read('I thought it would be more beneficial if I made a site where a person could aggregate all their learning progress/data from different learning modules.')
	time.sleep(1.2)
	read('So each person would have an archive of their learning.')
	read('This could assist with their organization AND show their compentency in certain knowledge domains.')

	intAnsw = questInterested()

	if intAnsw == 'heck yeah':
		read('brainswole.com is the website.')
		read('as of now brainswole has three functions:')
		time.sleep(1)
		read('1: a place to aggregate a users online learning data/progress from various online learning providers (Khanacademy,Codewars,Codecadmey,etc...)')
		time.sleep(1)
		demoAnsw1 = seeDemo()
		if demoAnsw1 == 'yup':
			webbrowser.open_new("https://neilbarduson.com/static/vids/aggregate.mp4")
			afterDemoContAnsw = afterDemoCont()
		else:
			pass

		read('\nthe second function of brainswole is:')
		time.sleep(0.8)
		read('a reddit-ish page the ranks links of STEM concepts.')
		time.sleep(1)
		demoAnsw1 = seeDemo()
		if demoAnsw1 == 'yup':
			webbrowser.open_new("https://neilbarduson.com/static/vids/bsreddit.mp4")
			afterDemoContAnsw = afterDemoCont()
		else:
			pass

		read('\nthe third function is:')
		read('to create an archive of your interaction with the previous two functions.')
		time.sleep(1)
		read('brainswole is quite alpha, and I do not have any active users.')
		read('so it may look bare, however the site should work and display its purpose/potential')
		time.sleep(1)
		read('enough of me gabbing, try heading over to brainswole.com, sign up with a dummy account, and check it out!')
		#ask if they want to see other parts of my resume
		postBSAnsw = questPostBS()

	else:
		read('awwwww nuts')

