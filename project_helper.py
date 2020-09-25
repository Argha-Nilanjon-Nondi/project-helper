import os

def make_folder(file_list):
	for i in file_list:
		os.mkdir(i)

def file_js(dir):
	file=open(dir+"/js/script.js","w")
	file.close()

def file_css(dir):
	file=open(dir+"/css/style.css","w")
	file.close()
	
def file_html(file_list):
	code=r"""
<!DOCTYPE html>
<html>

  <head>
   
  <meta name="viewport" conent="width=device-width, initial-scale=1"> 
  
  <link rel="stylesheet" type="text/css" href="css/style.css">
   
    <title> </title>
    
   <style>
   
   </style>
    
  </head>
  
  <body>
  
  <script src="js/script.js"></script>
  <script type="text/javascript">
  
    try{
    }
    
    catch(a){
    alert(a.name+" "+a.message)
    }  

 </script>
  
  </body>
  
</html>
	"""
	for i in file_list:
		file=open(i+".html","w")
		file.write(code)
		file.close()
		
def main(root,page):
	
	base_dir=os.getcwd()
	
	project_dir=base_dir+"/"+root
	
	os.chdir(base_dir)
	
	os.mkdir(root)
	
	os.chdir(project_dir)
	
	htmls=["index"]
	
	htmls+=page
	
	file_html(htmls)
	
	make_folder(["js","css","img"])
	
	os.chdir(project_dir+"/css")
	
	make_folder(["img"])
	
	file_css(project_dir)
	
	file_js(project_dir)
	
project_name="Responsive_website__test"
pages=["index","login","logout"]
main(project_name,pages)
print()