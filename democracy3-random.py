#!/usr/bin/python3.6
import random

#TODO create all-encompassing name file
#TODO images
#TODO generate a bunch of missions per run
#TODO update license once all content (images, name, etc) are original

class Policy:
    def __init__(self,name,floor,ceiling,chance):
        self.name=name
        self.floor=floor
        self.ceiling=ceiling
        self.chance=chance
        
    def generate(self):
        if r(1,CHANCES)<=self.chance:
            return f'{self.name}={r(self.floor,self.ceiling)/100}\n' 
        return ''

CHANCES=6
OPTIONS=['COMPULSORY_VOTING','MONARCHY','HURRICANES','EARTHQUAKES','FOXES']
POLICIES=[
    Policy('AbortionLaw',1,1,1),
    Policy('AdultEducationSubsidies',73,73,1),
    Policy('AgricultureSubsidies',21,75,4),
    Policy('AirlineTax',12,12,1),
    Policy('ArtsSubsidies',36,36,1),
    Policy('AlcoholLaw',16,60,2),
    Policy('AlcoholTax',20,40,4),
    Policy('ArmedPolice',20,58,3),
    Policy('BanSundayShopping',74,74,1),
    Policy('BiofuelSubsidies',75,75,1),
    Policy('BorderControls',40,75,2),
    Policy('BusLanes',50,50,1),
    Policy('CCTVCameras',20,80,4),
    Policy('CapitalGainsTax',20,40,5),
    Policy('CarTax',20,40,2),
    Policy('CarbonTax',40,40,1),
    Policy('CarEmmissionsLimits',75,75,1),
    Policy('ChildBenefit',40,85,5),
    Policy('CitizenshipTests',22,54,3),
    Policy('CleanEnergySubsidies',25,86,3),
    Policy('CommunityPolicing',55,63,2),
    Policy('CorporationTax',21,39,6),
    Policy('Creationism',40,75,2),
    Policy('DeathPenalty',5,83,1),
    Policy('DisabilityBenefit',67,83,2),
    Policy('FaithSchoolSubsidies',32,32,1),
    Policy('FoodStamps',60,82,1),
    Policy('FoodStandards',52,60,2),
    Policy('ForeignAid',20,40,6),
    Policy('ForeignInvestorTaxBreaks',10,22,2),
    Policy('Gambling',50,82,2),
    Policy('GatedCommunities',50,60,2),
    Policy('HandgunLaws',20,40,2),
    Policy('HybridCarsInitiative',25,25,1),
    Policy('IDCards',60,60,1),
    Policy('IncomeTax',25,62,6),
    Policy('InheritanceTax',20,40,5),
    Policy('IntelligenceServices',72,78,2),
    Policy('JuryTrial',50,80,6),
    Policy('LabourLaws',10,85,3),
    Policy('LegalAid',50,75,6),
    Policy('LegaliseProstitution',1,50,3),
    Policy('MaternityLeave',65,84,3),
    Policy('MicrogenerationGrants',50,95,2),
    Policy('MilitarySpending',32,100,4),
    Policy('Narcotics',0,10,5),
    Policy('OrganicSubsidy',70,70,1),
    Policy('PetrolTax',4,30,6),
    Policy('PhoneTapping',1,45,2),
    Policy('PoliceForce',55,80,3),
    Policy('PollutionControls',30,85,5),
    Policy('PrisonerTagging',55,55,1),
    Policy('PrivatePrisons',12,12,1),
    Policy('PropertyTax',11,73,5),
    Policy('PublicLibraries',50,60,2),
    Policy('RaceDiscriminationAct',70,80,3),
    Policy('RailSubsidies',31,86,5),
    Policy('Recycling',23,100,3),
    Policy('RoadBuilding',40,40,1),
    Policy('RuralDevelopmentGrants',20,20,1),
    Policy('SalesTax',22,52,6),
    Policy('SchoolBuses',75,75,2),
    Policy('SchoolPrayers',12,12,1),
    Policy('SchoolVouchers',20,20,1),
    Policy('SmallBusinessGrants',60,60,1),
    Policy('SpaceProgram',75,75,1),
    Policy('ScienceFunding',30,75,5),
    Policy('StateHealthService',10,78,6),
    Policy('StateHousing',50,72,4),
    Policy('StatePensions',51,88,5),
    Policy('StateSchools',35,75,6),
    Policy('StemCells',82,82,1),
    Policy('Tasers',20,50,2),
    Policy('TechnologyColleges',30,82,3),
    Policy('TechnologyGrants',74,75,3),
    Policy('TobaccoTax',15,45,5),
    Policy('TollRoads',25,40,3),
    Policy('UnemployedBenefit',12,75,6),
    Policy('UniversityGrants',48,78,4),
]
    
def r(lower,higher):
    return random.randint(lower,higher)

def choose(seq):
    return random.choice(seq)

def chancein(chance):
    return r(1,chance)==1

def getoptions():
    options=''
    for o in OPTIONS:
        if chancein(2):
            options+=o+'\n'
    return options

def getpolicies():
    policies=''
    for p in POLICIES:
        policies+=p.generate()
    return policies
            
i=1
allowbig=chancein(6) #USA has pretty crazy config

RANDOMIA=f'''
[config]
currency="$"
population={r(11131,158334 if allowbig else 40578)}
economic_cycle_start={r(28,96)/100}
min_income={r(8000,8343)}
max_income={r(150000,156431)}
min_gdp={r(498400,2021093 if allowbig else 882500)}
max_gdp={r(1495200,6063280 if allowbig else 2627500)}
wealth_mod={r(1260,23410 if allowbig else 4790)/1000}
starting_debt={r(267979,3120000 if allowbig else 1080000)}
name=randomia
guiname="Randomia #{i}"
names_file="data/names/braziliannames.txt"
term_length={choose([20,20,20,16,16,16,])}
max_terms={choose([-1,-1,2,-1,-1,2])}
details_image="randomia_details.jpg"
description="Randomia is generated based on country parameter ranges from official mission files."
flag="flag_randomia.jpg"
apathy={r(31,41)/100}
jobtitle={choose(["Prime Minister","Prime Minister",])}
GUID={6+i}

[options]
{getoptions()}
[stats]
Population:="?"
Size:="?"
Life expectancy:="?"
Gini(inequality):="?"
GDP per capita:="?"
Poverty:="?"
Ethnicity:="?"
Religion:="?"
Vegemite Consumption:="?"
Obesity Rate:="?"
Big Mac Index:="?"

[policies]
{getpolicies()}
'''

print(RANDOMIA)
