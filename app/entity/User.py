class User():
    
    def __init__(self, id, k_nev, cs_nev, szul_d, nem, felh_n, jelszo, prof_pic_loc):
        self._id = id
        self._k_nev = k_nev
        self._cs_nev = cs_nev
        self._szul_d = szul_d
        self._nem = nem
        self._felh_n = felh_n
        self._jelszo = jelszo
        self._prof_pic_loc = prof_pic_loc

    def to_dict(self):
        return {
            "id" : self._id,
            "k_nev" : self._k_nev,
            "cs_nev" : self._cs_nev,
            "szuld_d" : self._szul_d,
            "nem" : self._nem,
            "felh_n" : self._felh_n,
            "jelszo" : self._jelszo,
            "prof_pic_loc" : self._prof_pic_loc
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, n):
        self._id = n

    @property
    def k_nev(self):
        return self._k_nev
    
    @k_nev.setter
    def k_nev(self, n):
        self._k_nev = n
    
    @property
    def cs_nev(self):
        return self._cs_nev

    @cs_nev.setter
    def cs_nev(self, n):
        self._cs_nev = n
    
    @property
    def szul_d(self):
        return self._szul_d

    @szul_d.setter
    def szul_d(self, n):
        self._szul_d = n
    
    @property
    def nem(self):
        return self._nem
    
    @nem.setter
    def nem(self, n):
        self._nem = n

    @property
    def felh_n(self):
        return self._felh_n
    
    @felh_n.setter
    def felh_n(self, n):
        self._felh_n = n
    
    @property
    def jelszo(self):
        return self._jelszo

    @jelszo.setter
    def jelszo(self, n):
        self._jelszo = n

    @property
    def prof_pic_loc(self):
        return self._prof_pic_loc

    @prof_pic_loc.setter
    def prof_pic_loc(self, n):
        self._prof_pic_loc = n

    