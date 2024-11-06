import pygame
import random

# Initialisation de pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jeu de smart_x")

# Charger les images
car_img = pygame.image.load("car.png")
car_img = pygame.transform.scale(car_img, (50, 70))

# Création de la voiture du joueur
car = pygame.Rect(375, 500, 50, 100)

# Création des voitures adverses
enemy_cars = []
for i in range(5):
    x = random.randint(0, 750)
    y = random.randint(-150, -50)
    enemy_cars.append(pygame.Rect(x, y, 50, 100))

# Création de la police d'écriture
font = pygame.font.Font(None, 36)

# Initialisation du score
score = 0

def music():
    source = pygame.mixer.Sound("music.mp3")
    source.play()

music()

# Création de l'horloge pour contrôler le FPS
clock = pygame.time.Clock()

# Création de la boucle de jeu
running = True
game_over = False
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not game_over:  # Mouvements seulement si le jeu n'est pas terminé
                if event.key == pygame.K_LEFT and car.x > 0:
                    car.x -= 50
                if event.key == pygame.K_RIGHT and car.x < 750:
                    car.x += 50
                if event.key == pygame.K_UP and car.y > 0:
                    car.y -= 50
                if event.key == pygame.K_DOWN and car.y < 500:
                    car.y += 50
            if event.key == pygame.K_r and game_over:  # Redémarrage du jeu
                car.x = 375
                car.y = 500
                score = 0
                game_over = False
                enemy_cars = [pygame.Rect(random.randint(0, 750), random.randint(-150, -50), 50, 100) for _ in range(5)]

    # Mise à jour des voitures adverses
    if not game_over:
        for enemy_car in enemy_cars:
            enemy_car.y += 5  # Déplacement vers le bas
            if enemy_car.y > 600:
                enemy_car.x = random.randint(0, 750)
                enemy_car.y = random.randint(-150, -50)
                score += 1  # Incrémentation du score

            # Détection des collisions
            if car.colliderect(enemy_car):
                game_over = True

    # Mise à jour de l'écran
    screen.fill((0, 0, 0))

    # Affichage de la voiture du joueur
    screen.blit(car_img, car)

    # Affichage des voitures adverses
    for enemy_car in enemy_cars:
        screen.blit(car_img, enemy_car)

    # Affichage du score
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Gestion de la fin du jeu
    if game_over:
        end_text = font.render("Game Over", True, (255, 0, 0))
        restart_text = font.render("Appuyez sur R pour recommencer", True, (255, 255, 255))
        screen.blit(end_text, (300, 200))
        screen.blit(restart_text, (200, 300))

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Contrôle du FPS
    clock.tick(60)




# Fermeture de pygame
pygame.quit()
