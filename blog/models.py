from django.db import models
from django.utils import timezone

from django import forms


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Dog(models.Model):

    RESCATADO = 'Rescatado'
    DISPONIBLE = 'Disponible'
    ADOPTADO = 'Adoptado'

    STATE_CHOICES = (
        (RESCATADO, 'Rescatado'),
        (DISPONIBLE, 'Disponible'),
        (ADOPTADO, 'Adoptado'),
    )

    name = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=RESCATADO)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class AdoptionRegister(models.Model):

    owner = models.CharField(max_length=30)
    dogname = models.CharField(max_length=30)

    def publish(self):
        self.save()


    def __str__(self):
        return self.owner




ESTADO = (
        ('ADOPTADO','ADOPTADO'),
        ('RESCATADO', 'RESCATADO'),
        ('DISPONIBLE','DISPONIBLE'),
    )

REGIONES = (
        ('I de Tarapacá','I de Tarapacá'),
        ('II de Antofagasta', 'II de Antofagasta'),
        ('III de Atacama','III de Atacama'),
        ('IV de Coquimbo','IV de Coquimbo'),
        ('V de Valparaíso','V de Valparaíso'),
        ('VI del Libertador General Bernardo O’Higgins','VI del Libertador General Bernardo O’Higgins'),
        ('VII del Maule','VII del Maule'),
        ('VIII de Concepción','VIII de Concepción'),
        ('IX de la Araucanía','IX de la Araucanía'),
        ('X de Los Lagos','X de Los Lagos'),
        ('XI de Aysén del General Carlos Ibañez del Campo','XI de Aysén del General Carlos Ibañez del Campo'),
        ('XII de Magallanes y de la Antártica Chilena','XII de Magallanes y de la Antártica Chilena'),
        ('XIII Metropolitana de Santiago','XIII Metropolitana de Santiago'),
        ('XIV de Los Ríos','XIV de Los Ríos'),
        ('XV de Arica y Parinacota','XV de Arica y Parinacota'),
        ('XVI del Ñuble','XVI del Ñuble'),
    )

CIUDAD = (
		# Arica y Parinacota
        ('ARICA','ARICA'),
		('CAMARONES','CAMARONES'),
		('PUTRE','PUTRE'),
		('GENERAL LAGOS','GENERAL LAGOS'),
		# Tarapacá
		('IQUIQUE','IQUIQUE'),
		('ALTO HOSPICIO','ALTO HOSPICIO'),
		('POZO ALMONTE','POZO ALMONTE'),
		('CAMIÑA','CAMIÑA'),
		('COLCHANE','COLCHANE'),
		('HUARA','HUARA'),
		('PICA','PICA'),
		# Antofagasta
		('ANTOFAGASTA','ANTOFAGASTA'),
		('MEJILLONES','MEJILLONES'),
		('SIERRA GORDA','SIERRA GORDA'),
		('TALTAL','TALTAL'),
		('CALAMA','CALAMA'),
		('OLLAGÜE','OLLAGÜE'),
		('SAN PEDRO DE ATACAMA','SAN PEDRO DE ATACAMA'),
		('TOCOPILLA','TOCOPILLA'),
		('MARÍA ELENA','MARÍA ELENA'),
		# ATACAMA
		('COPIAPÓ','COPIAPÓ'),
		('CALDERA','CALDERA'),
		('TIERRA AMARILLA','TIERRA AMARILLA'),
		('CHAÑARAL','CHAÑARAL'),
		('DIEGO DE ALMAGRO','DIEGO DE ALMAGRO'),
		('VALLENAR','VALLENAR'),
		('ALTO DEL CARMEN','ALTO DEL CARMEN'),
		('FREIRINA','FREIRINA'),
		('HUASCO','HUASCO'),
		# COQUIMBO
		('LA SERENA','LA SERENA'),
		('COQUIMBO','COQUIMBO'),
		('ANDACOLLO','ANDACOLLO'),
		('LA HIGUERA','LA HIGUERA'),
		('PAIGUANO','PAIGUANO'),
		('VICUÑA','VICUÑA'),
		('ILLAPEL','ILLAPEL'),
		('CANELA','CANELA'),
		('LOS VILOS','LOS VILOS'),
		('SALAMANCA','SALAMANCA'),
		('OVALLE','OVALLE'),
		('COMBARBALÁ','COMBARBALÁ'),
		('MONTE PATRIA','MONTE PATRIA'),
		('PUNITAQUI','PUNITAQUI'),
		('RÍO HURTADO','RÍO HURTADO'),
		# VALPARAÍSO
		('VALPARAÍSO','VALPARAÍSO'),
		('CASABLANCA','CASABLANCA'),
		('CONCÓN','CONCÓN'),
		('JUAN FERNÁNDEZ','JUAN FERNÁNDEZ'),
		('PUCHUNCAVÍ','PUCHUNCAVÍ'),
		('QUINTERO','QUINTERO'),
		('VIÑA DEL MAR','VIÑA DEL MAR'),
		('ISLA DE PASCUA','ISLA DE PASCUA'),
		('LOS ANDES','LOS ANDES'),
		('CALLE LARGA','CALLE LARGA'),
		('RINCONADA','RINCONADA'),
		('SAN ESTEBAN','SAN ESTEBAN'),
		('LA LIGUA','LA LIGUA'),
		('CABILDO','CABILDO'),
		('PAPUDO','PAPUDO'),
		('PETORCA','PETORCA'),
		('ZAPALLAR','ZAPALLAR'),
		('QUILLOTA','QUILLOTA'),
		('CALERA','CALERA'),
		('HIJUELAS','HIJUELAS'),
		('LA CRUZ','LA CRUZ'),
		('NOGALES','NOGALES'),
		('SAN ANTONIO','SAN ANTONIO'),
		('ALGARROBO','ALGARROBO'),
		('CARTAGENA','CARTAGENA'),
		('EL QUISCO','EL QUISCO'),
		('EL TABO','EL TABO'),
		('SANTO DOMINGO','SANTO DOMINGO'),
		('SAN FELIPE','SAN FELIPE'),
		('CATEMU','CATEMU'),
		('LLAILLAY','LLAILLAY'),
		('PAQUEHUE','PANQUEHUE'),
		('PUTAENDO','PUTAENDO'),
		('SANTA MARÍA','SANTA MARÍA'),
		('QUILPUÉ','QUILPÚÉ'),
		('LIMACHE','LIMACHE'),
		('OLMUÉ','OLMUÉ'),
		('VILLA ALEMANA','VILLA ALEMANA'),
		# LIBERTADOR BERNARDO O´HIGGINS
		('RANCAGUA','RANCAGUA'),
		('CODEGUA','CODEGUA'),
		('COINCO','COINCO'),
		('COLTAUCO','COLTAUCO'),
		('DOÑIHUE','DOÑIHUE'),
		('GRANEROS','GRANEROS'),
		('LAS CABRAS','LAS CABRAS'),
		('MACHALÍ','MACHALÍ'),
		('MALLOA','MALLOA'),
		('MOSTAZAL','MOSTAZAL'),
		('OLIVAR','OLIVAR'),
		('PEUMO','PEUMO'),
		('PICHIDEGUA','PICHIDEGUA'),
		('QUINTA DE TILCOCO','QUINTA DE TILCOCO'),
		('RENGO','RENGO'),
		('REQUÍNOA','REQUÍNOA'),
		('SAN VICENTE','SAN VICENTE'),
		('PICHILEMU','PICHILEMU'),
		('LA ESTRELLA','LA ESTRELLA'),
		('LITUECHE','LITUECHE'),
		('MARCHIHUE','MARCHIHUE'),
		('NAVIDAD','NAVIDAD'),
		('PAREDONES','PAREDONES'),
		('SAN FERNANDO','SAN FERNANDO'),
		('CHÉPICA','CHÉPICA'),
		('CHIMBARONGO','CHIMBARONGO'),
		('LOLOL','LOLOL'),
		('NANCAGUA','NANCAGUA'),
		('PALMILLA','PALMILLA'),
		('PERALILLO','PERALILLO'),
		('PLACILLA','PLACILLA'),
		('PUMANQUE','PUMANQUE'),
		('SANTA CRUZ','SANTA CRUZ'),
		#MAULE
		('TALCA','TALCA'),
		('CONSTITUCIÓN','CONSTITUCIÓN'),
		('CUREPTO','CUREPTO'),
		('EMPEDRADO','EMPEDRADO'),
		('MAULE','MAULE'),
		('PELARCO','PELARCO'),
		('PENCAHUE','PENCAHUE'),
		('RÍO CLARO','RÍO CLARO'),
		('SAN CLEMENTE','SAN CLEMENTE'),
		('SAN RAFAEL','SAN RAFAEL'),
		('CAUQUENES','CAUQUENES'),
		('CHANCO','CHANCO'),
		('PELLUHUE','PELLUHUE'),
		('CURICÓ','CURICÓ'),
		('HUALAÑÉ','HUALAÑÉ'),
		('LINCANTÉN','LINCANTÉN'),
		('MOLINA','MOLINA'),
		('RAUCO','RAUCO'),
		('ROMERAL','ROMERAL'),
		('SAGRADA FAMILIA','SAGRADA FAMILIA'),
		('TENO','TENO'),
		('VICHUQUÉN','VICHUQUÉN'),
		('LINARES','LINARES'),
		('COLBÚN','COLBÚN'),
		('LONGAVÍ','LONGAVÍ'),
		('PARRAL','PARRAL'),
		('RETIRO','RETIRO'),
		('SAN JAVIER','SAN JAVIER'),
		('VILLA ALEGRE','VILLA ALEGRE'),
		('YERBAS BUENAS','YERBAS BUENAS'),
		# ÑUBLE
		('COBQUECURA','COBQUECURA'),
		('COELMU','COELMU'),
		('NINHUE','NINHUE'),
		('PORTEZUELO','PORTEZUELO'),
		('QUIRIHUE','QUIRIHUE'),
		('RÁNQUIL','RÁNQUIL'),
		('TREGUACO','TREGUACO'),
		('BULNES','BULNES'),
		('CHILLÁN VIEJO','CHILLÁN VIEJO'),
		('EL CARMEN','EL CARMEN'),
		('PEMUCO','PEMUCO'),
		('PINTO','PINTO'),
		('QUILLÓN','QUILLÓN'),
		('SAN IGNACIO','SAN IGNACIO'),
		('YUNGAY','YUNGAY'),
		('COIHUECO','COIHUECO'),
		('ÑIQUÉN','ÑIQUÉN'),
		('SAN CARLOS','SAN CARLOS'),
		('SAN FABIÁN','SAN FABIÁN'),
		('SAN NICOLÁS','SAN NICOLÁS'),
		# BIOBÍO
		('CONCEPCIÓN','CONCEPCIÓN'),
		('CORONEL','CORONEL'),
		('CHIGUAYANTE','CHIGUAYANTE'),
		('FLORIDA','FLORIDA'),
		('HUALQUI','HUALQUI'),
		('LOTA','LOTA'),
		('PENCO','PENCO'),
		('SAN PEDRO DE LA PAZ','SAN PEDRO DE LA PAZ'),
		('SANTA JUANA','SANTA JUANA'),
		('TALCAHUANO','TALCAHUANO'),
		('TOMÉ','TOMÉ'),
		('HUALPÉN','HUALPÉN'),
		('LEBU','LEBU'),
		('ARAUCO','ARAUCO'),
		('CAÑETE','CAÑETE'),
		('CONTULMO','CONTULMO'),
		('CURANILAHUE','CURANILAHUE'),
		('LOS ÁLAMOS','LOS ÁLAMOS'),
		('TIRÚA','TIRÚA'),
		('LOS ÁNGELES','LOS ÁNGELES'),
		('ANTUCO','ANTUCO'),
		('CABRERO','CABRERO'),
		('LAJA','LAJA'),
		('MULCHÉN','MULCHÉN'),
		('NACIMIENTO','NACIMIENTO'),
		('NEGRETE','NEGRETE'),
		('QUILACO','QUILACO'),
		('QUILLECO','QUILLECO'),
		('SAN ROSENDO','SAN ROSENDO'),
		('SANTA BÁRBARA','SANTA BÁRBARA'),
		('TUCAPEL','TUCAPEL'),
		('YUMBEL','YUMBEL'),
		('ALTO BIOBÍO','ALTO BIOBÍO'),
		# LA ARAUCANÍA
		('TEMUCO','TEMUCO'),
		('CARAHUE','CARAHUE'),
		('CUNCO','CUNCO'),
		('CURARREHUE','CURARREHUE'),
		('FREIRE','FREIRE'),
		('GALVARINO','GALVARINO'),
		('GORBEA','GORBEA'),
		('LAUTARO','LAUTARO'),
		('LONCOCHE','LONCOCHE'),
		('MELIPEUCO','MELIPEUCO'),
		('NUEVA IMPERIAL','NUEVA IMPERIAL'),
		('PADRE LAS CASAS','PADRE LAS CASAS'),
		('PERQUENCO','PERQUENCO'),
		('PITRUFQUÉN','PITRUFQUÉN'),
		('PUCÓN','PUCÓN'),
		('SAAVEDRA','SAAVEDRA'),
		('TEODORO SCHMIDT','TEODORO SCHMIDT'),
		('TOLTÉN','TOLTÉN'),
		('VILCÚN','VILCÚN'),
		('VILLARICA','VILLARICA'),
		('CHOLCHOL','CHOLCHOL'),
		('ANGOL','ANGOL'),
		('COLLIPULLI','COLLIPULLI'),
		('CURACAUTÍN','CURACAUTÍN'),
		('ERCILLA','ERCILLA'),
		('LONQUIMAY','LONQUIMAY'),
		('LOS SAUCES','LOS SAUCES'),
		('LUMACO','LUMACO'),
		('PURÉN','PURÉN'),
		('RENAICO','RENAICO'),
		('TRAIGUÉN','TRAIGUÉN'),
		('VICTORIA','VICTORIA'),
		# LOS RÍOS
		('VALDIVIA','VALDIVIA'),
		('CORRAL','CORRAL'),
		('LANCO','LANCO'),
		('LOS LAGOS','LOS LAGOS'),
		('MÁFIL','MÁFIL'),
		('MARIQUINA','MARAQUINA'),
		('PAILLACO','PAILLACO'),
		('PANQUIPULLI','PANGUIPULLI'),
		('LA UNIÓN','LA UNIÓN'),
		('FUTRONO','FUTRONO'),
		('LAGO RANCO','LAGO RANCO'),
		('RÍO BUENO','RÍO BUENO'),
		# LOS LAGOS
		('PUERTO MONTT','PUERTO MONTT'),
		('CALBUCO','CALBUCO'),
		('COCHAMÓ','COCHAMÓ'),
		('FRESIA','FRESIA'),
		('FRUTILLAR','FRUTILLAR'),
		('LOS MUERMOS','LOS MUERMOS'),
		('LLANQUIHUE','LLANQUIHUE'),
		('MAULLÍN','MAULLÍN'),
		('PUERTO VARAS','PUERTO VARAS'),
		('CASTRO','CASTRO'),
		('ANCUD','ANCUD'),
		('CHONCHI','CHONCHI'),
		('CURACO DE VÉLEZ','CURACO DE VÉLEZ'),
		('DALCAHUE','DALCAHUE'),
		('PUQUELDÓN','PUQUELDÓN'),
		('QUEILÉN','QUEILÉN'),
		('QUELLÓN','QUELLÓN'),
		('QUEMCHI','QUEMCHI'),
		('QUINCHAO','QUINCHAO'),
		('OSORNO','OSORNO'),
		('PUERTO OCTAY','PUERTO OCTAY'),
		('PURRANQUE','PURRANQUE'),
		('PUYEHUE','PUYEHUE'),
		('RÍO NEGRO','RÍO NEGRO'),
		('SAN JUAN DE LA COSTA','SAN JUAN DE LA COSTA'),
		('SAN PABLO','SAN PABLO'),
		('CHAITÉN','CHAITÉN'),
		('FUTALEUFÚ','FUTALEUFÚ'),
		('HUALAIHUÉ','HUALAIHUÉ'),
		('PALENA','PALENA'),
		# AYSÉN
		('COIHAIQUE','COIHAIQUE'),
		('LAGO VERDE','LAGO VERDE'),
		('AYSÉN','AYSÉN'),
		('CISNES','CISNES'),
		('GUAITECAS','GUAITECAS'),
		('COCHRANE','COCHRANE'),
		('O´HIGGINS','O´HIGGINS'),
		('TORTEL','TORTEL'),
		('CHILE CHICO','CHILE CHICO'),
		('RÍO IBÁÑEZ','RÍO IBÁÑEZ'),
		# MAGALLANES Y ANTÁRTICA CHILENA
		('PUNTA ARENAS','PUNTA ARENAS'),
		('LAGUNA BLANCA','LAGUNA BLANCA'),
		('RÍO VERDE','RÍO VERDE'),
		('SAN GREGORIO','SAN GREGORIO'),
		('CABO DE HORNOS (EX NAVARINO)','CABO DE HORNOS (EX NAVARINO)'),
		('ANTÁRTICA','ANTÁRTICA'),
		('PORVENIR','PORVENIR'),
		('PRIMAVERA','PRIMAVERA'),
		('TIMAUKEL','TIMAUKEL'),
		('NATALES','NATALES'),
		('TORRES DEL PAINE','TORRES DEL PAINE'),
		# METROPOLITANA DE SANTIAGO
		('CERRILLOS','CERRILLOS'),
		('CERRO NAVIA','CERRO NAVIA'),
		('CONCHALÍ','CONCHALÍ'),
		('EL BOSQUE','EL BOSQUE'),
		('ESTACIÓN CENTRAL','ESTACIÓN CENTRAL'),
		('HUECHURABA','HUECHURABA'),
		('INDEPENDENCIA','INDEPENDENCIA'),
		('LA CISTERNA','LA CISTERNA'),
		('LA FLORIDA','LA FLORIDA'),
		('LA GRANJA','LA GRANJA'),
		('LA PINTANA','LA PINTANA'),
		('LA REINA','LA REINA'),
		('LAS CONDES','LAS CONDES'),
		('LO BARNECHEA','LO BARNECHEA'),
		('LO ESPEJO','LO ESPEJO'),
		('LO PRADO','LO PRADO'),
		('MACUL','MACUL'),
		('MAIPÚ','MAIPÚ'),
		('ÑUÑOA','ÑUÑOA'),
		('PEDRO AGUIRRE CERDA','PEDRO AGUIRRE CERDA'),
		('PEÑALOLÉN','PEÑALOLÉN'),
		('PROVIDENCIA','PROVIDENCIA'),
		('PUDAHUEL','PUDAHUEL'),
		('QUILICURA','QUILICURA'),
		('QUINTA NORMAL','QUINTA NORMAL'),
		('RECOLETA','RECOLETA'),
		('RENCA','RENCA'),
		('SAN JOAQUÍN','SAN JOAQUÍN'),
		('SAN MIGUEL','SAN MIGUEL'),
		('SAN RAMÓN','SAN RAMÓN'),
		('VITACURA','VITACURA'),
		('PUENTE ALTO','PUENTE ALTO'),
		('PIRQUE','PIRQUE'),
		('SAN JOSÉ DE MAIPO','SAN JOSÉ DE MAIPO'),
		('COLINA','COLINA'),
		('LAMPA','LAMPA'),
		('TILTIL','TILTIL'),
		('SAN BERNARDO','SAN BERNARDO'),
		('BUIN','BUIN'),
		('CALERA DE TANGO','CALERA DE TANGO'),
		('PAINE','PAINE'),
		('MELIPILLA','MELIPILLA'),
		('ALHUÉ','ALHUÉ'),
		('CURACAVÍ','CURACAVÍ'),
		('MARÍA PINTO','MARÍA PINTO'),
		('SAN PEDRO','SAN PEDRO'),
		('TALAGANTE','TALAGANTE'),
		('EL MONTE','EL MONTE'),
		('ISLA DE MAIPO','ISLA DE MAIPO'),
		('PADRE HURTADO','PADRE HURTADO'),
		('PEÑAFLOR','PEÑAFLOR'),
	)



TIPOVIVIENDA = (
        ('Casa Patio Grande','Casa Patio Grande'),
        ('Casa Patio Pequeño', 'Casa Patio Pequeño'),
        ('Casa Sin Patio','Casa Sin Patio'),
        ('Departamento','Departamento'),
    )











class Adoptante(models.Model):
	correo = models.EmailField()
	run = models.CharField(max_length=10, primary_key=True)#validators=[run_validation])
	nombreCompleto = models.CharField(max_length=100)
	telefono = models.CharField(max_length=9)
	region = models.CharField(max_length=100, choices=REGIONES)
	vivienda = models.CharField(max_length=100, choices=TIPOVIVIENDA)
	def __str__(self):
		return self.correo

class Adoptado(models.Model):
	idPerro = models.AutoField(primary_key=True)
	#fotografia = models.ImageField()
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=30)
	descripcion = models.TextField()
	estado = models.CharField(max_length=10, choices=ESTADO)
	def __str__(self):
		return self.nombre        