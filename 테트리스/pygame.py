# game_functions.py
import pygame_gui
import pygame
import sys
 
 
def check_events(button1, button2, button3, kasa, add_cash, upgrade_system, upgrades, pygame_gui, manager, button_test):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        try:
            stara_rura(button1, kasa, event, pygame_gui, button_test)
            wiesniak(button2, kasa, event, pygame_gui, button_test)
            farmer(button3, kasa, event, pygame_gui, button_test)
        except AttributeError:
            pass
        manager.process_events(event)
        if event.type == add_cash:
            loop_cash(button1, button2, button3, kasa)
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_click(button1, button2, button3, kasa, upgrade_system, upgrades)
 
 
def button_costs(button1, button2, button3):
    button1.cost = 5
    button2.cost = 10
    button3.cost = 15
 
 
def update_screen(screen, ai_settings, button1, button2, button3, kasa, upgrade_system, upgrades, manager):
    screen.fill(ai_settings.bg_color)
    kasa.prep_cash()
    kasa.blitme()
    upgrade_system.prep_upg_count()
    upgrade_system.blitme()
    for upg in range(len(upgrades)):
        upgrade_system.blit_upgrades()
    show_upgrades(button1, button2, button3, upgrade_system, upgrades)
    button1.update_text()
    button2.update_text()
    button3.update_text()
    manager.update(120 / 1000.0)
    manager.draw_ui(screen)
    pygame.display.update()
 
 
def stara_rura(button1, kasa, event, pygame_gui, button_test):
    if event.type == button_test:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button1.draw:
                if kasa.cash >= button1.cost:
                    kasa.cash -= button1.cost
                    button1.cost *= 1.1
                    button1.button_cash += button1.button1_score
                    kasa.button_cash += button1.button1_score
                    button1.qty += 1
 
 
def wiesniak(button2, kasa, event, pygame_gui, button_test):
    if event.type == button_test:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button2.draw:
                if kasa.cash >= button2.cost:
                    kasa.cash -= button2.cost
                    button2.cost *= 1.2
                    button2.button_cash += 0.4
                    kasa.button_cash += 0.4
                    button2.qty += 1
 
def farmer(button3, kasa, event, pygame_gui, button_test):
    if event.type == button_test:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button3.draw:
                if kasa.cash >= button3.cost:
                    kasa.cash -= button3.cost
                    button3.cost *= 1.3
                    button3.button_cash += 0.6
                    kasa.button_cash += 0.6
                    button3.qty += 1
 
def button_click(button1, button2, button3, kasa, upgrade_system, upgrades):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if upgrade_system.image_rect.collidepoint(mouse_x, mouse_y):
        upgrade_system.upgrade_count += 1
        upgrade_system.prep_upg_count()
        button1.button_cash *= 1.5
        button1.button1_score *= 1.5
        kasa.button_cash = button1.button_cash
        upgrades.remove(upgrade_system)
 
 
def loop_cash(button1, button2, button3, kasa):
    kasa.cash += button1.button_cash
    kasa.cash += button2.button_cash
    kasa.cash += button3.button_cash
 
 
def show_upgrades(button1, button2, button3, upgrade_system, upgrades):
    if button1.qty in button1.upg_list and len(upgrades) <= 0:
        upgrades.append(upgrade_system)
        button1.qty = 0
 
# clicker_buttons.py
 
import pygame_gui
import pygame
 
 
class Buttons:
    def __init__(self, screen, ai_settings, x, y, text, manager):
        self.screen = screen
        self.ai_settings = ai_settings
        self.x = x
        self.y = y
        self.text = text
        self.manager = manager
        self.button_cash = 0
        self.button1_score = 0.2
        self.cost = 0
        self.qty = 0
        self.text_tip = 'Koszt: {}, Ilość: {}'.format(self.cost, self.qty)
        self.draw = pygame_gui.elements.UIButton(pygame.Rect((self.x, self.y), (150, 40)), self.text, self.manager,
                                                 None, self.text_tip)
        self.text_color = ai_settings.button_text_color
        self.font = pygame.font.Font(None, 36)
        self.cash_ps = self.font.render('Kasa/s: {}'.format(self.button_cash), True, self.text_color)
        self.upg_list = [10]
        self.update_text()
 
    def update_text(self):
        self.text_tip = 'Koszt: {}, Ilość: {}'.format(self.cost, self.qty)