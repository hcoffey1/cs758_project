from Q_Util import extractBackends


def genMachineIDs():
    backends = extractBackends()
    i = 0
    for be in backends:
        print("\""+be.configuration().backend_name+"\"", ':', i, ',')
        i += 1


MachineDict = {
    "fake_almaden": 0,
    "fake_armonk": 1,
    "fake_athens": 2,
    "fake_belem": 3,
    "fake_boeblingen": 4,
    "fake_bogota": 5,
    "fake_brooklyn": 6,
    "fake_burlington": 7,
    "fake_cairo": 8,
    "fake_cambridge": 9,
    "fake_casablanca": 10,
    "fake_essex": 11,
    "fake_guadalupe": 12,
    "fake_hanoi": 13,
    "fake_jakarta": 14,
    "fake_johannesburg": 15,
    "fake_kolkata": 16,
    "fake_lagos": 17,
    "fake_lima": 18,
    "fake_london": 19,
    "fake_manhattan": 20,
    "fake_manila": 21,
    "fake_melbourne": 22,
    "fake_montreal": 23,
    "fake_mumbai": 24,
    "fake_nairobi": 25,
    "fake_ourense": 26,
    "fake_paris": 27,
    "fake_poughkeepsie": 28,
    "fake_quito": 29,
    "fake_rochester": 30,
    "fake_rome": 31,
    "fake_rueschlikon": 32,
    "fake_santiago": 33,
    "fake_singapore": 34,
    "fake_sydney": 35,
    "fake_tenerife": 36,
    "fake_tokyo": 37,
    "fake_toronto": 38,
    "fake_valencia": 39,
    "fake_vigo": 40,
    "fake_washington": 41,
    "fake_yorktown": 42
}