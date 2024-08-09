from holidata.holiday import Region


class BE(Region):
    """
    2020-05-09 -           : https://gesetze.berlin.de/perma?d=jlr-FeiertGBEV7P1
    2019-02-07 - 2020-05-08: https://gesetze.berlin.de/perma?d=jlr-FeiertGBEV6P1
    2018-01-01 - 2019-02-06: https://gesetze.berlin.de/perma?d=jlr-FeiertGBEV5P1
    2015-10-25 - 2017-12-31: https://gesetze.berlin.de/perma?d=jlr-FeiertGBEV4P1
    2010-12-29 - 2015-10-24: https://gesetze.berlin.de/perma?d=jlr-FeiertGBEV2P1
    1995-01-01 - 2010-12-28: https://gesetze.berlin.de/perma?d=jlr-FeiertGBEV2P1
    """
    def __init__(self, country):
        super().__init__("BE", country)

        """
        2020-05-08: 75. Jahrestag der Befreiung vom Nationalsozialismus und der Beendigung des Zweiten Weltkrieges in Europa
        Introduced 2019 for Berlin
        https://gesetze.berlin.de/perma?d=jlr-FeiertGBEV6P1
        """
        self.define_holiday() \
            .with_name("75. Jahrestag der Befreiung vom Nationalsozialismus und der Beendigung des Zweiten Weltkrieges in Europa") \
            .in_years([2020]) \
            .on(month=5, day=8) \
            .with_flags("F")

        """
        03-08: Frauentag
        Introduced 2019 for Berlin
        https://gesetze.berlin.de/perma?d=jlr-FeiertGBEV6P1
        """
        self.define_holiday() \
            .with_name("Internationaler Frauentag") \
            .since(2019) \
            .on(month=3, day=8) \
            .with_flags("F")
