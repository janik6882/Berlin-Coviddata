import requests
import json
class Wrapper():
    def __init__(self):
        self.base = "https://www.berlin.de/lageso/gesundheit/infektionsepidemiologie-infektionsschutz/corona/"
        self.urls = {
                    "overview": self.base + "tabelle-indikatoren-gesamtuebersicht/index.php/index/all.json",
                    "distribution_districts": self.base + "tabelle-bezirke-gesamtuebersicht/index.php/index/all.json",
                    "overview__distr_ages": self.base + "tabelle-altersgruppen-gesamtuebersicht/index.php/index/all.json",
                    "distr_ages_curr": self.base + "tabelle-altersgruppen/index.php/index/all.json",
                    "distr_districs_curr": self.base + "tabelle-bezirke/index.php/index/all.json"
                    }
        self.s = requests.Session()
    def get_overview(self):
        # TODO: Add docu
        r = self.s.get(self.urls["overview"])
        data = json.loads(r.content)
        return data

    def get_last_overview(self):
        # TODO: add docu
        data = self.get_overview()
        last = data["index"][-1]
        return last

    def get_distr_districts(self):
        # TODO: Add docu



def main():
    test = Wrapper()
    x = test.get_today_overview()
    json.dump(x, open("out.json", "w"))

if __name__ == '__main__':
    main()
