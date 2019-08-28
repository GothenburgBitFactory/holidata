from plugin import Country


class Croatia(Country):
    u"""
    01-01: [NF] Nova Godina
    01-06: [NRF] Bogojavljanje / Sveta tri kralja
    05-01: [NF] Praznik rada
    06-22: [NF] Dan antifašističke borbe
    06-25: [NF] Dan državnosti
    08-05: [NF] Dan domovinske zahvalnosti
    08-15: [NRF] Velika Gospa
    10-08: [NF] Dan neovisnosti
    11-01: [NRF] Dan svih svetih
    12-25: [NRF] Božić
    12-26: [NRF] Sveti Stjepan
    1 day after Easter:   [NRV] Uskršnji ponedjeljak
    60 days after Easter: [NRV] Tijelovo
    """

    locale = "hr-HR"


class Slovakia(Country):
    u"""
    01-01: [NF] Deň vzniku Slovenskej republiky
    01-06: [NRF] Zjavenie Pána / Traja králi
    05-01: [NF] Sviatok práce
    05-08: [NF] Deň víťazstva nad fašizmom
    07-05: [NRF] Sviatok svätého Cyrila a Metoda
    08-29: [NF] Výročie SNP
    09-01: [NF] Deň Ústavy Slovenskej republiky
    09-15: [NRF] Sedembolestná Panna Mária
    11-01: [NRF] Sviatok všetkých svätých
    11-17: [NF] Deň boja za slobodu a demokraciu
    12-24: [NRF] Štedrý deň
    12-25: [NRF] Prvý sviatok vianočný
    12-26: [NRF] Druhý sviatok vianočný
    1 day after Easter:   [NRV] Veľkonočný pondelok
    2 days before Easter: [NRV] Veľký piatok
    """

    locale = "sk-SK"


class USA(Country):
    u"""
    01-01: [NF] New Year's Day
    07-04: [NF] Independence Day
    11-11: [NF] Veterans Day
    12-25: [NRF] Christmas Day
    3. monday in January:    [V] Birthday of Martin Luther King, Jr.
    3. monday in February:   [NV] Washington's Birthday
    3. monday in April:      [NV] Patriot's day
    1. last monday in May:   [NV] Memorial day
    1. monday in September:  [NV] Labor Day
    2. monday in October:    [NV] Columbus Day
    4. thursday in November: [NV] Thanksgiving Day
    """

    locale = "en-US"
