class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        string = "{artist}. \"{title}\". {year}, {medium}. {owner}, {location}.".format(artist=self.artist,
                                                                                        title=self.title,
                                                                                        year=self.year,
                                                                                        medium=self.medium,
                                                                                        owner=self.owner.name,
                                                                                        location=self.owner.location)
        return string


class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, listing):
        self.listings.remove(listing)

    def show_listings(self):
        for item in self.listings:
            print(item)

class Client:
    def __init__(self, name, location="Private Collection", is_museum=False):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def __repr__(self):
        string = """{name}
{location}
""".format(name=self.name, location=self.location)
        return string

    def sell_artwork(self, art, price):
        if self == art.owner:
            new_listing = Listing(art, price, self)
            veneer.add_listing(new_listing)

    def buy_artwork(self, artwork):
        if self != artwork.owner:
            for listing in veneer.listings:
                if listing.art == artwork:
                    art_listing = listing
            artwork.owner = self
            veneer.remove_listing(art_listing)



class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        string = "{}: {}".format(self.art.title, self.price)
        return string


veneer = Marketplace()
edytta = Client("Edytta Halpirt")
moma = Client("The MOMA", "New York", True)
girl_with_mandolin = Art("Pićasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
vetheuil_in_fog = Art("Monet, Claude", "Vétheuil in the Fog", "oil on canvas", 1879, moma)
edytta.sell_artwork(girl_with_mandolin, "$6M")
moma.sell_artwork(vetheuil_in_fog, "$22M")
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()
edytta.buy_artwork(vetheuil_in_fog)
print(vetheuil_in_fog)
veneer.show_listings()