from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function
    #print("welcome/ url is requested & display() is executed");
    print(request)
    print(type(request))
    #ss---> is html code/data
    ss = "<center><h2 style='color:Blue;'>Hello User, Welcome to Django First-Project First-App</h2><hr /></center>";
    return HttpResponse(ss);
    
    
def show(request):
    print("hello user");
    ss='''
        <!--
	HTML Webpage to display 'Welcome-Message' with different Headings 
	(F:\SAISIR\HTML\Welcome.html)
-->

<html>
	<head>
			}
			h2{
				color:Green;
			}
			h3{
				color:Red;
			}
			h4{
				color:Orange;
			}
			h5{
				color:Pink;
			}
			h6{
				color:violet;
			}
			h1,h3,h5{
		<title>***Weclome-Page***</title>
		<style>
			h1{
				color:Blue;
				background-color:yellow;
			}
			h2,h4,h6{
				background-color:lightgreen;
			}
		</style>
	</head>
	<body>
		<center>
			<h1>Welcome to DJANGO HTML webpage</h1>
			<hr color='brown' width='95%'/>
			<h2>Welcome to DJANGO HTML webpage</h2>
			<hr color='brown' width='85%'/>
			<h3>Welcome to DJANGO HTML webpage</h3>
			<hr color='brown' width='75%'/>
			<h4>Welcome to DJANGO HTML webpage</h4>
			<hr color='brown' width='65%'/>
			<h5>Welcome to DJANGO HTML webpage</h5>
			<hr color='brown' width='55%'/>
			<h6>Welcome to DJANGO HTML webpage</h6>
			<hr color='brown' width='45%'/>
		</center>
	</body>
</html>
''';
    return HttpResponse(ss); 

    
def hello(request):
	print("hello/ url is requested & hello() is executed");
	ss='''
	<html>
		<head>
			<title>Hello Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightblue;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Hello User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Welcome to Django-App</h2>
				<hr color='brown' width='60%'/>
				<h3>Have a nice day...</h3>
				<hr color='brown' width='40%'/>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);



import time;	
def senddatetime(request):
	print("dtime/ url is requested & senddatetime() is executed");
	ct = time.ctime()
	print("Client Request Date & time on server :: ",ct);
	ss='''
	<html>
		<head>
			<title>Date-time Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightgreen;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Welcome to DJango-User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Server-Date & Time :: </h2>
				<hr color='brown' width='70%'/>
				<h3>''',ct,'''</h3>
				<hr color='brown' width='60%'/>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);
    
    
#single-view-function with multiple-urls    
def demo(request):   
	print("mulitple-Requests-URLs same respose");
	htmldata='''
    <center>
		<h1>Welcome Demo User!!!</h1>
		<hr />
		<h2>This is Same-Output for diff-mulitple-Requests-URLs</h2>
		<hr />
		<h3>Have a Great Day...</h3>
	</center>
    ''';
	return HttpResponse(htmldata);
    
    
#default-url-request-view-func
def homepage(request):
    htmldata='''
        <center>
        <h1>Welcome to DEFAULT Home-Page!!!</h1>
        <hr />
        <h2>Your Request Page is Not-Found...</h2>
        <hr />
        <h3>Plz try other URL or Links!!!</h3>
        </center>
        ''';
    return HttpResponse(htmldata);
  
