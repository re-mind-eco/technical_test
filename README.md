# Test Technique

## API

### Ajout de livres

`POST /test/books/`

Paramètres de requête :

- `title` : Le titre du livre (obligatoire).
- `author` : L'auteur du livre (obligatoire).
- `description` : Une description du livre (optionnelle).
- `isbn` : Le numéro ISBN du livre (obligatoire et unique).
- `publication_date` : La date de publication du livre (optionnelle).

Exemple de requête : 

```json
POST /test/books/
Content-Type: application/json

{
    "title": "Nom du livre",
    "author": "Nom de l'auteur",
    "description": "Description du livre",
    "isbn": "1234567890",
    "publication_date": "2022-01-01"
}
```

### Recherche de livres

`GET /test/books/search/`

Paramètres de requête :

- `q` : Chaîne de caractères à rechercher dans le titre et l'auteur des livres.

Exemple de requête : `GET /test/books/search/?q=python`

## Comment lancer le projet

1. Clonez le dépôt Git
2. Dupliquez le fichier `template.env` en `.env`, puis remplissez les variables d'environnements
3. Construisez et lancez les conteneurs avec `docker-compose up --env-file .env up`.

Le serveur Django devrait maintenant être en cours d'exécution sur `localhost:8000`.


### Test réalisé par Wilquin Logan