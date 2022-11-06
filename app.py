# Core Pkgs
import streamlit as st 

# EDA Pkgs
import pandas as pd 
import codecs
from pandas_profiling import ProfileReport 

# Components Pkgs
import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report

# Custome Component Fxn
import sweetviz as sv 

def st_display_sweetviz(report_html,width=1000,height=500):
	report_file = codecs.open(report_html,'r')
	page = report_file.read()
	components.html(page,width=width,height=height,scrolling=True)


footer_temp = """
	<!-- CSS  -->
	<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	<link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	<link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">

	<footer class="page-footer grey darken-4">
		<div class="container" id="aboutapp">
	      	<div class="row">
	        	<div class="col l6 s12">
	          		<h5 class="white-text">About Streamlit EDA App</h5>
	          		<p class="grey-text text-lighten-4">Using Streamlit,Pandas,Pandas Profile and SweetViz.</p>
	        	</div>
	      
	   			<div class="col l3 s12">
	          		<h5 class="white-text">Connect With Me</h5>
	          		<ul>
	            		<a href="https://facebook.com/jcharistech" target="_blank" class="white-text">
	            			<i class="fab fa-facebook fa-4x"></i>
	          			</a>
	          			<a href="https://gh.linkedin.com/in/jesiel-emmanuel-agbemabiase-6935b690" target="_blank" class="white-text">
	            			<i class="fab fa-linkedin fa-4x"></i>
	          			</a>
	        			<a href="https://www.youtube.com/channel/UC2wMHF4HBkTMGLsvZAIWzRg" target="_blank" class="white-text">
	        				<i class="fab fa-youtube-square fa-4x"></i>
	          			</a>
	           			<a href="https://github.com/Jcharis/" target="_blank" class="white-text">
	            			<i class="fab fa-github-square fa-4x"></i>
	          			</a>
	          		</ul>
	        	</div>
	      	</div>
	    </div>
	    <div class="footer-copyright">
	      	<div class="container">
				Made by <a class="white-text text-lighten-3" href="https://jcharistech.wordpress.com">Jesse E.Agbe & JCharisTech</a><br/>
	      		<a class="white-text text-lighten-3" href="https://jcharistech.wordpress.com">Jesus Saves @JCharisTech</a>
	      	</div>
	    </div>
	</footer>
"""

def main():
	"""A Simple EDA App with Streamlit Components"""

	menu = ["Home","Pandas Profile","Sweetviz"]

	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Pandas Profile":
		st.subheader("Automated EDA with Pandas Profile")
		data_file = st.file_uploader("Upload CSV",type=['csv'])
		if data_file is not None:
			df = pd.read_csv(data_file)
			st.dataframe(df.head())
			profile = ProfileReport(df)
			st_profile_report(profile)

	elif choice == "Sweetviz":
		st.subheader("Automated EDA with Sweetviz")
		data_file = st.file_uploader("Upload CSV",type=['csv'])
		if data_file is not None:
			df = pd.read_csv(data_file)
			st.dataframe(df.head())
			if st.button("Generate Sweetviz Report"):
				# Normal Workflow
				report = sv.analyze(df)
				report.show_html()
				st_display_sweetviz("SWEETVIZ_REPORT.html")

	else:
		st.subheader("Home")
		html_temp = """
			<div style="background-color:royalblue;padding:10px;border-radius:10px">
				<h1 style="color:white;text-align:center;">Simple EDA App with Streamlit Components</h1>
			</div>
		"""

		# components.html("<p style='color:red;'> Streamlit Components is Awesome</p>")
		components.html(html_temp)

		components.html("""
			<style>
				* {box-sizing: border-box}
				body {
					font-family: Verdana,sans-serif; 
					margin:0
				}
				.mySlides {display: none}
				img {vertical-align: middle;}

				/* Slideshow container */
				.slideshow-container {
			  		max-width: 1000px;
			  		position: relative;
			  		margin: auto;
				}

				/* Next & previous buttons */
				.prev, .next {
					cursor: pointer;
			  		position: absolute;
			  		top: 50%;
			  		width: auto;
			  		padding: 16px;
			  		margin-top: -22px;
			  		color: white;
			  		font-weight: bold;
			  		font-size: 18px;
			  		transition: 0.6s ease;
			  		border-radius: 0 3px 3px 0;
			  		user-select: none;
				}

				/* Position the "next button" to the right */
				.next {
			  		right: 0;
			  		border-radius: 3px 0 0 3px;
				}

				/* On hover, add a black background color with a little bit see-through */
				.prev:hover, .next:hover {
			  		background-color: rgba(0,0,0,0.8);
				}

				/* Caption text */
				.text {
			  		color: #f2f2f2;
			  		font-size: 15px;
			  		padding: 8px 12px;
			  		position: absolute;
			  		bottom: 8px;
			  		width: 100%;
			  		text-align: center;
				}

				/* Number text (1/3 etc) */
				.numbertext {
			  		color: #f2f2f2;
			  		font-size: 12px;
			  		padding: 8px 12px;
					position: absolute;
					top: 0;
				}

				/* The dots/bullets/indicators */
				.dot {
			  		cursor: pointer;
			  		height: 15px;
			  		width: 15px;
			  		margin: 0 2px;
			  		background-color: #bbb;
			  		border-radius: 50%;
			  		display: inline-block;
			  		transition: background-color 0.6s ease;
				}

				.active, .dot:hover {
			  		background-color: #717171;
				}

				@-webkit-keyframes fade {
			  		from {opacity: .4} 
			  		to {opacity: 1}
				}

				@keyframes fade {
			  		from {opacity: .4} 
			  		to {opacity: 1}
				}

				/* On smaller screens, decrease text size */
				@media only screen and (max-width: 300px) {
			  		.prev, .next,.text {font-size: 11px}
				}
			</style>
		""")

if __name__ == '__main__':
	main()