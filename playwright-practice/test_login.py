from playwright.sync_api import sync_playwright


class LoginPage:
    """
    Page Object pentru pagina de login.
    Grupează într-un singur loc toate locators + acțiuni legate de login,
    ca să nu le repeți în fiecare test care are nevoie de logare.
    """

    def __init__(self, page):
        # 'page' e obiectul Playwright care controlează tab-ul de browser.
        # Îl primim ca parametru, nu-l creăm aici — clasa doar îl folosește.
        self.page = page

    def goto(self):
        # Navighează la pagina de login
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        # Completează câmpurile și dă submit — un singur apel, în loc de 3 linii repetate
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")


class SecureAreaPage:
    """
    Page Object pentru pagina afișată DUPĂ login reușit.
    Separată de LoginPage pentru că reprezintă un alt "ecran" al aplicației,
    cu propriile elemente și acțiuni.
    """

    def __init__(self, page):
        self.page = page

    def get_flash_message(self):
        # Citește mesajul de succes/eroare afișat de site
        return self.page.inner_text(".flash")

    def logout(self):
        # Pregătită pentru viitor — nu e folosită încă în testul de mai jos,
        # dar există gata, dacă vrem să testăm și fluxul de logout
        self.page.click("a.button[href='/logout']")


# Blocul de mai jos rulează DOAR dacă rulezi acest fișier direct
# (nu dacă îl imporți din alt fișier, ex: dintr-un test pytest viitor)
if __name__ == "__main__":
    with sync_playwright() as p:
        # Pornim un Chrome vizibil (headless=False = îl vezi pe ecran)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Folosim LoginPage ca să ne logăm, fără să scriem locators direct aici
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("tomsmith", "SuperSecretPassword!")

        # Folosim SecureAreaPage ca să citim rezultatul și să-l verificăm
        secure_page = SecureAreaPage(page)
        message = secure_page.get_flash_message()

        assert "secure" in message        # confirmă succesul
        assert "invalid" not in message   # confirmă că nu a fost eroare

        browser.close()