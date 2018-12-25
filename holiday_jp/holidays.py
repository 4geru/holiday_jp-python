# -*- coding: utf-8 -*-


class HolidayDataset(object):
    """Dataset as dict."""

    # holidays jp dataset
    HOLIDAYS = {
    "1970-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1970-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1970-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1970-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1970-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1970-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1970-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1970-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1970-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1970-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1970-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1970-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1971-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1971-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1971-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1971-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1971-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "木",
        "week_en": "Thursday"
    },
    "1971-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1971-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1971-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1971-09-24": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1971-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1971-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1971-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1972-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1972-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1972-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1972-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1972-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "土",
        "week_en": "Saturday"
    },
    "1972-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1972-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1972-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1972-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1972-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1972-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1972-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1973-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1973-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1973-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1973-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1973-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "1973-04-30": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1973-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1973-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1973-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1973-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1973-09-24": {
        "name": "秋分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1973-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1973-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1973-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1974-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1974-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1974-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1974-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1974-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "月",
        "week_en": "Monday"
    },
    "1974-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1974-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1974-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1974-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1974-09-16": {
        "name": "敬老の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1974-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1974-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1974-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1974-11-04": {
        "name": "文化の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1974-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1975-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1975-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1975-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1975-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1975-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1975-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1975-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1975-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1975-09-24": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1975-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1975-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1975-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1975-11-24": {
        "name": "勤労感謝の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1976-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1976-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1976-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1976-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1976-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "木",
        "week_en": "Thursday"
    },
    "1976-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1976-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1976-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1976-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1976-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1976-10-11": {
        "name": "体育の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1976-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1976-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1977-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1977-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1977-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1977-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1977-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "金",
        "week_en": "Friday"
    },
    "1977-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1977-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1977-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1977-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1977-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1977-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1977-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1978-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1978-01-02": {
        "name": "元日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1978-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1978-01-16": {
        "name": "成人の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1978-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1978-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1978-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "土",
        "week_en": "Saturday"
    },
    "1978-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1978-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1978-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1978-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1978-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1978-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1978-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1979-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1979-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1979-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1979-02-12": {
        "name": "建国記念の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1979-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1979-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "1979-04-30": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1979-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1979-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1979-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1979-09-24": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1979-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1979-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1979-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1980-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1980-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1980-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1980-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1980-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1980-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1980-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1980-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1980-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1980-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1980-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1980-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1980-11-24": {
        "name": "勤労感謝の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1981-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1981-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1981-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1981-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1981-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1981-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1981-05-04": {
        "name": "憲法記念日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1981-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1981-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1981-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1981-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1981-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1981-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1982-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1982-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1982-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1982-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1982-03-22": {
        "name": "春分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1982-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "木",
        "week_en": "Thursday"
    },
    "1982-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1982-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1982-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1982-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1982-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1982-10-11": {
        "name": "体育の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1982-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1982-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1983-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1983-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1983-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1983-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1983-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "金",
        "week_en": "Friday"
    },
    "1983-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1983-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1983-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1983-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1983-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1983-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1983-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1984-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1984-01-02": {
        "name": "元日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1984-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1984-01-16": {
        "name": "成人の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1984-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1984-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1984-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "1984-04-30": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1984-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1984-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1984-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1984-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1984-09-24": {
        "name": "秋分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1984-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1984-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1984-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1985-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1985-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1985-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1985-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1985-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "月",
        "week_en": "Monday"
    },
    "1985-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1985-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1985-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1985-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1985-09-16": {
        "name": "敬老の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1985-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1985-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1985-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1985-11-04": {
        "name": "文化の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1985-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1986-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1986-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1986-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1986-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1986-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1986-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1986-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1986-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1986-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1986-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1986-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1986-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1986-11-24": {
        "name": "勤労感謝の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1987-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1987-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1987-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1987-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1987-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1987-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1987-05-04": {
        "name": "憲法記念日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1987-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1987-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1987-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1987-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1987-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1987-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1988-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1988-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1988-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1988-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1988-03-21": {
        "name": "春分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1988-04-29": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "金",
        "week_en": "Friday"
    },
    "1988-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1988-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1988-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1988-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1988-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1988-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1988-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1988-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1989-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1989-01-02": {
        "name": "元日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1989-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1989-01-16": {
        "name": "成人の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1989-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1989-02-24": {
        "name": "昭和天皇の大喪の礼",
        "name_en": "The Funeral Ceremony of Emperor Showa.",
        "week": "金",
        "week_en": "Friday"
    },
    "1989-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1989-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1989-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1989-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "木",
        "week_en": "Thursday"
    },
    "1989-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1989-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1989-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1989-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1989-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1989-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1989-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "土",
        "week_en": "Saturday"
    },
    "1990-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1990-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1990-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1990-02-12": {
        "name": "建国記念の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1990-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1990-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1990-04-30": {
        "name": "みどりの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1990-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1990-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "金",
        "week_en": "Friday"
    },
    "1990-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1990-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1990-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1990-09-24": {
        "name": "秋分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1990-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1990-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1990-11-12": {
        "name": "即位礼正殿の儀",
        "name_en": "The Ceremony of the Enthronement of His Majesty the Emperor (at the Seiden)",
        "week": "月",
        "week_en": "Monday"
    },
    "1990-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1990-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "1990-12-24": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1991-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1991-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1991-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1991-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1991-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1991-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1991-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "土",
        "week_en": "Saturday"
    },
    "1991-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1991-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1991-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1991-09-16": {
        "name": "敬老の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1991-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1991-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1991-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1991-11-04": {
        "name": "文化の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1991-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1991-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "月",
        "week_en": "Monday"
    },
    "1992-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1992-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1992-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1992-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1992-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1992-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1992-05-04": {
        "name": "憲法記念日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1992-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1992-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1992-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1992-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1992-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1992-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1992-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1993-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1993-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1993-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1993-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1993-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1993-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1993-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1993-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1993-06-09": {
        "name": "皇太子徳仁親王の結婚の儀",
        "name_en": "The Rite of Wedding of HIH Crown Prince Naruhito",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1993-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1993-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1993-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1993-10-11": {
        "name": "体育の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1993-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1993-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1993-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "木",
        "week_en": "Thursday"
    },
    "1994-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1994-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1994-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1994-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1994-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1994-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1994-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1994-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1994-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1994-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1994-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1994-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1994-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1994-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "金",
        "week_en": "Friday"
    },
    "1995-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1995-01-02": {
        "name": "元日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1995-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1995-01-16": {
        "name": "成人の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1995-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1995-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1995-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1995-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1995-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "木",
        "week_en": "Thursday"
    },
    "1995-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1995-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1995-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1995-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1995-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1995-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1995-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "土",
        "week_en": "Saturday"
    },
    "1996-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1996-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1996-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1996-02-12": {
        "name": "建国記念の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1996-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1996-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1996-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1996-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "土",
        "week_en": "Saturday"
    },
    "1996-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1996-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1996-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1996-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1996-09-16": {
        "name": "敬老の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1996-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1996-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1996-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1996-11-04": {
        "name": "文化の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1996-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1996-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "月",
        "week_en": "Monday"
    },
    "1997-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1997-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1997-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1997-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1997-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1997-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1997-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1997-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1997-07-21": {
        "name": "海の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1997-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1997-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1997-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1997-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1997-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1997-11-24": {
        "name": "勤労感謝の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1997-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1998-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1998-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1998-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1998-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1998-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1998-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1998-05-04": {
        "name": "憲法記念日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1998-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1998-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1998-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1998-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1998-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "1998-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1998-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1998-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1999-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1999-01-15": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "金",
        "week_en": "Friday"
    },
    "1999-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1999-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1999-03-22": {
        "name": "春分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1999-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1999-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "月",
        "week_en": "Monday"
    },
    "1999-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1999-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1999-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1999-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1999-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "1999-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "1999-10-11": {
        "name": "体育の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "1999-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "1999-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "1999-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "木",
        "week_en": "Thursday"
    },
    "2000-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2000-01-10": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2000-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2000-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2000-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2000-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2000-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "木",
        "week_en": "Thursday"
    },
    "2000-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2000-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2000-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2000-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2000-10-09": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2000-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2000-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2000-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "土",
        "week_en": "Saturday"
    },
    "2001-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2001-01-08": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2001-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2001-02-12": {
        "name": "建国記念の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2001-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2001-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2001-04-30": {
        "name": "みどりの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2001-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2001-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "金",
        "week_en": "Friday"
    },
    "2001-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2001-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2001-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2001-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2001-09-24": {
        "name": "秋分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2001-10-08": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2001-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2001-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2001-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "2001-12-24": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2002-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2002-01-14": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2002-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2002-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2002-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2002-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2002-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "土",
        "week_en": "Saturday"
    },
    "2002-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2002-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2002-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2002-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2002-09-16": {
        "name": "敬老の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2002-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2002-10-14": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2002-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2002-11-04": {
        "name": "文化の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2002-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2002-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "月",
        "week_en": "Monday"
    },
    "2003-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2003-01-13": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2003-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2003-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2003-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2003-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2003-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2003-07-21": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2003-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2003-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2003-10-13": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2003-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2003-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2003-11-24": {
        "name": "勤労感謝の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2003-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2004-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2004-01-12": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2004-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2004-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2004-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2004-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2004-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2004-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2004-07-19": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2004-09-20": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2004-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2004-10-11": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2004-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2004-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2004-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "木",
        "week_en": "Thursday"
    },
    "2005-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2005-01-10": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2005-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2005-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2005-03-21": {
        "name": "春分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2005-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2005-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2005-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2005-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2005-07-18": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2005-09-19": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2005-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2005-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2005-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2005-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2005-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "金",
        "week_en": "Friday"
    },
    "2006-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2006-01-02": {
        "name": "元日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2006-01-09": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2006-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2006-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2006-04-29": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2006-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2006-05-04": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "木",
        "week_en": "Thursday"
    },
    "2006-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2006-07-17": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2006-09-18": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2006-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2006-10-09": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2006-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2006-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2006-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "土",
        "week_en": "Saturday"
    },
    "2007-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2007-01-08": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2007-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2007-02-12": {
        "name": "建国記念の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2007-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2007-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2007-04-30": {
        "name": "昭和の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2007-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2007-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2007-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2007-07-16": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2007-09-17": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2007-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2007-09-24": {
        "name": "秋分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2007-10-08": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2007-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2007-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2007-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "2007-12-24": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2008-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2008-01-14": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2008-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2008-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2008-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2008-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2008-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2008-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2008-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2008-07-21": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2008-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2008-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2008-10-13": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2008-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2008-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2008-11-24": {
        "name": "勤労感謝の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2008-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2009-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2009-01-12": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2009-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2009-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2009-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2009-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2009-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2009-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2009-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2009-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2009-09-21": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2009-09-22": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2009-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2009-10-12": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2009-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2009-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2009-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2010-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2010-01-11": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2010-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2010-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2010-03-22": {
        "name": "春分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2010-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2010-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2010-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2010-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2010-07-19": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2010-09-20": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2010-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2010-10-11": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2010-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2010-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2010-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "木",
        "week_en": "Thursday"
    },
    "2011-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2011-01-10": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2011-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2011-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2011-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2011-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2011-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2011-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2011-07-18": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2011-09-19": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2011-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2011-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2011-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2011-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2011-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "金",
        "week_en": "Friday"
    },
    "2012-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2012-01-02": {
        "name": "元日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2012-01-09": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2012-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2012-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2012-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2012-04-30": {
        "name": "昭和の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2012-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2012-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2012-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2012-07-16": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2012-09-17": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2012-09-22": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2012-10-08": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2012-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2012-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2012-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "2012-12-24": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2013-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2013-01-14": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2013-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2013-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2013-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2013-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2013-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2013-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2013-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2013-07-15": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2013-09-16": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2013-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2013-10-14": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2013-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2013-11-04": {
        "name": "文化の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2013-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2013-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "月",
        "week_en": "Monday"
    },
    "2014-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2014-01-13": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2014-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2014-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2014-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2014-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2014-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2014-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2014-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2014-07-21": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2014-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2014-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2014-10-13": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2014-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2014-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2014-11-24": {
        "name": "勤労感謝の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2014-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2015-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2015-01-12": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2015-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2015-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2015-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2015-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2015-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2015-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2015-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2015-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2015-09-21": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2015-09-22": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2015-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2015-10-12": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2015-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2015-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2015-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2016-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2016-01-11": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2016-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2016-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2016-03-21": {
        "name": "春分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2016-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2016-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2016-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2016-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2016-07-18": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2016-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2016-09-19": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2016-09-22": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2016-10-10": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2016-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2016-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2016-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "金",
        "week_en": "Friday"
    },
    "2017-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2017-01-02": {
        "name": "元日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2017-01-09": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2017-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2017-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2017-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2017-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2017-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2017-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2017-07-17": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2017-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2017-09-18": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2017-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2017-10-09": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2017-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2017-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2017-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "土",
        "week_en": "Saturday"
    },
    "2018-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2018-01-08": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2018-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2018-02-12": {
        "name": "建国記念の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2018-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2018-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2018-04-30": {
        "name": "昭和の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2018-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2018-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2018-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2018-07-16": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2018-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2018-09-17": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2018-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2018-09-24": {
        "name": "秋分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2018-10-08": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2018-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2018-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2018-12-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "2018-12-24": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2019-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2019-01-14": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2019-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2019-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2019-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2019-04-30": {
        "name": "休日",
        "name_en": "Holiday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2019-05-01": {
        "name": "休日（祝日扱い）",
        "name_en": "Holiday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2019-05-02": {
        "name": "休日",
        "name_en": "Holiday",
        "week": "木",
        "week_en": "Thursday"
    },
    "2019-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2019-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2019-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2019-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2019-07-15": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2019-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2019-08-12": {
        "name": "山の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2019-09-16": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2019-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2019-10-14": {
        "name": "体育の日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2019-10-22": {
        "name": "休日（祝日扱い）",
        "name_en": "Holiday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2019-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2019-11-04": {
        "name": "文化の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2019-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2020-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2020-01-13": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2020-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2020-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "2020-02-24": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2020-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2020-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2020-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2020-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2020-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2020-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2020-07-23": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2020-07-24": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2020-08-10": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2020-09-21": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2020-09-22": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2020-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2020-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2021-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2021-01-11": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2021-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2021-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2021-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2021-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2021-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2021-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2021-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2021-07-19": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2021-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2021-09-20": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2021-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2021-10-11": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2021-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2021-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2022-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2022-01-10": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2022-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2022-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2022-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2022-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2022-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2022-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2022-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2022-07-18": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2022-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2022-09-19": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2022-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2022-10-10": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2022-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2022-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2023-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2023-01-02": {
        "name": "元日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2023-01-09": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2023-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2023-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "木",
        "week_en": "Thursday"
    },
    "2023-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2023-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2023-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2023-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2023-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2023-07-17": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2023-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2023-09-18": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2023-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2023-10-09": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2023-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2023-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2024-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2024-01-08": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2024-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2024-02-12": {
        "name": "建国記念の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2024-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "金",
        "week_en": "Friday"
    },
    "2024-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2024-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2024-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2024-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2024-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2024-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2024-07-15": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2024-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2024-08-12": {
        "name": "山の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2024-09-16": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2024-09-22": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2024-09-23": {
        "name": "秋分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2024-10-14": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2024-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2024-11-04": {
        "name": "文化の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2024-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2025-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2025-01-13": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2025-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2025-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "2025-02-24": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2025-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2025-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2025-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2025-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2025-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2025-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2025-07-21": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2025-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2025-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2025-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2025-10-13": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2025-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2025-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2025-11-24": {
        "name": "勤労感謝の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2026-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2026-01-12": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2026-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2026-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "月",
        "week_en": "Monday"
    },
    "2026-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2026-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2026-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2026-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2026-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2026-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2026-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2026-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2026-09-21": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2026-09-22": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2026-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2026-10-12": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2026-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2026-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2027-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2027-01-11": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2027-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2027-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2027-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2027-03-22": {
        "name": "春分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2027-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2027-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2027-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2027-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2027-07-19": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2027-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2027-09-20": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2027-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2027-10-11": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2027-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2027-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2028-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2028-01-10": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2028-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2028-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2028-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2028-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2028-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2028-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2028-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2028-07-17": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2028-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2028-09-18": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2028-09-22": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2028-10-09": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2028-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2028-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2029-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2029-01-08": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2029-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2029-02-12": {
        "name": "建国記念の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2029-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "金",
        "week_en": "Friday"
    },
    "2029-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2029-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2029-04-30": {
        "name": "昭和の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2029-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2029-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2029-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2029-07-16": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2029-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2029-09-17": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2029-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2029-09-24": {
        "name": "秋分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2029-10-08": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2029-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2029-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2030-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2030-01-14": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2030-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2030-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "土",
        "week_en": "Saturday"
    },
    "2030-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2030-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2030-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2030-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2030-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2030-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2030-07-15": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2030-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2030-08-12": {
        "name": "山の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2030-09-16": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2030-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2030-10-14": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2030-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2030-11-04": {
        "name": "文化の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2030-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2031-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2031-01-13": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2031-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2031-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "2031-02-24": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2031-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2031-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2031-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2031-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2031-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2031-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2031-07-21": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2031-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2031-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2031-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2031-10-13": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2031-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2031-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2031-11-24": {
        "name": "勤労感謝の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2032-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2032-01-12": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2032-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2032-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "月",
        "week_en": "Monday"
    },
    "2032-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2032-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2032-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2032-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2032-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2032-07-19": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2032-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2032-09-20": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2032-09-21": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2032-09-22": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2032-10-11": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2032-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2032-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2033-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2033-01-10": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2033-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2033-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2033-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2033-03-21": {
        "name": "春分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2033-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2033-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2033-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2033-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2033-07-18": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2033-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2033-09-19": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2033-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2033-10-10": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2033-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2033-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2034-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2034-01-02": {
        "name": "元日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2034-01-09": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2034-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2034-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "木",
        "week_en": "Thursday"
    },
    "2034-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2034-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2034-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2034-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2034-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2034-07-17": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2034-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2034-09-18": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2034-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2034-10-09": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2034-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2034-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2035-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2035-01-08": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2035-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2035-02-12": {
        "name": "建国記念の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2035-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "金",
        "week_en": "Friday"
    },
    "2035-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2035-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2035-04-30": {
        "name": "昭和の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2035-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2035-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2035-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2035-07-16": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2035-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2035-09-17": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2035-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2035-09-24": {
        "name": "秋分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2035-10-08": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2035-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2035-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2036-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2036-01-14": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2036-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2036-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "土",
        "week_en": "Saturday"
    },
    "2036-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2036-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2036-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2036-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2036-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2036-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2036-07-21": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2036-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2036-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2036-09-22": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2036-10-13": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2036-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2036-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2036-11-24": {
        "name": "勤労感謝の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2037-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2037-01-12": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2037-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2037-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "月",
        "week_en": "Monday"
    },
    "2037-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2037-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2037-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2037-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2037-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2037-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2037-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2037-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2037-09-21": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2037-09-22": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2037-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2037-10-12": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2037-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2037-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2038-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2038-01-11": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2038-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2038-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2038-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2038-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2038-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2038-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2038-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2038-07-19": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2038-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2038-09-20": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2038-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2038-10-11": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2038-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2038-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2039-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2039-01-10": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2039-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2039-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2039-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2039-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2039-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2039-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2039-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2039-07-18": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2039-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2039-09-19": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2039-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2039-10-10": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2039-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2039-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2040-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2040-01-02": {
        "name": "元日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2040-01-09": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2040-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2040-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "木",
        "week_en": "Thursday"
    },
    "2040-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2040-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2040-04-30": {
        "name": "昭和の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2040-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2040-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2040-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2040-07-16": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2040-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2040-09-17": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2040-09-22": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2040-10-08": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2040-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2040-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2041-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2041-01-14": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2041-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2041-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "土",
        "week_en": "Saturday"
    },
    "2041-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2041-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2041-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2041-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2041-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2041-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2041-07-15": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2041-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2041-08-12": {
        "name": "山の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2041-09-16": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2041-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2041-10-14": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2041-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2041-11-04": {
        "name": "文化の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2041-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2042-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2042-01-13": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2042-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2042-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "2042-02-24": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2042-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2042-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2042-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2042-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2042-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2042-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2042-07-21": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2042-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2042-09-15": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2042-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2042-10-13": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2042-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2042-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2042-11-24": {
        "name": "勤労感謝の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2043-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2043-01-12": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2043-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2043-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "月",
        "week_en": "Monday"
    },
    "2043-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2043-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2043-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2043-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2043-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2043-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2043-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2043-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2043-09-21": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2043-09-22": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2043-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2043-10-12": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2043-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2043-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2044-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2044-01-11": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2044-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2044-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2044-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2044-03-21": {
        "name": "春分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2044-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2044-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2044-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2044-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2044-07-18": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2044-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2044-09-19": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2044-09-22": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2044-10-10": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2044-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2044-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2045-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2045-01-02": {
        "name": "元日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2045-01-09": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2045-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2045-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "木",
        "week_en": "Thursday"
    },
    "2045-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2045-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2045-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2045-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2045-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2045-07-17": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2045-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2045-09-18": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2045-09-22": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2045-10-09": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2045-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2045-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2046-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2046-01-08": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2046-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2046-02-12": {
        "name": "建国記念の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2046-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "金",
        "week_en": "Friday"
    },
    "2046-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2046-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2046-04-30": {
        "name": "昭和の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2046-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2046-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2046-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2046-07-16": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2046-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2046-09-17": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2046-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2046-09-24": {
        "name": "秋分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2046-10-08": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2046-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2046-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2047-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2047-01-14": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2047-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2047-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "土",
        "week_en": "Saturday"
    },
    "2047-03-21": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2047-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2047-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2047-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2047-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2047-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2047-07-15": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2047-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2047-08-12": {
        "name": "山の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2047-09-16": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2047-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2047-10-14": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2047-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2047-11-04": {
        "name": "文化の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2047-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2048-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2048-01-13": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2048-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2048-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "日",
        "week_en": "Sunday"
    },
    "2048-02-24": {
        "name": "天皇誕生日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2048-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2048-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2048-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2048-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2048-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2048-05-06": {
        "name": "こどもの日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2048-07-20": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2048-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2048-09-21": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2048-09-22": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2048-10-12": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2048-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2048-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2049-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2049-01-11": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2049-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2049-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2049-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2049-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2049-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2049-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2049-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2049-07-19": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2049-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2049-09-20": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2049-09-21": {
        "name": "国民の休日",
        "name_en": "Citizen's Holiday",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2049-09-22": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2049-10-11": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2049-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2049-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2050-01-01": {
        "name": "元日",
        "name_en": "New Year's Day",
        "week": "土",
        "week_en": "Saturday"
    },
    "2050-01-10": {
        "name": "成人の日",
        "name_en": "Coming of Age Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2050-02-11": {
        "name": "建国記念の日",
        "name_en": "National Foundation Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2050-02-23": {
        "name": "天皇誕生日",
        "name_en": "Emperor's Birthday",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2050-03-20": {
        "name": "春分の日",
        "name_en": "Vernal Equinox Day",
        "week": "日",
        "week_en": "Sunday"
    },
    "2050-03-21": {
        "name": "春分の日 振替休日",
        "name_en": "Holiday in lieu",
        "week": "月",
        "week_en": "Monday"
    },
    "2050-04-29": {
        "name": "昭和の日",
        "name_en": "Showa Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2050-05-03": {
        "name": "憲法記念日",
        "name_en": "Constitution Memorial Day",
        "week": "火",
        "week_en": "Tuesday"
    },
    "2050-05-04": {
        "name": "みどりの日",
        "name_en": "Greenery Day",
        "week": "水",
        "week_en": "Wednesday"
    },
    "2050-05-05": {
        "name": "こどもの日",
        "name_en": "Children's Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2050-07-18": {
        "name": "海の日",
        "name_en": "Marine Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2050-08-11": {
        "name": "山の日",
        "name_en": "Mountain Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2050-09-19": {
        "name": "敬老の日",
        "name_en": "Respect for the Aged Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2050-09-23": {
        "name": "秋分の日",
        "name_en": "Autumnal Equinox Day",
        "week": "金",
        "week_en": "Friday"
    },
    "2050-10-10": {
        "name": "スポーツの日",
        "name_en": "Health and Sports Day",
        "week": "月",
        "week_en": "Monday"
    },
    "2050-11-03": {
        "name": "文化の日",
        "name_en": "National Culture Day",
        "week": "木",
        "week_en": "Thursday"
    },
    "2050-11-23": {
        "name": "勤労感謝の日",
        "name_en": "Labor Thanksgiving Day",
        "week": "水",
        "week_en": "Wednesday"
    }
}