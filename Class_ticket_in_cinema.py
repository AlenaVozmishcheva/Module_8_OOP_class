class TicketInCinema:

    def __init__(self, title_of_the_film, session_time, qr_code, place):
        self.title_of_the_film = title_of_the_film
        self.session_time = session_time
        self.qr_code = qr_code
        self.place = place

    def get_buy(self):
       return f"Вы купили билет на фильм '{self.title_of_the_film}', время сеанса : {self.session_time}, ваше место: {self.place}. Qr-code билета: {self.qr_code}"

    def get_exchange(self, new_title_of_the_film, new_session_time, new_qr_code, new_place):
        self.title_of_the_film = new_title_of_the_film
        self.session_time = new_session_time
        self.qr_code = new_qr_code
        self.place = new_place
        return f"Вы успешно обменяли билет!"

    def print_info_ticket(self):
        show_info_ticket = str(self.title_of_the_film) + ", " + self.session_time + ", " + self.qr_code + ", " + self.place
        return str(self.title_of_the_film) + ", " +  self.session_time + ", " + self.qr_code + ", " + self.place


ticket_1 = TicketInCinema('Любовь и голуби', '14:00', 'DBY456','Ряд 2 место 12' )
print(ticket_1.get_buy())
print(ticket_1.get_exchange('Афоня', '11:30', 'QLB8529', 'ряд 5 место 26'))
print(ticket_1.print_info_ticket())
print()

ticket_1 = TicketInCinema('Астрал', '21:00', 'FNY123','Ряд 10 место 15' )
print(ticket_1.get_buy())
print(ticket_1.get_exchange('Астрал', '22:30', 'HBB8529', 'ряд 8 место 10'))
print(ticket_1.print_info_ticket())
