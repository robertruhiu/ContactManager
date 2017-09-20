class School :
    def __init__ ( self , eits, fellows ) :
        self.eits = eits
        self.fellows = fellows
        eits =open("let.txt","r")
        eits = eits.readlines()
        print(eits.read())


class Eit:
    def __init__ ( self , names , nationalities , fact ) :
        self.names = names
        self.nationalities = nationalities
        self.fact = fact

    def recite_fun_facts ( self , fact ) :
        return self.fact


class Fellow:
    def __init__ ( self , name , nationality , happiness_level ) :
        self.name = name
        self.nationality = nationality
        self.happiness_level = happiness_level

    def eat ( self , happiness_level ) :
        return self.happiness_level

    def teach ( self , happiness_level ) :
        return self.happiness_level
