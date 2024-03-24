import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://realtimefacedetection-dc463-default-rtdb.firebaseio.com/"
})


# CREATING THE REQUIRED DATABASE REFERENCES
reference = db.reference("MCAB")

# ADDING DATA TO THE DATABASE FOR THE STUDENTS
data = {

    "2347201": {

    },

    "2347202": {

    },

    "2347203": {

    },

    "2347204": {

    },

    "2347205": {

    },

    "2347206": {

    },

    "2347207": {

    },

    "2347208": {

    },

    "2347209": {

    },

    "2347210": {

    },

    "2347211": {

    },

    "2347212": {

    },

    "2347213": {

    },

    "2347214": {

    },

    "2347215": {

    },

    "2347216": {

    },

    "2347217": {

    },

    "2347218": {

    },

    "2347219": {

    },

    "2347220": {

    },

    "2347221": {

    },

    "2347222": {

    },

    "2347223": {

    },

    "2347224": {
        "name": "HrishabhGautam",
        "major": "MCAB",
        "starting_year": 2022,
        "total_attendance": 93,
        "standing": "A",
        "year": 1,
        "last_attendance_time": "2024-03-11 11:33:11"
    },

    "2347225": {

    },

    "2347226": {

    },

    "2347227": {

    },

    "2347228": {

    },

    "2347229": {

    },

    "2347230": {

    },

    "2347231": {

    },

    "2347232": {

    },

    "2347233": {

    },

    "2347234": {

    },

    "2347235": {

    },

    "2347236": {

    },

    "2347237": {

    },

    "234723": {

    },


    "2347238": {
        "name": "ManoswitaBose",
        "major": "MCAB",
        "starting_year": 2022,
        "total_attendance": 87,
        "standing": "A",
        "year": 1,
        "last_attendance_time": "2024-03-11 00:11:60"
    },

    "2347239": {

    },

    "2347240": {

    },

    "2347241": {

    },

    "2347242": {

    },

    "2347243": {

    },

    "2347244": {

    },

    "2347245": {

    },

    "2347246": {

    },

    "2347247": {

    },

    "2347248": {

    },

    "2347249": {

    },

    "2347250": {

    },

    "2347251": {

    },

    "2347252": {

    },

    "2347253": {

    },

    "2347254": {

    },

    "2347255": {

    },

    "2347256": {

    },

    "2347257": {

    },

    "2347258": {

    },

    "2347259": {

    },

    "2347260": {

    },

    "2347261": {
        "name": "SuvajitKarmakar",
        "major": "MCAB",
        "starting_year": 2022,
        "total_attendance": 56,
        "standing": "A",
        "year": 1,
        "last_attendance_time": "2024-03-11 00:54:34"
    },

    "2347262": {

    },

    "2347263": {

    },

    "2347264": {

    },

    "2347265": {

    }

}