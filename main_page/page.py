#!C:\Python34\python
import cgi
import cgitb; cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

form = cgi.FieldStorage() # se instancia solo una vez
buscar = form.getfirst('buscar', 'empty')
db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='bdalbum')


form = cgi.FieldStorage() # se instancia solo una vez
user= form.getfirst('user', 'empty')

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Topbuilder Construction Template</title>

    <!-- Favicon -->
    <link rel="icon" href="images/equipo.png" type="image/x-icon" />
    <!-- Bootstrap CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <!-- Animate CSS -->
    <link href="vendors/animate/animate.css" rel="stylesheet">
    <!-- Icon CSS-->
	<link rel="stylesheet" href="vendors/font-awesome/css/font-awesome.min.css">
    <!-- Camera Slider -->
    <link rel="stylesheet" href="vendors/camera-slider/camera.css">
    <!-- Owlcarousel CSS-->
	<link rel="stylesheet" type="text/css" href="vendors/owl_carousel/owl.carousel.css" media="all">

    <!--Theme Styles CSS-->
	<link rel="stylesheet" type="text/css" href="css/style.css" media="all" />

    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="js/html5shiv.min.js"></script>
    <script src="js/respond.min.js"></script>
    <![endif]-->
	
	<script language="JavaScript"> 
	function mueveReloj(){ 
		momentoActual = new Date() 
		hora = momentoActual.getHours() 
		minuto = momentoActual.getMinutes() 
		segundo = momentoActual.getSeconds() 

		str_segundo = new String (segundo) 
		if (str_segundo.length == 1) 
			segundo = "0" + segundo 

		str_minuto = new String (minuto) 
		if (str_minuto.length == 1) 
			minuto = "0" + minuto 

		str_hora = new String (hora) 
		if (str_hora.length == 1) 
			hora = "0" + hora 

		horaImprimible = hora + " : " + minuto + " : " + segundo 

		document.form_reloj.reloj.value = horaImprimible 

		setTimeout("mueveReloj()",1000) 
	} 
	</script>
</head>
<body onload="mueveReloj()">
	
    <!-- Preloader -->
    <div class="preloader"></div>

	<!-- Top Header_Area -->
	<section class="top_header_area">
	    <div class="container">
            <ul class="nav navbar-nav navbar-right social_nav">
                <li><a href="#"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fa fa-google-plus" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fa fa-instagram" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fa fa-pinterest-p" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fa fa-linkedin" aria-hidden="true"></i></a></li>
            </ul>
	    </div>
	</section>
	<!-- End Top Header_Area -->

	<!-- Header_Area -->
    <nav class="navbar navbar-default header_aera" id="main_navbar">
        <div class="container">
            <!-- searchForm -->
            <div class="searchForm">
                <form action="#" class="row m0">
                    <div class="input-group">
                        <span class="input-group-addon"><i class="fa fa-search"></i></span>
                        <input type="search" name="search" class="form-control" placeholder="Type & Hit Enter">
                        <span class="input-group-addon form_hide"><i class="fa fa-times"></i></span>
                    </div>
                </form>
            </div><!-- End searchForm -->
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="col-md-2 p0">
				<div class="navbar-header">
                    <a class="navbar-brand" href="index.html"><img src="images/logo.png" alt=""></a>
                </div>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="col-md-10 p0">
                <div class="collapse navbar-collapse" id="min_navbar">
                    <ul class="nav navbar-nav navbar-right">
					    <li class="dropdown submenu">
							<form name="form_reloj"> 
							<input align="left" type="text" name="reloj" size="20" style="background-color : Orange; color : Black; font-family : Verdana, Arial, Helvetica; font-size : 10pt; text-align : center;" onfocus="window.document.form_reloj.reloj.blur()"> 
							</form>
						</li>
                        <li class="dropdown submenu">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Menu</a>
							<ul class="dropdown-menu other_dropdwn">
                                <li><a href="about.html">Your Album</a></li>
                                <li><a href="about-2.html">About Us-2</a></li>
                            </ul>
                        </li>
                        <li class="dropdown submenu">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Tu Cuenta</a>
                        </li>
                        <li class="dropdown submenu">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Tus figuras</a>
                            <ul class="dropdown-menu other_dropdwn">
                                <li><a href="services.html">Services</a></li>
                                <li><a href="services-2.html">Services-2</a></li>
                            </ul>
                        </li>
                        <li><a href="#">Abrir Paquete</a></li>
                        <li><a href="contact.html">Contact</a></li>
                    </ul>
                </div><!-- /.navbar-collapse -->
            </div>
        </div><!-- /.container -->
    </nav>
	<!-- End Header_Area -->

    <!-- Slider area -->
    <section class="slider_area row m0">
        <div class="slider_inner">
            <div data-thumb="images/slider-1.jpg" data-src="images/slider-1.jpg">	
                <div class="camera_caption">
				<table with="100%" border="0">
				    <tr>
					  <td><a class="nav-link" href="../fifa/pagina.py?user=%s """%(user) + """ ">
							<img class="media-object" src="images/fig.png" alt=" "/>
					   </a></td>
					   <td><a class="nav-link" href="../fifa/pagina.py?user=%s """%(user) + """ ">
                        <img class="media-object" src="images/album.jpg" alt=""/>
					   </a></td> 
					</tr>
				</table>	
                </div>
            </div>
            <div data-thumb="images/slider-2.jpg" data-src="images/slider-2.jpg">
                <div class="camera_caption">
				   <table with="100%" border="0">
				    <tr>
					    <td><a class="nav-link" href="../fifa/pagina.py?user=%s" """ %(user) + """ >
							<img class="media-object" src="images/fig.png" alt=""/>
					    </a></td>
					    
					</tr>
					</table>
                </div>
            </div>
        </div>
    </section>
    <!-- End Slider area -->

    <!-- Professional Builde -->
    <section class="professional_builder row">
        <div class="container">
           <div class="row builder_all">
                <div class="col-md-3 col-sm-6 builder">
					<a href="about.html">
                                <img class="fa fa-building" src="images/team.png" alt="">
                    </a>
					<h4>Equipo</h4>
                </div>
                <div class="col-md-3 col-sm-6 builder">
					<a href="about.html"> <!--fa fa-clock-o-->
                                <img src="images/exchange_zone.png" alt="">
                    </a>
					<h4>Zona de Intercambio</h4>
                </div>
                <div class="col-md-3 col-sm-6 builder">
					<a href="about.html"> <!--fa fa-thumbs-up-->
                                <img src="images/exchange_zone.png" alt="">
                    </a>
                </div>
           </div>
        </div>
    </section>
    <!-- End Professional Builde -->

    <!-- Our Partners Area -->
    <section class="our_partners_area">
        <div class="container">
            <div class="tittle wow fadeInUp">
                <h2>Our Partners</h2>
                <h4>Lorem Ipsum is simply dummy text of the printing and typesetting industry</h4>
            </div>
            <div class="partners">
                <div class="item"><img src="images/client_logo/client_logo-1.png" alt=""></div>
                <div class="item"><img src="images/client_logo/client_logo-2.png" alt=""></div>
                <div class="item"><img src="images/client_logo/client_logo-3.png" alt=""></div>
                <div class="item"><img src="images/client_logo/client_logo-4.png" alt=""></div>
                <div class="item"><img src="images/client_logo/client_logo-5.png" alt=""></div>
            </div>
        </div>
    </section>
    <!-- End Our Partners Area -->


    <!-- jQuery JS -->
    <script src="js/jquery-1.12.0.min.js"></script>
    <!-- Bootstrap JS -->
    <script src="js/bootstrap.min.js"></script>
    <!-- Animate JS -->
    <script src="vendors/animate/wow.min.js"></script>
    <!-- Camera Slider -->
    <script src="vendors/camera-slider/jquery.easing.1.3.js"></script>
    <script src="vendors/camera-slider/camera.min.js"></script>
    <!-- Isotope JS -->
    <script src="vendors/isotope/imagesloaded.pkgd.min.js"></script>
    <script src="vendors/isotope/isotope.pkgd.min.js"></script>
    
    <!-- Owlcarousel JS -->
    <script src="vendors/owl_carousel/owl.carousel.min.js"></script>
    <!-- Stellar JS -->
    <script src="vendors/stellar/jquery.stellar.js"></script>
    <!-- Theme JS -->
    <script src="js/theme.js"></script>
</body>
</html>
""")
