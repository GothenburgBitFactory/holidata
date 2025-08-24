from holidata.holiday import Country

__all__ = [
    "IN",
]


class IN(Country):
    id = "IN"
    languages = ["en"]
    default_lang = "en"

    def __init__(self):
        super().__init__()
        self.regions = []

        self.define_holiday() \
            .with_name("New Year's Day") \
            .on(month=1, day=1) \
            .with_flags("NF")

        self.define_holiday() \
            .with_name("Lohri") \
            .on(month=1, day=14) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Pongal, Makar Sankranti") \
            .on(month=1, day=15) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Guru Gobind Singh Jayanti") \
            .on(month=1, day=16) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Republic Day") \
            .on(month=1, day=26) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Vasant Panchami") \
            .on(month=2, day=12) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Guru Ravidas Jayanti") \
            .on(month=2, day=22) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Maha Shivaratri") \
            .on(month=3, day=7) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Chhoti Holi, Holika Dahan") \
            .on(month=3, day=23) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Holi") \
            .on(month=3, day=24) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Good Friday") \
            .on(month=3, day=25) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Easter") \
            .on(month=3, day=27) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Gudi Padwa, Ugadi") \
            .on(month=4, day=8) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Solar New Year, Baisakhi") \
            .on(month=4, day=13) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Rama Navami") \
            .on(month=4, day=15) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Hazarat Ali's Birthday") \
            .on(month=4, day=21) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Buddha Purnima") \
            .on(month=5, day=21) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Eid al-Fitr , Ramadan") \
            .on(month=7, day=7) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Independence Day") \
            .on(month=8, day=15) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Rakhi, Raksha Bandhan") \
            .on(month=8, day=18) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Krishna Janmashtami") \
            .on(month=8, day=25) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Ganesh Chaturthi") \
            .on(month=9, day=5) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Onam, Eid al-Adha, Bakrid") \
            .on(month=9, day=13) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Gandhi Jayanti") \
            .on(month=10, day=2) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Durga Ashtami") \
            .on(month=10, day=9) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Maha Navami") \
            .on(month=10, day=10) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Dussehra, Madhvacharya Jayanti") \
            .on(month=10, day=11) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Muharram") \
            .on(month=10, day=12) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Valmiki Jayanti") \
            .on(month=10, day=16) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Karwa Chauth") \
            .on(month=10, day=19) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Diwali, Lakshmi Puja") \
            .on(month=10, day=30) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Gowardhan Puja") \
            .on(month=10, day=31) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Bhaiya Dooj") \
            .on(month=11, day=1) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Chhath Puja") \
            .on(month=11, day=6) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Guru Nanak Jayanti, Nehru Jayanti") \
            .on(month=11, day=14) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Milad an-Nabi, Id-e-Milad") \
            .on(month=12, day=12) \
            .with_flags("NV")  # has to be changed to a variable date

        self.define_holiday() \
            .with_name("Christmas") \
            .on(month=12, day=25) \
            .with_flags("NF")
