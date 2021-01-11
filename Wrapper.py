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
        url = self.urls["overview"]
        r = self.s.get(url)
        data = json.loads(r.content)
        return data

    def get_last_overview(self):
        # TODO: add docu
        data = self.get_overview()
        last = data["index"][-1]
        return last

    def get_distrib_districts(self):
        # TODO: Add docu
        url = self.urls["distribution_districts"]
        r = self.s.get(url)
        data = json.loads(r.content)
        return data

    def get_last_distrib_districts(self):
        # TODO: add docu
        data = self.get_distrib_districts()
        last = data["index"][-1]
        return last

    def get_distrib_ages_districts(self):
        # TODO: add docu
        url = self.urls["overview__distr_ages"]
        r = self.s.get(url)
        data = json.loads(r.content)
        return data

    def get_last_distrib_ages_districts(self):
        # TODO: add docu
        data = self.get_distrib_ages_districts()
        last = data["index"][-1]
        res = [last]
        last_week = last["meldewoche"]
        last_year = last["jahr"]
        for i in data["index"]:
            if i["meldewoche"]==last_week and i["jahr"]==last_year:
                res.append(i)
        return res


def main():
    test = Wrapper()
    x = test.get_last_distrib_ages_districts()
    json.dump(x, open("out.json", "w"))

if __name__ == '__main__':
    main()
