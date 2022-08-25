import json, re, csv, os, unicodedata, requests, string, platform
import ijson
from bs4 import BeautifulSoup
from pathlib import Path
from six.moves.urllib.request import urlopen

import pandas as pd

import urllib.request

import numpy as np

from requests import request
from urllib.error import URLError

from itertools import filterfalse
import json, re, csv, unicodedata, string, sys, glob
from pathlib import Path
import pandas as pd
from subprocess import check_output
#----------------------------------------------------------
customers_google_cloud = '''
17 Media, 20th Century Fox, 33Bondi, 3PM Solutions, 4INFO, 6 River Systems, 8BIT, 90 Seconds, 99, 99acres, A2X, AB InBev, AB Tasty, ABAX, ABN AMRO, Absolutdata, AccuWeather, Aclima, Adcash, Adler Planetarium, Aerospike, Aerotech, Affini-Tech, Afinis (NACHA), AfterShip, AgroStar, AgroTools, AIB, AirAsia, Airbus Defence and Space, AISportsWatch, Akeneo, akippa, Akselos, AlacrisTheranostics, Alcide, Allcyte, Allianz, AllSaints, Allstate, Allthecooks, Almundo, AloTech, Alpega Group, Alpha Vertex, Alstom, Amadeus, Ambra Health, American Cancer Society, American Eagle Outfitters, Ananda Development, Anaplan, Andela, AngkasaPura Supports, Aniview, Answear, Antvoice, AnyMind Group, AODocs, Apester, APImetrics, APMEX, Inc., AppLift, AppsFlyer, AppyParking, Archer First Response Systems, Arcules, Area 1 Security, Arity, Ascend Money, ASML, AT&T, ATB Financial, Athena Breast Health Network, Ather Energy, Atlassian, Atomic Fiction, Atomx, Aucor, Augury, AUKA, Autheos, Auto Trader (UK), Autodesk, Avanza, Avaya, AVEVE Group, aWhere, AXA Switzerland, Azavea, Azimut, Backflip Studios, Banca Mediolanum, Banco Davivienda, Band Aid 30, Bank BRI, Banlinea, Barilla, Bazaarvoice, BBM/Creative Media Works, BBVA Microfinance Foundation, Bci, BeDataDriven, Bending Spoons, BenefícioFácil, Betfair US/TVG Network, Better Business Bureau, BetterCloud, Bigbasket, BigChange, Billie, BioDot, Bioz, Birdz, Bitrix24, Bitsmedia, Black Knight, Blend, Blibli.com, Blockchain.com, Bloomberg, Blossom.io, Blue Apron, Bluecore, BlueStacks, Body & Fit, bofrost, Bombora, Bonnier Publications, Boo-box, boodmo, BOTfriends, BotMaker, BPAY Group, BPER, BQ, Brainy Bunch, Brandfolder, Brandwatch, Breaktime, BreezoMeter, Brightcove, BrightInsight, Bringg, Broad Institute, Broadmann17, Brønnøysund Register Center (BRREG), BroodMinder, Brut, Bugaboo, Bugsnag, Buildertrend, Built, Bulweria, BURGER KING® Germany, BUTIK., Cabify, Caja Los Andes, California Design Den, CanaccordGenuity, Canada Games Council, Canam Group, Canberra Public Schools, CareerBuilder, Cargills Bank, Carousell, Cars.com, Carussel, Casa della Salute, Castbox, Catalant, Celestica, CENTURY 21 Canada, Chainstack, Change Healthcare, CHANGING.AI, Chapters Health System, Charity: Water, Charles Schwab, Chas Everitt, Chauffeur Privé, Chicago Department of Transportation, Chicago Technology Advisors, Chicory, Chilean Health Ministry, Chironix, Chope, Citrix, City of Chattanooga, City of Los Angeles, City of Memphis, CL (Chantelle Lingerie), Clarkstown Police Department, Classcraft, Clear Labs, ClearSky Data, Cleveland Clinic, CLEW, ClimaCell, Clipchamp, Cloud 66, Cloud9 Technologies, CloudLock, CMMS, CoinGecko, Coinhako, Colgate-Palmolive, College Recruiter, COLLINS, Color, Colorado Center for Personalized Medicine, Colorado Statewide Internet Portal Authority (SIPA), Comanche County Memorial Hospital, commercetools, Compara Online, Computerlogy, Concord Hospitality, Conductor Tech, Connekt, Conrad Electronic, Converga, Coolblue, Cornershop, Cosmo Tech, Craveable Brands, Crocus Energy, Crystalloids, Current, Curves, Custom Ink, Dacsee, Daffodil, Dámejídlo, DataStax, DB Corp, Dedact, Deep Silver FISHLABS, Deep Sky Vineyard, Defy Ventures, Degoo, Deliveroo, Derive Systems, Descartes Labs, Descript, Deskforce, Desktop Genetics, DIA, Dialpad, Digiexam, Digital Dimension, Digital District, Digital Mobility Solutions/PickMe, DiMuto, DIRECTV, Discount Bank, DLR, DNAstack, doc.ai, Doctor on Demand, Doctor.com, Docxonomy, Dolphin Technologies, Domino’s, DotComm / Omaha + Douglas County, Douglas and Gordon, Dow Jones, Dozens, DPD, DPD UK, Dr. Agarwal Eye Hospital, Drayson Technologies, Drouot Digital, DSI Solutions, Dun & Bradstreet, Duo Security, E Fundamentals, Eagle County Government, Early Birds, Easypromos, eBay, ECDPM, Edebé, EDF, EDP, Energias De Portugal, eDreams ODIGEO, EE, Eldorado, ELEX, ELI WMS, Emarsys, Encore, Endowus, Enel Codensa, Energyworx, Enevo, Entelgy, Equinix, Ervia, Esdemarca, eSilicon Corporation, eToroX, EULEN, Euroclean, Euromaster, Eurostar, Everflow, Evernote, Evite, Exact, Experian, Expliseat, Exponea, Ezakus, FACEIT, Fairfield County Schools, Feedly, Feralpi, Ferrero, FFF Enterprises, Filmograph, FiloBlu, Finalsite, FinancieraIndependencia FINDEP, Finnomena, First Data, First Tech Federal Credit Union, Fit Analytics, Fix Studio, Fleetminder, FlexyBeauty, Flinks, floreysoft, Fluidly, Flywheel, FNM Group, FOMO Pay, Fontana Gruppo, fonYou, Forbes, Forthright, Foundation for Precision Medicine, Fracarro, Framestore, Frazer, Freestar, FTD Companies, Fujitec, Fusionex, GABA, Gallagher Communication, Game Insight, Gamesys, GANT, GearLaunch, GEEV, Genbook, General Mobile, Generali Hungary, Genesys, Geneva Business School, Gennion, Geopointe, Georgetown University, Georgia State University, Geotab, Getaround, GetQuanty, GF Hoteles, GGN, Gigya, GitLab, Glitnir Ticketing, Global Fishing Watch, Global Payments, GlobalLogic, GlobalX, Globe Telecom, Glowforge, GoCardless, Goibibo, GO-JEK, Good Friday Appeal, Goodbye Kansas, GoOpti, Gordon Food Service, Gorgias, Gosu.ai, GRAS, Grasshopper, GreatSchools!, Greedy Game, Grofers, GroupeDauphinoise, Groupe Le Monde, Grupo Colon Gerena, GrupoNavent SRL, GSMA, Guidion, GungHo, HackerOne, Hafslund, happn, Harambee, Hare Digital, Hays, Hearst, Herfy, Hermes, HerMin Textile, Hero MotoCorp, High 5 Games, Hike, Hilton HHonors, Hire1, HKTaxi, Hoff, Homer Central School District, honestbee, Hotel Urbano, HP, Inc., HSBC, HTC, Hubstairs, HUDORA, Humana, Hunterdon Healthcare, Hurley Medical Center, Hyperconnect, ibibo Group, iCarAsia, icitizen, ICON Health and Fitness, IDEXX Laboratories, iGenius, iGuzzini, Imagia, IndiaMART, Infectious Media, Infoxchange, Ingedata, Ingenious, Innoplexus, Innovela, Inspire Digital, Instal, InstantSearch+, Institute for Systems Biology, IntegraGen, Interactions Marketing, InteractiveTel, IT Convergence, ITV, Jackson National, Jargon PR, Jayride, JBGoodwin, Jelly Button, Jerusalem Post Group, Jobrapido, Jobtome, Johnson & Johnson, Juiced TV, JumpCloud, Jupiter Orthopedics & Sports Medicine, Just Develop It, Kadaxis, KAESER COMPRESSORS, Kahuna, Kaiko, Kao AEMEA, Kapiche, Kaplan, Kapten, Kasturba Hospital / Manipal Group, KBZ Bank, Keller Williams, Keos, KeyBank, Khan Academy, Khan Bank, King, Kings Transport, Kingston and Sutton London Borough Councils, Kinsta, KIPP, Kisan Network, KiSSFLOW, Kiwi.com, KKBOX, KNOLSKAPE, Knorex, Kofera, Kolide, Kolumbus, Konga, KPN, Krikey, Kronoshop, Krungsri Consumer, Kurio, L&T Financial Services, L.L.Bean, L’Appart Fitness, Label Insight, Laboratory for Traffic and Transport Engineering (LICIT), LafargeHolcim, Lahey, LANSA, LATAM Airlines, LeadPages, Leanplum, LenddoEFL, L'Equipe, Leroy Merlin, Les Echos, LG CNS, LiftIgniter, LINE GAMES, LiveHive, LivePerson, Living Consumer Products, Loblaw, Logflare, LogoGrab, London Borough of Barking and Dagenham, loveholidays, Loyal Guru, LSA Courtage, Lucille Games, Lupa, Lush, Lyft, Lytics, M.video, mabl, Macquarie Bank, Macquarie Group, Madfinger Games, Madgic, Madison + Fifth, Magazine Luiza, Magma Partners, Mailjet, MainAd, Maison du Monde, Mako Design + Invent, Malaysia Airlines, Maldives Pension Administration Office, MANA Partners, ManagedMethods, Manchester City Council, Map of Life, MapBiomas, MarineTraffic, MarketCheck, Marks & Spencer, Maropost, mashme.io, Mass Rapid Transit Corporation, Maven Wave, Max Kelsen, Maxeda, Maxwell Plus, McClatchy, McKesson, MD Insider, MD.ai, MediaMarktSaturn, MediaNews Group, MedXM, MeilleursAgents, MeisterLabs, Melsoft, Merantix, Mercado Libre, Mercari, Meredith, MetGlobal, Metro, Middlesex Health, MightyHive, Milford, Mimiboard, MINDBODY, Mindvalley, Minka, Mito.ai, Mitsui, mixi, Inc., Mixpanel, MobileOne, MokiMobility, MOKLI, Moloco, Monex, MoneySuperMarket, Montreal Museum of Fine Arts, Monzo, Morellato Group, Morningstar, Morrisons, Motorola, Moviebill, Mozio, Multiasistencia, Multiplay, MultiScale Health Networks, MutuaMadrileña, MWM, MyCujoo, MyDoc, MyRepublic, mytaxi, NaCesty.cz, Namshi, Narvar, National Bank of Pakistan, National Institute on Aging, National Institutes of Health, Nationwide, Nationwide Insurance, Natura, Network Rail High Speed, New Media Investment Group, News Limited, Next Games, Next Limit, NextPlane, NH Hotels, Niantic, Inc., Nielsen, Ninja Van, NIRAMAI Health Analytix, Noberasco, Nodeflux, Nojima, Nomanini, NomNomNow, Northern Grampians Shire Council, Northrop Grumman, Northumberland County Council, Noxxon Sat, Nozzle, NTT Docomo, NU.nl, Nubbius, Nubian Skin, Numadic, Nuna, NYC Cyber Command, NZTA, Oasis Games, Objenious, Ocado, Oddschecker, Oden Technologies, OFX, Oledcomm, Omaha and Douglas County, Omio, Omise, omni:us, Omnigen, On Center Software, Oncology Venture, OneAD, OnlineTours, Open House, OpenGov, OpenX, Opportunity Fund, Optiva, Orange, OrangeTee, OspedaliRiunitid’Ancona, OTA Insight, Outbrain, Owlin, Øyedrops, Packlink, PaGaLGuY, Palatinate Group, Panda Restaurant Group, Panorays, Pantheon, PaperCut, Partner, PathMotion, Paxport, PayPal, Pegadaian, Pendo, PerimeterX, Perx Technologies, Pex, Philips, PicMonkey, PIK Group, Piramis, Pitney Bowes, Pivotal, PIXNET, Pizza Hut, Pizza Hut India, Planet, Plantronics, Platform161, Pluribus Labs, Pluto7, PNB (Permodalan Nasional Berhad), Pocket Gems, Pod Trackers, Podo, Polydice, Portal Telemedicina, Posterscope, Power Ledger, Power Poetry, Powerspace, Pozible, PPS, PrestaShop, Primer Group, Priori Data, Promevo, Properati, Proximis, Pulse Secure, PulsePoint, Purplle, PwC Australia, Q42, QAD, Qlue, Qopius, QSearch, QuantConnect, Quantum Metric, Qubit, Quby, Queensland University of Technology, Questar, Quimmco, Quizlet, R/GA, RAD-AID, Ragic, Rakuten-Viki, Ramco Cements, Randstad, Rapido, Rave, Ravelin, Rawson Properties, Rayark, Raycatch, RealMassive, Rebel Foods, RecruitMilitary, Recurly, Recursion Pharmaceuticals, Red Bull X-Alps, Redboat, redBus, RedDoorz, Redfin, Referral Saasquatch, Reliance Nippon Life Asset Management, RelianceUnited, Rent.com.au, Rentokil, Repl.it, ResultadosDigitais, Revolut, REWE digital, Rezco, RLE International, rMark Bio, RMI Insights, Rome2rio, Routard.com, Route4Me, Rovaniemi, Rovio, Royal Resort, Royal Technologies, Ruangguru, Rush University Medical Center, Rustomjee, Sacyr, Safaricom, SafeliteAutoglass, Sage, SageMathCloud, Sajari, SalesSeek, Sandvik, Sanmina, Santehnika, Sara Assicurazioni, SBT, Schadegarant, School Loop, scitis.io, Scotiabank, Scotts Miracle-Gro Company, Scout24, Screenz, Scribendi, SeaRates, SecciónAmarilla, Sedex, Seeff Properties, Seenit, Sefamerve, SelectMedia, SEM, Semios, Sensormatic, Sertis, Service NSW, Servicio de Salud San Vicente, ServiciosLogísticos de Combustibles de Aviación (SLCA), SFO, Shamir Optical, ShareThis, Shazam, Sheboygan County, Shine Technologies, Shutterfly, Siemens, Sightly, Signify, Simperium, Simplify, Simprints, Singapore Press Holdings, Sirplay, Sittercity, Sky Italia, Sky News, Sky U.K., Skyscanner, Sleekr, Smart Parking, Snapfrozen, SoCash, Soccer Manager, Softonic, Sojern, Solar Impulse, Solitex, SongPop, Sony Music, Sony Pictures Imageworks, SoulCycle, Soundtrack Your Brand, South China Morning Post, SparkCognition, Spendee, Spideo, SPINS, Spiraledge, Spoke, Sport Singapore, Spotify, Square, St. Benedict Technology Consortium (SBTC), Stanford Center for Cognitive and Neurobiological Imaging, Stanford University’s Center of Genomics and Personalized Medicine, Staples, Star Media Group, Starling Bank, Starmaker Interactive, State Auto Insurance Companies, State of Arizona, Stitch Labs, Storytel, Streak, Streamroot, StreamShark, Streem, StreetSmart, Style Theory, SulAmérica, Sun Surveyor, Sunman Group, Swiggy, Swiss Life, Swiss Steel, Swisscom, Symphony, Système U, TabTale, Taiwan Taxi, Talgo, Tamr, Taranis, Target, Teads, TeamSnap, Teamwork Commerce, Teemo, Telegraph Media Group, Telenor, Telepass, TeletracNavman, Telia, Telstra, Tencent Africa, TenX, Tera (Campus SP), Teridion, The Climate Corporation, The F.C. Tucker Company, The Football Association, The Home Depot, The New York Times, The Queen's Fund, The Regional Government of Castilla-La Mancha, The Roche Group, The Walt Disney Co., ThinkData Works, Thomson Reuters, ThoughtWorks, Tick Talk Soft, Ticketmaster, Tieto, tiramizoo, TisoBlackstar, Tixsee, T-Mobile, TNO, Tokopedia, Topcoder, Torch, Toyota, Trace One, Trade Me, Tradebridge, TradeIt, Tradier, TransContainer, TranslateLive, travel audience, TravelgateX, Travello App, Traveloka, Travis Perkins, Travix, Travlytix, Trax, Treeptik, Tripping, Truecaller, TrueCar, Trulia, Tulip, Tute Genomics, Twiddy& Company, Twinkl, Twitter, U.S. Cellular, Ubamarket, Ubisoft, Ulmart, Umbo Computer Vision, Unacast, UniCredit, Unilog, UntieNots, Up, Upwire, Urban Infrastructure, Urban Science, UrbanSitter, Vagabond, Vallie, Valora, Vantiv, Vendasta, Veneto Region, Vente-Exclusive, Veolia, Vertex, Vestiaire Collective, Via, Viant, Vibrant Credit Union, Vichey Catalan, VictoriaPlum.com, Vidyo, Viessmann, Vimeo, Virgin Active, ViSenze, Vodafone, VOGSY, Volusion, Vonage, Voodoo, Voximplant, VTCSecure, Vuclip, Walgreens, Warburtons, WatchRx, Waymo, Webdox, Webydo, Weepee, Weight Watchers, Wellframe, wellio, West Corporation, WeVideo, Whirlpool, Whisper, Wind Tre, Wix, wnDirect, Wolters Kluwer Transport Services, Wondermall, Woolworths, Wootric, Workiva, World Surf League, Worldline, WP Engine, XITE, YMCA of San Francisco, York Risk Services, YouGenomics, YoungCapital, yReceipts, Zagat, Zain, Zalando, Zalora, Zeiss, Zenconnect, Zenly, Zenoss, zest HACCP, Zesty.io, Zoological Society of London, ZoomInfo, Zubie, zulily, Zync, Zype, Zzish.
'''
#----------------------------------------------------------
def removen(string):
    for m in ('\n', '\r'):
        clean_string = re.sub(m, '', string)
        clean_string = clean_string.replace(m, '')
        clean_string = clean_string.rstrip()
        clean_string = clean_string.strip(m)
        clean_string = re.sub(m,' ', clean_string)
        mymano = ''
        for x in clean_string:
            mymano += ''+ x
        return mymano
#---------------------------------------------------
def fullyqualifydirs(mylist):
    mydircode = N.join(mylist)
    return mydircode
#---------------------------------------------------

myos = platform.system()

if (myos == "Linux" or myos == "linux2"):
    # linux
    N="/"
    homedirectory = str(Path.home())
    print(homedirectory)
    
    mylist = [ homedirectory, 'serpapi/python/app/nature-labs/customerbase' ]
    basedir = fullyqualifydirs(mylist)
    print(basedir)
elif myos == "win32" or myos == "Windows":
    # Windows 
    N="\\"    
    basedir = 'C:\\serpapi\\python\\app\\nature-labs\\customerbase'  
#--------------------------------------------------------------
if not basedir:
    basedir = os.getcwd()
#-------------------------------------------------------------------------------------
mylist = [basedir, 'initialization.py']
initialdirectoryconfig = fullyqualifydirs(mylist)
#-------------------------------------------------------------------------------------
getdirectory = removen(check_output([sys.executable, initialdirectoryconfig], universal_newlines=True))
#-----------------------------------------------------
def mkingdirs(givenlist):
    mymanog = N.join(givenlist)
    mk_dir = Path(mymanog)
    mk_dir.mkdir(parents=True, exist_ok=True)
    return mk_dir
#-------------------------------------------------------------------
myoutdir = [getdirectory, 'output' ]
outputdir = mkingdirs(myoutdir)
#-------------------------------------------------------------------------------
csvdatasheet = ("{}{}".format('Google_Cloud_Customers_Report','.csv'))
mylist = [ getdirectory, 'output' , csvdatasheet ]
templesserpapifilterdata = fullyqualifydirs(mylist)
#-------------------------------------------------------------------------------
google_customers = []
for k in customers_google_cloud.split(','):
    google_customers.append(removen(k))
modetw = 'w' if k else 'a'
header = ['Google Cloud Customers']
tf = pd.DataFrame(google_customers)
tf.to_csv(templesserpapifilterdata, encoding='utf-8', mode=modetw, index=False, header = header)