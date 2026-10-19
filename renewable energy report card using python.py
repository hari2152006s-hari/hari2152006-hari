class RenewableEnergyReportCard:                                                                    #class
    renewableEnergyReport = ["Wind Turbine","Solar Panels","Hydroelectric Plants",]
    def display1(self):
        print(f"wellcome to our power plants{self.renewableEnergyReport}")


class windTurbine(RenewableEnergyReportCard):
    def __init__(self):
        self.windturbine_report ={"energy produced":"10kw",
                                  "Wind speed m/s": "25",
                                  "energy loss":"5%",}
        self.velue1=self.windturbine_report["energy produced"]
    def display2(self):
        print("wind report card")
        print(self.windturbine_report)
        return self.velue1
class solarPanel(RenewableEnergyReportCard):
    def __init__(self):
        self.solarPanel_report ={"energy produced":"15kw",
                                 "Sunlight intensity":"7%",
                                  "heat loss":"8%",}
        self.velue=self.solarPanel_report["energy produced"]

    def display3(self):
        print("solar panel report card")
        print(self.solarPanel_report)
        return self.velue
class Hydroelectricenergy(RenewableEnergyReportCard):
    def __init__(self):
        self.hydroelectric_report ={"energy produced":"30kw",
                                    "Water flow rate m³/s":"40",
                                    "water head":"99"}
        self.hydroelectric_report_report ={"energy produced":"15kw",}
    def display4(self):
        print("hydroelectric report card")
        print(self.hydroelectric_report)
        return self.hydroelectric_report_report





# objects
reportCard = RenewableEnergyReportCard()
reportCard.display1()

windTurbinereport = windTurbine()
windTurbinereport.display2()

solarPanelreport = solarPanel()
solarPanelreport.display3()

hydroelectricenergy = Hydroelectricenergy()
hydroelectricenergy.display4()


